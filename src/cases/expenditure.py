import collections
import logging
import datetime

import numpy as np
import pandas as pd

import config


class Expenditure:

    def __init__(self):

        # The raw expenditure data file
        self.uri = config.Config().expenditure.source

        # Exclude these expenditure transaction labels because they are aggregates of other labels
        self.__aggregates = config.Config().expenditure.aggregates

        # data sheets
        Data = collections.namedtuple(typename='Data', field_names=['cells', 'start', 'end'])
        self.data = Data._make(('A:AG', 6, 86))

        # logging
        logging.basicConfig(level=logging.INFO, format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __dataset(self, sheet_name: str) -> pd.DataFrame:
        """

        :return:
        """

        # Note: The header value is relative to a specified data matrix
        try:
            return pd.read_excel(io=self.uri, sheet_name=sheet_name, header=0,
                                 skiprows=np.arange(self.data.start - 1), usecols=self.data.cells,
                                 nrows=(self.data.end - self.data.start + 1))
        except OSError as err:
            raise Exception(err.strerror) from err

    @staticmethod
    def __code(blob: pd.DataFrame) -> pd.DataFrame:
        """
        Deduces the transaction code of each record/row

        :param blob: An expenditure data set
        :return:
        """

        data = blob.copy()

        # Each <Transaction> field value is a combination of transaction code & transaction description,
        # separated by a dash
        doublet = data['Transaction'].str.split(pat='-', n=1, expand=True)
        doublet = doublet.copy().set_axis(['code', 'description'], axis=1)
        doublet.loc[:, 'code'] = doublet['code'].str.strip()

        # Instead of the transaction column, code & description columns
        data = doublet.join(data.drop(columns=['Transaction']))

        return data

    def __filter(self, blob: pd.DataFrame) -> pd.DataFrame:
        """

        :param blob: An expenditure data set
        :return:
        """

        # Excluding records that are aggregates of other records
        data = blob.copy()
        data = data.copy().loc[~data['code'].isin(self.__aggregates), :]

        return data

    @staticmethod
    def __segment(blob: pd.DataFrame) -> pd.DataFrame:
        """
        The first four characters of a transaction code denote an overarching transaction
        segment, e.g., defence, economic affairs, environmental protection, etc.

        :param blob:
        :return:
        """

        data = blob.copy()
        data.loc[:, 'segment_code'] = data['code'].str.slice(stop=4)

        return data

    def exc(self, year: int) -> pd.DataFrame:
        """

        :param year:
        :return:
        """

        # steps
        data = self.__dataset(sheet_name=str(year))
        data = self.__code(blob=data)
        data = self.__filter(blob=data)
        data = self.__segment(blob=data)

        # year
        data.loc[:, 'year'] = year

        # ... milliseconds since 1970-01-01
        # seconds -> datetime.datetime.strptime('2020', '%Y').timestamp()
        data.loc[:, 'epoch'] = 1000 * datetime.datetime.strptime(str(year), '%Y').timestamp()

        return data
