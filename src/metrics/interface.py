"""
interface.py
"""
import collections
import logging
import os

import src.functions.directories
import src.metrics.aggregates.architecture
import src.metrics.children.architecture
import src.metrics.parent.architecture


class Interface:
    """
    Interface
    """

    def __init__(self):
        """
        Constructor
        """

        # Storage
        self.__storage = os.path.join(os.getcwd(), 'warehouse', 'expenditure', 'metrics')

        # Depositories
        Paths = collections.namedtuple(
            typename='Paths', field_names=['aggregates', 'disaggregates', 'parent', 'children'])
        self.__paths = Paths(aggregates=self.__storage, disaggregates=os.path.join(self.__storage, 'disaggregates'),
                             parent=self.__storage, children=os.path.join(self.__storage, 'children'))
        self.__directories()

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __directories(self):
        """

        :return:
        """

        directories = src.functions.directories.Directories()
        directories.cleanup(path=self.__storage)

        for path in list(self.__paths):
            directories.create(path=path)

    def exc(self):
        """

        :return:
        """

        '''
        In-depth
        '''
        message = src.metrics.aggregates.architecture.Architecture(storage=self.__paths.aggregates).exc()
        self.__logger.info(message)

        '''
        Simple
        '''
        message = src.metrics.parent.architecture.Architecture(storage=self.__paths.parent).exc()
        self.__logger.info(message)

        message = src.metrics.children.architecture.Architecture(storage=self.__paths.children).exc()
        self.__logger.info(message)
