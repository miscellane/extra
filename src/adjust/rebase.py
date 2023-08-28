"""
rebase.py
"""
import logging
import os

import pandas as pd
import numpy as np

import config
import src.functions.streams
import src.functions.objects
import src.functions.directories


class Rebase:
    """
    The United Kingdom's treasury releases a deflator series every year.  Each year the base year differs.  This
    class re-calculates the series such that the base year is config.Config().rebase_year
    """

    def __init__(self):
        """
        Constructor
        """

        # the metadata of the deflator series
        configurations = config.Config()
        self.__deflator = configurations.deflator

        # storage
        directories = src.functions.directories.Directories()
        directories.cleanup(self.__deflator.storage)
        directories.create(self.__deflator.storage)

        # logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

        # the rebase data
        self.data = self.__exc()

    @staticmethod
    def __epoch(series: pd.Series) -> pd.Series:
        """

        :param series:
        :return:
        """

        nanoseconds = pd.to_datetime(series.astype(str), format='%Y').astype(np.int64)
        milliseconds: pd.Series = (nanoseconds / (10 ** 6)).astype(np.longlong)

        return milliseconds

    def __persist(self, blob: pd.DataFrame) -> str:
        """

        :param blob:
        :return:
        """

        data = blob.copy().loc[blob['year'] >= 1971, ['epoch', 'rebase']]
        data.rename(columns={'epoch': 'x', 'rebase': 'y'}, inplace=True)
        dictionary = {'name': 'deflator',
                      'description': f'Deflator Series (Base Year: {self.__deflator.rebase_year})',
                      'data': data.to_dict(orient='records')}
        return src.functions.objects.Objects().write(
            nodes=dictionary, path=os.path.join(self.__deflator.storage, 'series.json'))

    def __calculate(self, data: pd.DataFrame) -> pd.DataFrame:
        """

        :param data:
        :return:
        """

        # The <quote> of the rebase year is the rebasing denominator
        value = data.loc[data['year'] == self.__deflator.rebase_year, 'quote'].array[0]
        data.loc[:, 'rebase'] = 100 * data['quote'] / value
        data.loc[:, 'kappa'] = 100 / data['rebase']
        data.loc[:, 'epoch'] = self.__epoch(series=data['year']).values

        return data

    def __exc(self) -> pd.DataFrame:
        """

        :return:
        """

        # Reading-in the raw deflator data
        data = src.functions.streams.Streams().read(
            uri=self.__deflator.source, header=0, usecols=['year', 'quote'], dtype={'year': int, 'quote': float})

        # Rebasing the data
        data = self.__calculate(data=data.copy())
        self.__logger.info(data)

        # Store
        self.__persist(blob=data)

        return data
