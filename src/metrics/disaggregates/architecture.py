"""
architecture.py
"""
import os
import logging

import dask.dataframe
import numpy as np
import pandas as pd

import config
import src.functions.streams


class Architecture:

    def __init__(self, blob: pd.DataFrame, storage: str):

        self.__blob = blob
        self.__storage = storage

        # The calculations must be based on revalued data sets, hence comparable prices/costs across years.
        self.__datapath = config.Config().expenditure.revalued_

        # The fields in focus: The overall government expenditure per segment code is recorded in field <OTE>
        self.__usecols = ['code', 'OTE', 'segment_code', 'year', 'epoch']

        # logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
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

    @dask.delayed
    def __transactions(self, segment_code: str) -> pd.DataFrame:

        # The records of a segment
        data: pd.DataFrame = self.__blob.copy().loc[self.__blob['segment_code'] == segment_code, :]

        # Per epoch year, what is each code's percentage?
        temporary = data.groupby(by=['epoch']).agg(denominator=('OTE', sum))
        data = data.copy().merge(temporary.copy(), how='left', on='epoch')
        data.loc[:, 'annual_code_%'] = 100 * data['OTE'] / data['denominator']

        return data

    @dask.delayed
    def __series(self, blob: pd.DataFrame) -> pd.DataFrame:
        """

        :param blob:
        :return:
        """

        data = blob.copy()

        # Per segment code time series, evaluate the delta percentage vis-à-vis the previous year
        data.sort_values(by=['code', 'epoch'], ascending=True, inplace=True)
        data.loc[:, 'series_delta'] = data.groupby(by=['code'])['OTE'].diff().fillna(np.NaN)
        data.loc[:, 'series_shift'] = data.groupby(by=['code'])['OTE'].shift(periods=1, fill_value=np.NaN)
        data.loc[:, 'series_delta_%'] = 100 * data['series_delta'] / data['series_shift']

        return data

    def exc(self):

        # Read-in the revalued data
        data = self.__read()
        self.__logger.info(data)
        segment_codes = data['segment_code'].unique()
        self.__logger.info(segment_codes)

        for segment_code in segment_codes:
            self.__logger.info(data.loc[data['segment_code'] == segment_code,  ['segment_code', 'code']].drop_duplicates())
