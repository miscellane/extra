import pandas as pd
import os
import logging

import src.functions.streams
import src.functions.directories
import src.cases.expenditure

import config


class Interface:

    def __init__(self):

        self.__years = config.Config().expenditure.years

        # Storage
        self.__datasets = config.Config().expenditure.datasets
        self.__set_up()

        # Exporting
        self.__streams = src.functions.streams.Streams()
        self.__expenditure = src.cases.expenditure.Expenditure()

        # Logging
        logging.basicConfig(level=logging.INFO, format='\n%(message)s\n%(asctime)s.%(msecs).03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __set_up(self):

        directories = src.functions.directories.Directories()
        directories.cleanup(path=self.__datasets)
        directories.create(path=self.__datasets)

    def __expenditure_cases(self, year: int) -> pd.DataFrame:

        return self.__expenditure.exc(year=year)

    def __write(self, blob: pd.DataFrame, path: str) -> str:

        return self.__streams.write(blob=blob, path=path)

    def exc(self):

        for year in self.__years[:1]:

            data = self.__expenditure_cases(year=year)
            self.__logger.info(data.head())

            message = self.__write(blob=data, path=os.path.join(self.__datasets, f'{str(year)}.csv'))
            self.__logger.info(message)
