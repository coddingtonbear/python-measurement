from measurement.base import MeasureBase


__all__ = [
    'Weight',
]


class Weight(MeasureBase):
    STANDARD_UNIT = 'g'
    UNITS = {
        'mcg': 0.000001,
        'mg': 0.001,
        'g': 1.0,
        'kg': 1000.0,
        'tonne': 1000000.0,
        'oz': 28.3495,
        'lb': 453.592,
        'stone': 6350.29,
        'short_ton': 907185.0,
        'long_ton': 1016000.0,
    }
    ALIAS = {
        'microgram': 'mcg',
        'milligram': 'mg',
        'gram': 'g',
        'kilogram': 'kg',
        'ton': 'short_ton',
        'metric tonne': 'tonne',
        'metric ton': 'tonne',
        'ounce': 'oz',
        'pound': 'lb',
        'short ton': 'short_ton',
        'long ton': 'long_ton',
    }
    LALIAS = dict([(k.lower(), v) for k, v in ALIAS.items()])
