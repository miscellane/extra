import collections

import numpy as np


class Config:

    def __init__(self):
        
        Expenditure = collections.namedtuple(typename='Expenditure', field_names=['exclude', 'years'])
        start = 1996
        stop = 2021
        self.expenditure = Expenditure(
            exclude=['_T', 'GF01', 'GF02', 'GF03', 'GF04', 'GF05', 'GF06', 'GF07', 'GF08', 'GF09', 'GF10'],
            years=np.linspace(start=start, stop=stop, num=stop - start + 1))
