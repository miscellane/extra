import collections
import os

import numpy as np


class Config:

    def __init__(self):

        Expenditure = collections.namedtuple(typename='Expenditure', field_names=['exclude', 'years', 'datapath'])
        start = 1995
        stop = 2021
        self.expenditure = Expenditure(
            exclude=['_T', 'GF01', 'GF02', 'GF03', 'GF04', 'GF05', 'GF06', 'GF07', 'GF08', 'GF09', 'GF10'],
            years=np.linspace(start=start, stop=stop, num=stop - start + 1, dtype=int),
            datapath=os.path.join(os.getcwd(), 'warehouse', 'expenditure', 'initial'))
