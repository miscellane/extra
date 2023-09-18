"""
vertex.py
"""
import pandas as pd

import src.cases.transactions


class Vertex:
    """
    Vertex
    """

    def __init__(self, data: pd.DataFrame, focus: str):
        """

        :param data:
        :param focus: 'code' or 'segment'
        """

        self.__data = data
        self.__focus = focus

        # The parent segments, e.g., defence, economic affairs, etc., and their child codes, e.g., military
        # defence (defence), civil defence (defence), etc.
        transactions = src.cases.transactions.Transactions()
        self.__codes = transactions.codes
        self.__segments = transactions.segments

    def __vertex(self, part: str, description: str) -> dict:
        """

        :param part:
        :param description:
        :return:
        """

        excerpt = self.__data.copy()[['epoch', part]]
        excerpt.rename(columns={'epoch': 'x', part: 'y'}, inplace=True)
        return {'name': part, 'description': description, 'data': excerpt.to_dict(orient='records')}

    def __desc_code(self, part: str) -> str:
        """

        :param part:
        :return:
        """

        return self.__codes.loc[self.__codes['code'] == part, 'description'].array[0]

    def __desc_segment(self, part: str) -> str:
        """

        :param part: For example, parent segment GF02, etc.
        :return:
        """

        return self.__segments.loc[self.__segments['segment_code'] == part, 'segment_description'].array[0]

    def exc(self, part: str) -> dict:
        """
        
        :param part:
        :return:
        """

        if self.__focus == 'code':
            description = self.__desc_code(part=part)
        else:
            description = self.__desc_segment(part=part)

        return self.__vertex(part=part, description=description)
