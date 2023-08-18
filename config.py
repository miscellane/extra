import collections
import os

import numpy as np


class Config:

    def __init__(self):

        # gross domestic product (gdp) deflator series
        Deflator = collections.namedtuple(typename='Deflator', field_names=['source', 'base_year', 'rebase_year'])
        self.deflator = Deflator(source=os.path.join(os.getcwd(), 'data', 'gdp_deflator_qna_update_2022.csv'),
                                 base_year=2022, rebase_year=2010)

        # quarterly national accounts (qna)
        Expenditure = collections.namedtuple(typename='Expenditure',
                                             field_names=['source', 'aggregates', 'years', 'destination', 'unavailable'])
        start = 1995
        stop = 2021
        self.expenditure = Expenditure(
            source=os.path.join(os.getcwd(), 'data', 'esa_table_11_central_government.xls'),
            aggregates=['_T', 'GF01', 'GF02', 'GF03', 'GF04', 'GF05', 'GF06', 'GF07', 'GF08', 'GF09', 'GF10'],
            years=np.linspace(start=start, stop=stop, num=stop - start + 1, dtype=int),
            destination=os.path.join(os.getcwd(), 'warehouse', 'expenditure', 'initial'),
            unavailable=['D4.2', 'D4.4', 'D7.2', 'D7.4', 'D9.2', 'D9.4', 'P31', 'P32'])
