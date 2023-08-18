"""
overall.py
"""
import logging
import os

import dask
import dask.dataframe
import pandas as pd

import config
import src.adjust.transactions
import src.functions.streams


class Overall:
    """
    Overall
    """

    def __init__(self):
        """
        Constructor
        """

        self.__segments = src.adjust.transactions.Transactions().segments

        # The overall government expenditure per segment code is recorded in field <OTE> 
        self.__usecols = ['code', 'OTE', 'segment_code', 'year']

        # The path to the revalued data sets
        self.__datapath = config.Config().expenditure.datapath

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

    @staticmethod
    def __aggregates(blob: pd.DataFrame) -> pd.DataFrame:

        data = blob.copy()
        aggregates = data.groupby(by=['segment_code', 'year']).agg(total=('OTE', sum))
        aggregates.reset_index(drop=False, inplace=True)

        return aggregates

    @dask.delayed
    def __node(self, aggregates: pd.DataFrame, segment_code: str) -> dict:
        """

        :param aggregates:
        :param segment_code:
        :return:
        """

        data = aggregates.loc[aggregates['segment_code'] == segment_code, ['year', 'total']]
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

        #
        aggregates = self.__aggregates(blob=data)
        segment_codes = aggregates['segment_code'].unique()

        computations = []
        for segment_code in segment_codes:
            node = self.__node(aggregates=aggregates, segment_code=segment_code)
            computations.append(node)
        summary = dask.compute(computations, scheduler='threads')[0]

        self.__logger.info(summary)
