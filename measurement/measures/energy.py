from measurement.base import MeasureBase


__all__ = [
    'Energy'
]


class Energy(MeasureBase):
    STANDARD_UNIT = 'J'
    UNITS = {
        'c': 4.18400,
        'C': 4184.0,
        'J': 1.0,
    }
    ALIAS = {
        'joule': 'J',
        'calorie': 'c',
        'Calorie': 'C',
    }
    SI_UNITS = ['J', 'c']
