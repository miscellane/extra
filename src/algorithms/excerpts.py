import json
import logging
import os

import dask
import dask.dataframe
import pandas as pd

import config
import src.adjust.transactions
import src.functions.directories
import src.functions.streams


class Excerpts:

    def __init__(self):
        """
        Constructor
        """

        # The overarching foci, i.e., segments, e.g., defence, economic affairs, etc.
        self.__segments = src.adjust.transactions.Transactions().segments

        # The calculations must be based on revalued data sets, hence comparable prices/costs across years.
        self.__datapath = config.Config().expenditure.datapath

        # The graphing data will be stored in ...
        self.__storage = os.path.join(os.getcwd(), 'warehouse', 'expenditure', 'graphs', 'excerpts')
        src.functions.directories.Directories().create(self.__storage)

        # The fields in focus: The overall government expenditure per segment code is recorded in field <OTE>
        self.__usecols = ['code', 'description', 'OTE', 'segment_code', 'year']
        self.__rename_aggregates = {'year': 'x', 'OTE': 'y'}

        # logging
        logging.basicConfig(level=logging.INFO, format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __read(self) -> pd.DataFrame:
        """

        :return:
        """

        frame = dask.dataframe.read_csv(
            urlpath=os.path.join(self.__datapath, '*.csv'), usecols=self.__usecols)
        data = frame.compute().reset_index(drop=True)

        return data

    @dask.delayed
    def __persist(self, dictionary: list, segment_code: str) -> str:
        """

        :param dictionary:
        :return:
        """

        try:
            with open(os.path.join(self.__storage, f'{segment_code}.json'), 'w') as disk:
                json.dump(dictionary, disk)
            return f'{segment_code}.json: success'
        except IOError as err:
            raise Exception(err) from err

    def exc(self):
        """

        :return:
        """

        # Read-in the revalued data
        data = self.__read()
        segment_codes = data['segment_code'].unique()

        computations = []
        for segment_code in segment_codes:
            pass
