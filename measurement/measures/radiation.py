# -*- coding: utf-8 -*-
from decimal import Decimal

from measurement.base import MeasureBase


__all__ = [
    'Radiation'
]


class Radiation(MeasureBase):
    STANDARD_UNIT = 'bq'
    UNITS = {
        'bq': Decimal('1'),
        'ci': Decimal('37000000000'),
        'rd': Decimal('1000000'),
        'dpm': Decimal('0.0166666666666666666666666667'),
    }
    ALIAS = {
        'becquerel': 'bq',
        'curie': 'ci',
        'rutherford': 'rd',
        'disintegrations per minute': 'dpm', 
    }
    SI_UNITS = ['bq']

