import collections
import logging
import os
import pandas as pd
import numpy as np


class Expenditure:

    def __init__(self):

        self.uri = os.path.join(os.getcwd(), 'data', 'esatable11centralgovernment.xls')

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

    def __code(self, blob: pd.DataFrame):

        data = blob.copy()

        doublet = data['Transaction'].str.split(pat='-', n=1, expand=True)
        doublet = doublet.copy().set_axis(['code', 'description'], axis=1)
        self.__logger.info(doublet)

        data = doublet.join(data.drop(columns=['Transaction']))
        self.__logger.info(data.head())

    def exc(self, year) -> pd.DataFrame:

        data = self.__dataset(sheet_name=str(year))
        self.__code(blob=data)

        return data
