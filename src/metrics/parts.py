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

    def __excerpt(self, part: str) -> pd.DataFrame:

        return self.__data.copy()[['epoch', part]]

    def code(self, part: str):
        """

        :param part:
        :return:
        """

        name = self.__codes[self.__codes['code'] == part, 'description'].array[0]
        excerpt = self.__excerpt(part=part)

    def segment(self, part: str):
        """

        :param part: For example, parent segment GF02, etc.
        :return:
        """

        name = self.__segments[self.__segments['segment_code'] == part, 'segment_description'].array[0]
        excerpt = self.__excerpt(part=part)
