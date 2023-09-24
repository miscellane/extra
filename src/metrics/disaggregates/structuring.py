import os
import pandas as pd

import src.metrics.tree
import src.functions.objects


class Structuring:

    def __init__(self, storage: str):
        """

        :param storage:
        """

        self.__storage = storage

        self.__partitions = ['OTE', 'annual_segment_%', 'series_delta_%']

    def __persist(self, dictionary: any, path: str) -> str:
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
            frame = aggregates[['epoch', partition, 'code']]
            structure = frame.pivot(index='epoch', columns='code', values=partition)
            structure.reset_index(drop=False, inplace=True)
            structure.dropna(axis=0, inplace=True)

            # Either
            node = src.metrics.tree.Tree(data=structure, focus='code').exc()

            # Or
            # node = structure.to_dict(orient='tight')
            # node['name'] = partition

            # Subsequently
            parts.append(node)

        return parts
