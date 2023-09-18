import logging
import os

import pandas as pd

import src.functions.directories
import src.functions.objects
import src.functions.streams


class Classifications:

    def __init__(self, storage: str, uri: str, fields: dict):
        """

        :param storage:
        :param fields:
        """

        self.__storage = storage
        self.__uri = uri
        self.__fields = fields

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

    def __persist(self, blob: pd.DataFrame, name: str) -> str:
        """

        :param blob:
        :param name:
        :return:
        """

        # Save
        return src.functions.objects.Objects().write(
            nodes=blob.to_dict(orient='tight'), path=os.path.join(self.__storage, f'{name}.json'))

