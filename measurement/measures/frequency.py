from decimal import Decimal

from measurement.base import MeasureBase


__all__ = [
    'Frequency'
]


class Frequency(MeasureBase):
    STANDARD_UNIT = 'Hz'
    UNITS = {
        'Hz': Decimal('1.0'),
    }
    ALIAS = {
        'hertz': 'Hz',
    }
    SI_UNITS = ['Hz']
