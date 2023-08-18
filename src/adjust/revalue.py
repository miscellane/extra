import pandas as pd
import numpy as np

import config
import glob
import os
import src.adjust.rebase
import src.adjust.variables
import src.functions.streams


class Revalue:

    def __init__(self):

        # The rebase values, and variables, for revaluation
        self.__rebase: pd.DataFrame = src.adjust.rebase.Rebase().data
        self.__variables = src.adjust.variables.Variables().data

        # Expenditure metadata
        self.__expenditure = config.Config().expenditure

        # Instances
        self.__streams = src.functions.streams.Streams()

    def __read(self, path) -> pd.DataFrame:

        return self.__streams.read(uri=path, header=0)

    def __streamline(self, blob: pd.DataFrame):

        difference = np.setdiff1d(blob.columns.to_numpy(), self.__variables['variable'].to_numpy())
        print(difference)

    def __revalue(self):
        pass

    def exc(self):

        paths = glob.glob(pathname=os.path.join(self.__expenditure.destination, '*.csv'))

        for path in paths[:8]:

            data = self.__read(path=path)
            self.__streamline(blob=data)
