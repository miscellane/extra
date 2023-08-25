"""
aggregates.py
"""
import os

import dask.dataframe
import numpy as np
import pandas as pd

import config
import src.functions.streams


class Aggregates:
    """
    Overall
    """

    def __init__(self, storage: str):
        """

        """

        self.__storage = storage

        # The calculations must be based on revalued data sets, hence comparable prices/costs across years.
        self.__datapath = config.Config().expenditure.datapath

        # The fields in focus: The overall government expenditure per segment code is recorded in field <OTE>
        self.__usecols = ['code', 'OTE', 'segment_code', 'year', 'epoch']

    def __read(self) -> pd.DataFrame:
        """

        :return:
        """

        frame = dask.dataframe.read_csv(
            urlpath=os.path.join(self.__datapath, '*.csv'), usecols=self.__usecols)
        data = frame.compute().reset_index(drop=True)

        return data

    @staticmethod
    def __segments(blob: pd.DataFrame) -> pd.DataFrame:
        """

        :param blob:
        :return:
        """

        # Per epoch year, what is each segment's expenditure?
        aggregates = blob.copy().groupby(by=['segment_code', 'epoch', 'year']).agg(annual_segment_total=('OTE', sum))
        aggregates.reset_index(drop=False, inplace=True)

        # Per epoch year, what is each segment's percentage expenditure?
        temporary = aggregates.groupby(by=['epoch']).agg(denominator=('annual_segment_total', sum))
        temporary.reset_index(drop=False, inplace=True)
        temporary = aggregates.merge(temporary.copy(), how='left', on='epoch')
        temporary.loc[:, 'annual_segment_%'] = 100 * temporary['annual_segment_total'] / temporary['denominator']

        return temporary

    @staticmethod
    def __series(blob: pd.DataFrame) -> pd.DataFrame:
        """

        :param blob:
        :return:
        """

        temporary = blob.copy()

        # Per segment code time series, evaluate the delta percentage vis-à-vis the previous year
        temporary.sort_values(by=['segment_code', 'epoch'], ascending=True, inplace=True)
        temporary.loc[:, 'series_delta'] = temporary.groupby(by=['segment_code'])['annual_segment_total'].diff().fillna(np.NaN)
        temporary.loc[:, 'series_shift'] = temporary['annual_segment_total'].shift(periods=1, fill_value=np.NaN)
        temporary.loc[:, 'series_delta_%'] = 100 * temporary['series_delta'] / temporary['series_shift']

        return temporary

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        # Read-in the revalued data
        data = self.__read()

        # Per segment code, how much was spent each epoch year?
        data = self.__segments(blob=data)
        data = self.__series(blob=data)

        # Write
        src.functions.streams.Streams().write(blob=data, path=os.path.join(self.__storage, 'aggregates.csv'))

        return data
