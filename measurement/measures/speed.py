from measurement.base import BidimensionalMeasure


from measurement.measures.distance import Distance
from measurement.measures.time import Time


__all__ = [
    'Speed'
]


class Speed(BidimensionalMeasure):
    PRIMARY_DIMENSION = Distance
    REFERENCE_DIMENSION = Time

    ALIASES = {
        'mph': 'mile__hour',
        'kph': 'kilometer__hour',
    }
