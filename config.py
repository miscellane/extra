import collections
import os

import numpy as np


class Config:

    def __init__(self):

        # gross domestic product (gdp) deflator series
        self.deflator_rebase_year = 2010
        self.deflator_base_year = 2022
        self.deflator_file = os.path.join(os.getcwd(), 'data', 'gdp_deflator_qna_update_2022.csv')

        # quarterly national accounts (qna)
        Expenditure = collections.namedtuple(typename='Expenditure',
                                             field_names=['source', 'exclude', 'years', 'datapath'])
        start = 1995
        stop = 2021
        self.expenditure = Expenditure(
            source=os.path.join(os.getcwd(), 'data', 'esa_table_11_central_government.xls'),
            exclude=['_T', 'GF01', 'GF02', 'GF03', 'GF04', 'GF05', 'GF06', 'GF07', 'GF08', 'GF09', 'GF10'],
            years=np.linspace(start=start, stop=stop, num=stop - start + 1, dtype=int),
            datapath=os.path.join(os.getcwd(), 'warehouse', 'expenditure', 'initial'))
