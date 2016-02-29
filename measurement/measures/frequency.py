from decimal import Decimal

from measurement.base import MeasureBase


__all__ = [
    'Frequency'
]


class Frequency(MeasureBase):
    STANDARD_UNIT = 'Hz'
    UNITS = {
        'Hz': Decimal('1.0'),
        'rpm': Decimal('1.0') / Decimal('60'),
    }
    ALIAS = {
        'hertz': 'Hz',
    }
    SI_UNITS = ['Hz']
