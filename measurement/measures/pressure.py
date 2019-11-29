from measurement.base import MeasureBase


__all__ = [
    'Pressure'
]


class Pressure(MeasureBase):
    """Pressure measurements."""

    STANDARD_UNIT = 'pa'
    UNITS = {
        'pa': 1.0,
        'bar': 100000,
        'at': 98066.5,
        'atm': 101325,
        'torr': 133.322,
        'psi': 6894.757293168,
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
