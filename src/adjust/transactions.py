"""
transactions.py
"""
import os

import pandas as pd

import src.functions.streams
import src.functions.objects


class Transactions:

    def __init__(self):
        """
        Constructor
        """

        self.__uri = os.path.join(os.getcwd(), 'data', 'expenditure', 'expenditure_transaction_types.csv')

        # the variables data
        self.codes: pd.DataFrame = self.__codes()
        self.segments: pd.DataFrame = self.__segments()

    def __codes(self) -> pd.DataFrame:
        """

        :return:
        """

        data = src.functions.streams.Streams().read(
            uri=self.__uri, header=0, usecols=['code', 'description'],
            dtype={'code': str, 'description': str})

        return data

    def __segments(self) -> pd.DataFrame:
        """

        :return:
        """

        data = src.functions.streams.Streams().read(
            uri=self.__uri, header=0, usecols=['segment_code', 'segment_description'],
            dtype={'segment_code': str, 'segment_description': str})
        data.drop_duplicates(inplace=True)

        return data
