"""
tree.py
"""
import os

import dask
import numpy as np
import pandas as pd

import src.metrics.vertex


class Tree:
    """
    Tree
    """

    def __init__(self, data: pd.DataFrame, focus: str):
        """

        :param data:
        :param focus:
        """

        self.__fields = data.columns.drop(labels=['epoch'])
        self.__vertex = src.metrics.vertex.Vertex(data=data, focus=focus)

    @dask.delayed
    def __part(self, field: str) -> dict:
        """

        :param field:
        :return:
        """

        return self.__vertex.exc(part=field)

    def exc(self) -> list:
        """

        :return:
        """

        computations = []
        for field in self.__fields:
            part = self.__part(field=field)
            computations.append(part)
        dictionary = dask.compute(computations, scheduler='threads')[0]

        return dictionary
