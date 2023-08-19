import json
import os

import dask
import dask.dataframe
import pandas as pd

import config
import src.adjust.transactions
import src.functions.streams


class Excerpts:

    def __init__(self, storage: str):
        """

        :param storage:
        """

        # The resulting graphing data will be stored in ...
        self.__storage = storage

        # The overarching foci, i.e., segments, e.g., defence, economic affairs, etc.
        self.__codes = src.adjust.transactions.Transactions().codes

        # The calculations must be based on revalued data sets, hence comparable prices/costs across years.
        datapath = config.Config().expenditure.datapath
        self.__data = self.__read(datapath=datapath)

        # The fields in focus: The overall government expenditure per segment code is recorded in field <OTE>
        self.__usecols = ['code', 'description', 'OTE', 'segment_code', 'year']
        self.__rename_fields = {'year': 'x', 'OTE': 'y'}

    def __read(self, datapath: str) -> pd.DataFrame:
        """

        :param datapath:
        :return:
        """

        frame = dask.dataframe.read_csv(
            urlpath=os.path.join(datapath, '*.csv'), usecols=self.__usecols)
        data = frame.compute().reset_index(drop=True)
        data.rename(columns=self.__rename_fields, inplace=True)

        return data

    @dask.delayed
    def __persist(self, dictionary: list, segment_code: str) -> str:
        """

        :param dictionary:
        :return:
        """

        try:
            with open(os.path.join(self.__storage, f'{segment_code}.json'), 'w') as disk:
                json.dump(dictionary, disk)
            return f'{segment_code}.json: success'
        except IOError as err:
            raise Exception(err) from err

    @dask.delayed
    def __nodes(self, segment_code: str) -> list:
        """

        :param segment_code:
        :return:
        """

        frame = self.__data.copy().loc[self.__data['segment_code'] == segment_code, :]
        codes = frame['code'].unique()

        structure = []
        for code in codes:
            partition = frame[frame['code'] == code, :]
            data = partition[['x', 'y']]
            description = self.__codes.loc[self.__codes['code'] == code, 'description'].array[0]
            structure.append({'name': code, 'description': description, 'data': data.to_dict(orient='records')})
        return structure

    def exc(self) -> list:
        """

        :return:
        """

        # Read-in the revalued data

        segment_codes = self.__data['segment_code'].unique()

        computations = []
        for segment_code in segment_codes:
            dictionary = self.__nodes(segment_code)
            message = self.__persist(dictionary=dictionary, segment_code=segment_code)
            computations.append(message)
        messages = dask.compute(computations, scheduler='threads')[0]

        return messages
