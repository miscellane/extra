"""
rebase.py
"""
import logging

import pandas as pd

import config
import src.functions.streams


class Rebase:
    """
    The United Kingdom's treasury releases a deflator series every year.  Each year the base year differs.  This
    class re-calculates the series such that the base year is config.Config().rebase_year
    """

    def __init__(self):
        """
        Constructor
        """

        configurations = config.Config()
        self.__deflator = configurations.deflator

        # logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        deflator = src.functions.streams.Streams().read(
            uri=self.__deflator.source, header=0, usecols=['year', 'quote'], dtype={'year': int, 'quote': float})

        value = deflator.loc[deflator['year'] == self.__deflator.rebase_year, 'quote'].array[0]
        deflator.loc[:, 'rebase'] = 100 * deflator['quote'] / value
        deflator.loc[:, 'kappa'] = deflator['rebase'] / 100
        self.__logger.info(deflator)

        return deflator
