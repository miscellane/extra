import logging
import os

import dask.dataframe
import pandas as pd

import config


class Overall:
    """
    Overall
    """

    def __init__(self):
        """
        Constructor
        """

        # The overall government expenditure per segment code is recorded in field <OTE> 
        self.__usecols = ['code', 'OTE', 'segment', 'year']

        # The path to the data sets
        self.__datapath = config.Config().expenditure.datapath

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

    def exc(self):
        """

        :return:
        """

        data = self.__read()
        self.__logger.info(data)

        tallies = data.groupby(by=['segment', 'year']).agg(total=('OTE', sum))
        self.__logger.info(tallies)
