"""
interface.py
"""
import os
import logging

import src.metrics.aggregates
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

    @staticmethod
    def __persist(dictionary: any, path: str) -> str:
        """

        :param dictionary:
        :return:
        """

        return src.functions.objects.Objects().write(nodes=dictionary, path=path)

    def __disaggregates(self):
        pass

    def __aggregates(self) -> str:
        """
        * structure.to_dict(orient='tight')
        
        :return: 
        """

        aggregates = src.metrics.aggregates.Aggregates().exc()
        partitions = ['annual_segment_total', 'annual_segment_%', 'series_delta_%']

        parts = []
        for partition in partitions:
            frame = aggregates[['epoch', partition, 'segment_code']]
            structure = frame.pivot(index='epoch', columns='segment_code', values=partition)
            structure.reset_index(drop=False, inplace=True)
            structure.dropna(axis=0, inplace=True)

            # Either
            node = src.metrics.tree.Tree(data=structure, focus='segment_code').exc()

            # Or
            # node = structure.to_dict(orient='tight')
            # node['name'] = partition

            # Then
            parts.append(node)

        dictionary = {'partitions': partitions, 'data': parts}

        return self.__persist(dictionary=dictionary, path=os.path.join(self.__storage, 'aggregates.json'))

    def exc(self):

        message = self.__aggregates()
        self.__logger.info(message)

        message = src.metrics.parent.Parent(storage=self.__storage).exc()
        self.__logger.info(message)

        message = src.metrics.children.Children(storage=os.path.join(self.__storage, 'children')).exc()
        self.__logger.info(message)
