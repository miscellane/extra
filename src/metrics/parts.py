import pandas as pd


class Parts:

    def __init__(self, data: pd.DataFrame):
        """

        :param data:
        """

        self.__data = data

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
