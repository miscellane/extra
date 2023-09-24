"""
architecture.py
"""
import os
import pandas as pd

import src.metrics.tree
import src.functions.objects


class Structuring:
    """
    Structuring
    """

    def __init__(self, storage: str):
        """

        :param storage:
        """

        self.__storage = storage

        self.__partitions = ['OTE', 'annual_code_%', 'series_delta_%']

    @staticmethod
    def __persist(dictionary: any, path: str) -> str:
        """

        :param dictionary:
        :param path:
        :return:
        """

        return src.functions.objects.Objects().write(nodes=dictionary, path=path)

    def __parts(self, blob: pd.DataFrame):
        """

        :param blob:
        :return:
        """

        aggregates = blob.copy()

        parts = []
        for partition in self.__partitions:
            frame = aggregates[['epoch', partition, 'code']]
            structure = frame.pivot(index='epoch', columns='code', values=partition)
            structure.reset_index(drop=False, inplace=True)
            structure.dropna(axis=0, inplace=True)

            # Either
            node = src.metrics.tree.Tree(data=structure, focus='code').exc()

            # Subsequently
            parts.append(node)

        return parts

    def exc(self, blob: pd.DataFrame, segment_code) -> str:
        """

        :param blob:
        :param segment_code
        :return:
        """

        # The data partitions
        parts = self.__parts(blob=blob)

        # This structure declares an injective mapping: partitions[i] -> data[i]
        dictionary = {'partitions': self.__partitions, 'data': parts}

        return self.__persist(dictionary=dictionary, path=os.path.join(self.__storage, f'{segment_code}.json'))
