"""
overall.py
"""
import logging
import os

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

    def __node(self, aggregates: pd.DataFrame, segment_code: str):
        """

        :param aggregates:
        :param segment_code:
        :return:
        """

        data = aggregates.loc[aggregates['segment_code'] == segment_code, ['year', 'total']]
        self.__logger.info(data)
        description = self.__segments.loc[self.__segments['segment_code'] == segment_code, 'segment_description'].array[
            0]

        node = {'name': segment_code, 'description': description, 'data': data.to_dict(orient='records')}
        self.__logger.info(node)

    def exc(self):
        """

        :return:
        """

        data = self.__read()
        aggregates = data.groupby(by=['segment_code', 'year']).agg(total=('OTE', sum))
        aggregates.reset_index(drop=False, inplace=True)
        segment_codes = aggregates['segment_code'].unique()

        for segment_code in segment_codes:
            self.__node(aggregates=aggregates, segment_code=segment_code)
