import glob
import logging
import os
import config


class Summaries:

    def __init__(self):

        self.__datasets = config.Config().expenditure.datasets

        # ['code', 'OTE', 'segment']
        # .loc[:, 'year'] =

        # logging
        logging.basicConfig(level=logging.INFO, format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self):

        list_of_documents = glob.glob(pathname=os.path.join(self.__datasets, '*.csv'))
        self.__logger.info(list_of_documents)
