from decimal import Decimal

from measurement.base import MeasureBase


__all__ = [
    'Weight',
]


class Weight(MeasureBase):
    STANDARD_UNIT = 'g'
    UNITS = {
        'g': Decimal('1.0'),
        'tonne': Decimal('1000000.0'),
        'oz': Decimal('28.3495'),
        'lb': Decimal('453.592'),
        'stone': Decimal('6350.29'),
        'short_ton': Decimal('907185.0'),
        'long_ton': Decimal('1016000.0'),
    }
    ALIAS = {
        'mcg': 'ug',
        'gram': 'g',
        'ton': 'short_ton',
        'metric tonne': 'tonne',
        'metric ton': 'tonne',
        'ounce': 'oz',
        'pound': 'lb',
        'short ton': 'short_ton',
        'long ton': 'long_ton',
    }
    SI_UNITS = ['g']
