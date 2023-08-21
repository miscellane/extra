"""
overall.py
"""
import os

import dask
import dask.dataframe
import pandas as pd

import config
import src.adjust.transactions
import src.functions.directories
import src.functions.objects
import src.functions.streams


class Overall:
    """
    Overall
    """

    def __init__(self, storage: str):
        """

        :param storage:
        """

        # The resulting graphing data will be stored in ...
        self.__storage = storage

        # The overarching foci, i.e., segments, e.g., defence, economic affairs, etc.
        self.__segments = src.adjust.transactions.Transactions().segments

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

    def __persist(self, dictionary) -> str:
        """

        :param dictionary:
        :return:
        """

        return src.functions.objects.Objects().write(
            nodes=dictionary, path=os.path.join(self.__storage, 'overall.json'))

    @staticmethod
    def __aggregates(blob: pd.DataFrame) -> pd.DataFrame:
        """

        :param blob:
        :return:
        """

        aggregates = blob.copy().groupby(by=['segment_code', 'epoch']).agg(total=('OTE', sum))
        aggregates.reset_index(drop=False, inplace=True)

        return aggregates

    def exc(self):
        """

        :return:
        """

        # Read-in the revalued data
        data = self.__read()

        # Get aggregates by segment
        aggregates = self.__aggregates(blob=data)
        aggregates.sort_values(by=['segment_code', 'year'], ascending=True, inplace=True)

        # Extend: a sum per epoch year field
        temporary = aggregates.groupby(by=['epoch']).agg(denominator=('total', sum))
        temporary.reset_index(drop=False, inplace=True)
        temporary = aggregates.merge(temporary.copy(), how='left', on='epoch')
        print(temporary.loc[temporary['epoch'] == 1609459200000, :])

        # delta
        temporary.loc[:, 'segment_delta'] = temporary.groupby(by=['segment_code'])['total'].diff().fillna(0)
        print(temporary.loc[temporary['segment_code'] == 'GF01', :])
