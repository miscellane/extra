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
