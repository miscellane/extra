import os

import dask
import dask.dataframe
import pandas as pd

import config
import src.adjust.transactions
import src.functions.objects
import src.functions.streams


class Excerpts:

    def __init__(self, storage: str):
        """

        :param storage:
        """

        # The resulting graphing data will be stored in ...
        self.__storage = storage
        self.__objects = src.functions.objects.Objects()

        # The overarching foci, i.e., segments, e.g., defence, economic affairs, etc.
        self.__codes = src.adjust.transactions.Transactions().codes

        # The calculations must be based on revalued data sets, hence comparable prices/costs across years.
        # The fields in focus: The overall government expenditure per segment code is recorded in field <OTE>
        datapath = config.Config().expenditure.datapath
        self.__data = self.__read(datapath=datapath, usecols=['code', 'description', 'OTE', 'segment_code', 'year'],
                                  rename_fields={'year': 'x', 'OTE': 'y'})

    @staticmethod
    def __read(datapath: str, usecols: list, rename_fields: dict) -> pd.DataFrame:
        """

        :param datapath:
        :return:
        """

        frame = dask.dataframe.read_csv(
            urlpath=os.path.join(datapath, '*.csv'), usecols=usecols)
        data = frame.compute().reset_index(drop=True)
        data.rename(columns=rename_fields, inplace=True)

        return data

    @dask.delayed
    def __persist(self, dictionary: list, segment_code: str) -> str:
        """

        :param dictionary:
        :return:
        """

        return self.__objects.write(
            nodes=dictionary, path=os.path.join(self.__storage, f'{segment_code}.json'))

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
            partition = frame.copy().loc[frame['code'] == code, :]
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
