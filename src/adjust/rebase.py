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

    def __calculate(self, data: pd.DataFrame) -> pd.DataFrame:
        """

        :param data:
        :return:
        """

        # The <quote> of the rebase year is the rebasing denominator
        value = data.loc[data['year'] == self.__deflator.rebase_year, 'quote'].array[0]
        data.loc[:, 'rebase'] = 100 * data['quote'] / value
        data.loc[:, 'kappa'] = data['rebase'] / 100

        return data

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        frame = src.functions.streams.Streams().read(
            uri=self.__deflator.source, header=0, usecols=['year', 'quote'], dtype={'year': int, 'quote': float})
        frame = self.__calculate(data=frame.copy())
        self.__logger.info(frame)

        return frame
