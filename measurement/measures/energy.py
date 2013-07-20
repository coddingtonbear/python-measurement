from measurement.base import MeasureBase


__all__ = [
    'Energy'
]


class Energy(MeasureBase):
    STANDARD_UNIT = 'J'
    UNITS = {
        'c': 4.1400,
        'J': 1.0,
    }
    ALIAS = {
        'joule': 'j'
    }
