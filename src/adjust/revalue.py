"""
revalue.py
"""
import glob
import os
import pathlib

import numpy as np
import pandas as pd
import dask

import config
import src.adjust.rebase
import src.adjust.variables
import src.functions.streams
import src.functions.directories


class Revalue:
    """
    Revalue
    """

    def __init__(self):
        """
        Constructor
        """

        # Expenditure metadata
        self.__expenditure = config.Config().expenditure
        self.__datapath = self.__expenditure.datapath
        directories = src.functions.directories.Directories()
        directories.cleanup(self.__datapath)
        directories.create(self.__datapath)

        # The rebase values, and variables, for revaluation
        self.__rebase: pd.DataFrame = src.adjust.rebase.Rebase().data
        fields = src.adjust.variables.Variables().fields
        self.__fields: np.ndarray = np.setdiff1d(fields, self.__expenditure.unavailable)

        # Instances
        self.__streams = src.functions.streams.Streams()

    @dask.delayed
    def __read(self, path) -> pd.DataFrame:
        """

        :param path: Path to data file
        :return:
        """

        return self.__streams.read(uri=path, header=0)

    @dask.delayed
    def __streamline(self, blob: pd.DataFrame) -> pd.DataFrame:
        """

        :param blob: A year's expenditure data
        :return:
        """

        # Focusing on the available fields
        spectrum = np.setdiff1d(blob.columns, self.__expenditure.unavailable)

        return blob.copy()[spectrum]

    @dask.delayed
    def __revalue(self, blob: pd.DataFrame, year: int) -> pd.DataFrame:
        """
        Revaluing vis-à-vis the rebase year

        :param blob: A year's expenditure data, which excludes fields without data
        :param year: Year
        :return:
        """

        data = blob.copy()
        kappa = self.__rebase.loc[self.__rebase['year'] == year, 'kappa'].array[0]
        data.loc[:, self.__fields] = kappa * data[self.__fields]

        return data

    @dask.delayed
    def __write(self, blob: pd.DataFrame, year: int) -> str:
        """

        :param blob: Revalued data
        :param year: Year
        :return:
        """

        return self.__streams.write(blob=blob,
                                    path=os.path.join(self.__datapath, f'{year}.csv'))

    def exc(self) -> list:
        """

        :return:
        """

        paths = glob.glob(pathname=os.path.join(self.__expenditure.destination, '*.csv'))

        computations = []
        for path in paths:
            data = self.__read(path=path)
            data = self.__streamline(blob=data)
            data = self.__revalue(blob=data, year=int(pathlib.Path(path).stem))
            message = self.__write(blob=data, year=int(pathlib.Path(path).stem))
            computations.append(message)
        messages = dask.compute(computations, scheduler='threads')[0]

        return messages
