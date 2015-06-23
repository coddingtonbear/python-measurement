from decimal import Decimal

from measurement.base import MeasureBase


__all__ = [
    'Time',
]


class Time(MeasureBase):
    """ Time measurements (generally for multidimensional measures).

    Please do not use this for handling durations of time unrelated to
    measure classes -- python's built-in datetime module has much better
    functionality for handling intervals of time than this class provides.

    """
    STANDARD_UNIT = 'sec'
    UNITS = {
        'sec': Decimal('1.0'),
        'min': Decimal('60.0'),
        'hr': Decimal('3600.0'),
        'day': Decimal('86400.0')
    }
    ALIAS = {
        'second': 'sec',
        'minute': 'min',
        'hour': 'hr',
        'day': 'day'
    }
    SI_UNITS = ['sec']
