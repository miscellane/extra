"""
interface.py
"""
import logging
import os

import pandas as pd
import dask

import config
import src.cases.expenditure
import src.functions.directories
import src.functions.streams


class Interface:
    """
    Interface
    """

    def __init__(self):
        """
        Constructor
        """

        self.__years = config.Config().expenditure.years

        # Storage
        self.__datapath = config.Config().expenditure.datapath
        self.__set_up()

        # Exporting
        self.__streams = src.functions.streams.Streams()
        self.__expenditure = src.cases.expenditure.Expenditure()

        # Logging
        logging.basicConfig(level=logging.INFO, format='\n%(message)s\n%(asctime)s.%(msecs).03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __set_up(self):
        """

        :return:
        """

        directories = src.functions.directories.Directories()
        directories.cleanup(path=self.__datapath)
        directories.create(path=self.__datapath)

    @dask.delayed
    def __expenditure_cases(self, year: int) -> pd.DataFrame:
        """

        :param year:
        :return:
        """

        return self.__expenditure.exc(year=year)

    @dask.delayed
    def __write(self, blob: pd.DataFrame, path: str) -> str:
        """

        :param blob:
        :param path:
        :return:
        """

        return self.__streams.write(blob=blob, path=path)

    def exc(self) -> list:
        """

        :return:
        """

        computations = []
        for year in self.__years:
            data = self.__expenditure_cases(year=year)
            message = self.__write(blob=data, path=os.path.join(self.__datapath, f'{str(year)}.csv'))
            computations.append(message)
        dask.visualize(computations, filename='computations.pdf')
        messages = dask.compute(computations, scheduler='threads')[0]

        return messages
