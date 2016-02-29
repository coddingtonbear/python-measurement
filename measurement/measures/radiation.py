# -*- coding: utf-8 -*-
from decimal import Decimal

from measurement.base import MeasureBase


__all__ = [
    'Radiation'
]


class Radiation(MeasureBase):
    STANDARD_UNIT = 'Bq'
    UNITS = {
        'Bq': Decimal('1'),
        'Ci': Decimal('37000000000'),
        'Rd': Decimal('1000000'),
        'dpm': Decimal('0.0166666666666666666666666667'),
    }
    ALIAS = {
        'becquerel': 'Bq',
        'curie': 'Ci',
        'rutherford': 'Rd',
        'disintegrations per minute': 'dpm', 
    }
    SI_UNITS = ['Bq']

