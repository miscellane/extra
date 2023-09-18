"""
aggregates.py
"""
import logging
import os

import src.diagrams.classifications
import src.functions.directories


class Interface:

    def __init__(self):

        # Storage
        self.__storage = os.path.join(os.getcwd(), 'warehouse', 'expenditure', 'diagrams')

        # And
        self.__classifications = src.diagrams.classifications.Classifications(storage=self.__storage)

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __aggregates(self):

        uri = os.path.join(os.getcwd(), 'data', 'expenditure', 'expenditure_transaction_types_aggregates.csv')

        fields = {'parent_identifier': 'parent', 'parent_description': 'parent_desc', 'child_identifier': 'id',
                  'child_description': 'child_desc'}

        # Data structure: Aggregates
        self.__classifications.exc(uri=uri, fields=fields, name='aggregates')

    def __disaggregates(self):

        uri = os.path.join(os.getcwd(), 'data', 'expenditure', 'expenditure_transaction_types_disaggregates.csv')

        fields = {'parent_identifier': 'parent', 'parent_description': 'parent_desc', 'child_identifier': 'id',
                  'child_description': 'child_desc'}

        # Data structure: Aggregates -> Disaggregates
        self.__classifications.exc(uri=uri, fields=fields, name='disaggregates')

    def exc(self):

        directories = src.functions.directories.Directories()
        directories.cleanup(path=self.__storage)
        directories.create(path=self.__storage)

        self.__logger.info('Data structures for illustrations')
        self.__aggregates()
        self.__disaggregates()
