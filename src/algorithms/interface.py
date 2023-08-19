import os

import src.algorithms.overall
import src.algorithms.excerpts

import src.functions.directories


class Interface:

    def __init__(self):
        pass

    @staticmethod
    def graphs():

        path = os.path.join(os.getcwd(), 'warehouse', 'expenditure', 'graphs')

        directories = src.functions.directories.Directories()
        directories.cleanup(path=path)
        for pathstr in [path, os.path.join(path, 'excerpts')]:
            directories.create(path=pathstr)

        src.algorithms.overall.Overall(storage=path).exc()
        src.algorithms.excerpts.Excerpts(storage=os.path.join(path, 'excerpts')).exc()
