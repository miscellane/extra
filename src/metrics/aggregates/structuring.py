import os
import pandas as pd

import src.metrics.tree
import src.functions.objects


class Structuring:
    """

    This class structures the output of src.metrics.aggregates.architecture for graphing purposes
    """

    def __init__(self, storage: str):
        """

        :param storage:
        """

        self.__storage = storage

        self.__partitions = ['annual_segment_total', 'annual_segment_%', 'series_delta_%']

    @staticmethod
    def __persist(dictionary: any, path: str) -> str:
        """

        :param dictionary:
        :param path:
        :return:
        """

        return src.functions.objects.Objects().write(nodes=dictionary, path=path)

    def __parts(self, blob: pd.DataFrame):

        aggregates = blob.copy()

        parts = []
        for partition in self.__partitions:
            frame = aggregates[['epoch', partition, 'segment_code']]
            structure = frame.pivot(index='epoch', columns='segment_code', values=partition)
            structure.reset_index(drop=False, inplace=True)
            structure.dropna(axis=0, inplace=True)

            # Either
            node = src.metrics.tree.Tree(data=structure, focus='segment_code').exc()

            # Or
            # node = structure.to_dict(orient='tight')
            # node['name'] = partition

            # Subsequently
            parts.append(node)

        return parts

    def exc(self, blob: pd.DataFrame) -> str:
        """

        :param blob:
        :return:
        """

        # The data partitions
        parts = self.__parts(blob=blob)

        # This structure declares an injective mapping: partitions[i] -> data[i]
        dictionary = {'partitions': self.__partitions, 'data': parts}

        return self.__persist(dictionary=dictionary, path=os.path.join(self.__storage, 'aggregates.json'))
