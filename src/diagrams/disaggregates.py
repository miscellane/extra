"""
disaggregates.py
"""
import logging
import os

import pandas as pd

import src.functions.directories
import src.functions.objects
import src.functions.streams


class Disaggregates:
    """
    Disaggregates
    """

    def __init__(self, storage: str):
        """

        :param storage:
        """

        self.__storage = storage

        self.__uri = os.path.join(os.getcwd(), 'data', 'expenditure', 'expenditure_transaction_types_disaggregates.csv')

        self.__fields = {'parent_identifier': 'parent', 'parent_description': 'parent_desc', 'child_identifier': 'id',
                         'child_description': 'child_desc'}

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

        # Renaming fields
        data.rename(columns=self.__fields, inplace=True)

        # Ensuring NaN cells have a <null> value
        condition = data.isna()
        data[condition] = None

        return data

    def __persist(self, blob: pd.DataFrame) -> str:
        """

        :param blob:
        :return:
        """

        # Save
        return src.functions.objects.Objects().write(
            nodes=blob.to_dict(orient='tight'), path=os.path.join(self.__storage, 'disaggregates.json'))

    def exc(self) -> None:
        """

        :return:
        """

        # Data
        data = self.__data()

        # Save
        message = self.__persist(blob=data)
        self.__logger.info(message)