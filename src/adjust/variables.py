"""
variables.py
"""
import os

import pandas as pd

import src.functions.streams


class Variables:
    """

    """

    def __init__(self):
        """

        """

        self.__uri = os.path.join(os.getcwd(), 'data', 'variables.csv')

        # the variables data
        self.data: pd.DataFrame = self.__exc()

    def __exc(self) -> pd.DataFrame:
        """

        :return:
        """

        data = src.functions.streams.Streams().read(
            uri=self.__uri, header=0, usecols=['variable', 'description'], dtype={'variable': str, 'description': str})

        return data
