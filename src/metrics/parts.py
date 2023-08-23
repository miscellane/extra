import pandas as pd

import src.adjust.transactions


class Parts:

    def __init__(self, data: pd.DataFrame):
        """

        :param data:
        """

        self.__data = data

        # The parent segments, e.g., defence, economic affairs, etc., and their child codes, e.g., military
        # defence (defence), civil defence (defence), etc.
        transactions = src.adjust.transactions.Transactions()
        self.__codes = transactions.codes
        self.__segments = transactions.segments

    def code(self, part: str):
        """

        :param part:
        :return:
        """

    def segment(self, part: str):
        """

        :param part: For example, parent segment GF02, child segment GF0201, etc.
        :return:
        """

        fields = ['epoch', part]
