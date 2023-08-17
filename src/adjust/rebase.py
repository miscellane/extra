"""
rebase.py
"""
import logging

import config
import src.functions.streams


class Rebase:
    """
    The United Kingdom's treasury releases a deflator series every year.  Each year the base year differs.  This
    class re-calculates the series such that the base year is config.Config().rebase_year
    """

    def __init__(self):
        configurations = config.Config()
        self.deflator_rebase_year = configurations.deflator_rebase_year
        self.deflator_file = configurations.deflator_file

        # logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self):
        deflator = src.functions.streams.Streams().read(
            uri=self.deflator_file, header=0, usecols=['year', 'series'], dtype={'year': int, 'series': float})

        value = deflator.loc[deflator['year'] == self.deflator_rebase_year, 'base']
        self.__logger.info(type(value))
        self.__logger.info(value)
