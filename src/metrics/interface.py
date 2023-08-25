"""
interface.py
"""
import os
import logging

import src.metrics.aggregates.architecture
import src.metrics.parent
import src.metrics.children
import src.metrics.tree
import src.functions.objects
import src.functions.directories


class Interface:
    """

    """

    def __init__(self):
        """

        """

        self.__storage = os.path.join(os.getcwd(), 'warehouse', 'expenditure', 'metrics')
        directories = src.functions.directories.Directories()
        directories.cleanup(path=self.__storage)
        directories.create(path=self.__storage)
        directories.create(path=os.path.join(self.__storage, 'disaggregates'))
        directories.create(path=os.path.join(self.__storage, 'children'))

        # logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self):
        """

        :return:
        """

        '''
        In-depth
        '''
        message = src.metrics.aggregates.architecture.Architecture(storage=self.__storage).exc()
        self.__logger.info(message)

        '''
        Simple
        '''
        message = src.metrics.parent.Parent(storage=self.__storage).exc()
        self.__logger.info(message)

        message = src.metrics.children.Children(storage=os.path.join(self.__storage, 'children')).exc()
        self.__logger.info(message)
