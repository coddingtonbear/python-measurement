# -*- coding: utf-8 -*-
from measurement.base import MeasureBase


__all__ = [
    'Resistance'
]


class Resistance(MeasureBase):
    STANDARD_UNIT = 'Ω'
    UNITS = {
        'Ω': 1.0,
    }
    ALIAS = {
        'ohm': 'Ω',
    }
    SI_UNITS = ['Ω']
