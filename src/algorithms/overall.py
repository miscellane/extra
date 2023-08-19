"""
overall.py
"""
import json
import logging
import os

import dask
import dask.dataframe
import pandas as pd

import config
import src.adjust.transactions
import src.functions.directories
import src.functions.streams


class Overall:
    """
    Overall
    """

    def __init__(self):
        """
        Constructor
        """

        # The overarching foci, i.e., segments, e.g., defence, economic affairs, etc.
        self.__segments = src.adjust.transactions.Transactions().segments

        # The calculations must be based on revalued data sets, hence comparable prices/costs across years.
        self.__datapath = config.Config().expenditure.datapath

        # The graphing data will be stored in ...
        self.__storage = os.path.join(os.getcwd(), 'warehouse', 'expenditure', 'graphs')
        src.functions.directories.Directories().create(self.__storage)

        # The fields in focus: The overall government expenditure per segment code is recorded in field <OTE>
        self.__usecols = ['code', 'OTE', 'segment_code', 'year']
        self.__rename_aggregates = {'year': 'x', 'total': 'y'}

        # logging
        logging.basicConfig(level=logging.INFO, format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __read(self) -> pd.DataFrame:
        """

        :return:
        """

        frame = dask.dataframe.read_csv(
            urlpath=os.path.join(self.__datapath, '*.csv'), usecols=self.__usecols)
        data = frame.compute().reset_index(drop=True)

        return data

    def __persist(self, dictionary) -> str:
        """

        :param dictionary:
        :return:
        """

        try:
            with open(os.path.join(self.__storage, 'overall.json'), 'w') as disk:
                json.dump(dictionary, disk)
            return 'overall.json: success'
        except IOError as err:
            raise Exception(err) from err

    def __aggregates(self, blob: pd.DataFrame) -> pd.DataFrame:
        """

        :param blob:
        :return:
        """

        aggregates = blob.copy().groupby(by=['segment_code', 'year']).agg(total=('OTE', sum))
        aggregates.reset_index(drop=False, inplace=True)
        aggregates.rename(columns=self.__rename_aggregates, inplace=True)

        return aggregates

    @dask.delayed
    def __node(self, aggregates: pd.DataFrame, segment_code: str) -> dict:
        """

        :param aggregates:
        :param segment_code:
        :return:
        """

        data = aggregates.loc[aggregates['segment_code'] == segment_code, ['x', 'y']]
        description = self.__segments.loc[
            self.__segments['segment_code'] == segment_code, 'segment_description'].array[0]

        node = {'name': segment_code, 'description': description, 'data': data.to_dict(orient='records')}

        return node

    def exc(self):
        """

        :return:
        """

        # Read-in the revalued data
        data = self.__read()

        # Get aggregates by segment
        aggregates = self.__aggregates(blob=data)

        # The unique segments
        segment_codes = aggregates['segment_code'].unique()

        computations = []
        for segment_code in segment_codes:
            node = self.__node(aggregates=aggregates, segment_code=segment_code)
            computations.append(node)
        dictionary = dask.compute(computations, scheduler='threads')[0]
        message = self.__persist(dictionary=dictionary)

        self.__logger.info(message)
