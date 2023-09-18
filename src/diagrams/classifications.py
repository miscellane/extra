import logging
import os

import pandas as pd

import src.functions.directories
import src.functions.objects
import src.functions.streams


class Classifications:

    def __init__(self, storage: str):
        """

        :param storage:
        """

        # Storage
        self.__storage = storage

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    @staticmethod
    def __data(uri: str, fields: dict) -> pd.DataFrame:
        """

        :return:
        """

        # The data set of top government divisions/segments
        data = src.functions.streams.Streams().read(uri=uri, usecols=list(fields.keys()))

        # Renaming fields
        data.rename(columns=fields, inplace=True)

        # Ensuring NaN cells have a <null> value
        condition = data.isna()
        data[condition] = None

        return data

    def __persist(self, blob: pd.DataFrame, name: str) -> str:
        """

        :param blob:
        :param name:
        :return:
        """

        # Save
        return src.functions.objects.Objects().write(
            nodes=blob.to_dict(orient='tight'), path=os.path.join(self.__storage, f'{name}.json'))

    def exc(self, uri: str, fields: dict, name: str):
        """

        :param uri:
        :param fields:
        :param name:
        :return:
        """

        # Data
        data = self.__data(uri=uri, fields=fields)

        # Save
        message = self.__persist(blob=data, name=name)
        self.__logger.info(message)
