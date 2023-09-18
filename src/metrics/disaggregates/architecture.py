"""
architecture.py
"""
import os

import dask.dataframe
import numpy as np
import pandas as pd

import config
import src.functions.streams


class Architecture:

    def __init__(self, storage: str):

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

    def exc(self):

        # Read-in the revalued data
        data = self.__read()






