# -*- coding: utf-8 -*-
from decimal import Decimal

from measurement.base import MeasureBase


__all__ = [
    'Pressure'
]


class Pressure(MeasureBase):
    STANDARD_UNIT = 'pa'
    UNITS = {
        'pa': Decimal('1.0'),
        'bar': Decimal('100000'),
        'at': Decimal('98066.5'),
        'atm': Decimal('101325'),
        'torr': Decimal('133.322'),
        'psi': Decimal('6894.757293168'),
    }
    ALIAS = {
        'pascal': 'pa',
        'bar': 'bar',
        'technical atmosphere': 'at',
        'atmosphere': 'atm',
        'torr': 'torr',
        'pounds per square inch': 'psi' 
    }
    SI_UNITS = ['pa']
