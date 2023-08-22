"""
interface.py
"""
import logging
import os

import src.algorithms.parent
import src.algorithms.children

import src.functions.directories


class Interface:
    """

    """

    def __init__(self):
        """

        """

        # Logging
        logging.basicConfig(level=logging.INFO, format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def graphs(self):
        """

        :return:
        """

        path = os.path.join(os.getcwd(), 'warehouse', 'expenditure', 'graphs')

        directories = src.functions.directories.Directories()
        directories.cleanup(path=path)
        for pathstr in [path, os.path.join(path, 'excerpts')]:
            directories.create(path=pathstr)

        message = src.algorithms.parent.Parent(storage=path).exc()
        self.__logger.info(message)

        message = src.algorithms.children.Children(storage=os.path.join(path, 'excerpts')).exc()
        self.__logger.info(message)
