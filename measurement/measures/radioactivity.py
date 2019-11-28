# -*- coding: utf-8 -*-

from measurement.base import MeasureBase


__all__ = [
    'Radioactivity'
]


class Radioactivity(MeasureBase):
    """Radioactivity measurements."""

    STANDARD_UNIT = 'bq'
    UNITS = {
        'bq': 1,
        'ci': 37000000000,
        'rd': 1000000,
        'dpm': 0.0166666666666666666666666667,
    }
    ALIAS = {
        'becquerel': 'bq',
        'Bq': 'bq',
        'curie': 'ci',
        'Ci': 'ci',
        'rutherford': 'rd',
        'disintegrations per minute': 'dpm', 
    }
    SI_UNITS = ['bq']
