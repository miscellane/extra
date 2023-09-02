"""
aggregates.py
"""
import logging
import os

import pandas as pd

import src.functions.directories
import src.functions.objects
import src.functions.streams


class Aggregates:

    def __init__(self, storage: str):
        """

        :param storage:
        """

        self.__storage = storage

        self.__uri = os.path.join(os.getcwd(), 'data', 'expenditure', 'expenditure_transaction_types_aggregates.csv')

        self.__fields = {'parent_identifier': 'parent', 'parent_description': 'name', 'child_identifier': 'id',
                         'child_description': 'segment'}

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __data(self) -> pd.DataFrame:
        """

        :return:
        """

        # The data set of top government divisions/segments
        data = src.functions.streams.Streams().read(uri=self.__uri, usecols=list(self.__fields.keys()))
        data.rename(columns=self.__fields, inplace=True)

        return data

    @staticmethod
    def __collapse(blob: pd.DataFrame) -> pd.DataFrame:
        """

        :param blob:
        :return:
        """

        data = blob.copy()

        # For directed acyclic graph purposes, append a collapsed field.  If a node is collapsed, its
        # children are hidden by default
        data.loc[:, 'collapsed'] = data['id'].apply(lambda x: True if x == 'central' else None)

        return data

    def __persist(self, blob: pd.DataFrame) -> str:
        """

        :param blob:
        :return:
        """

        # Save
        return src.functions.objects.Objects().write(
            nodes=blob.to_dict(orient='tight'), path=os.path.join(self.__storage, 'aggregates.json'))

    def exc(self):
        """

        :return:
        """

        # Data
        data = self.__data()

        # Collapse?
        data = self.__collapse(blob=data)

        # Save
        message = self.__persist(blob=data)
        self.__logger.info(message)
