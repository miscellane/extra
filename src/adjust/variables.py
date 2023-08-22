"""
variables.py
"""
import os

import numpy as np
import pandas as pd

import src.functions.streams


class Variables:
    """
    Each transaction code expenditure can be broken down into different parts.  The expenditure
    variables describe these parts; some parts are aggregates of others.
    """

    def __init__(self):
        """

        """

        self.__uri = os.path.join(os.getcwd(), 'data', 'expenditure', 'expenditure_variables.csv')

        # the variables data
        self.data: pd.DataFrame = self.__exc()
        self.fields: np.ndarray = self.data['field'].to_numpy()

    def __exc(self) -> pd.DataFrame:
        """

        :return:
        """

        data = src.functions.streams.Streams().read(
            uri=self.__uri, header=0, usecols=['field', 'description'], dtype={'field': str, 'description': str})

        return data
