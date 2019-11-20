from measurement.base import BidimensionalMeasure
from measurement.measures.time import Time
from measurement.measures.volume import Volume


__all__ = [
    'VolumetricFlow'
]


class VolumetricFlow(BidimensionalMeasure):
    """Volumetric Flow measurements (generally for water flow)."""

    PRIMARY_DIMENSION = Volume
    REFERENCE_DIMENSION = Time

    ALIAS = {
        'cfs': 'cubic_foot__s',
        'cubic feet per second': 'cubic_foot__s',
        'cubic feet per minute': 'cubic_foot__min',
        'cubic feet per hour': 'cubic_foot__hr',
        'cubic feet per day': 'cubic_foot__day',
        'cubic yards per second': 'cubic_yard__s',
        'cubic yards per minute': 'cubic_yard__min',
        'cubic yards per hour': 'cubic_yard__hr',
        'cubic yards per day': 'cubic_yard__day',
        'gps': 'us_g__s',
        'gpm': 'us_g__min',
        'gph': 'us_g__hr',
        'gpd': 'us_g__day',
        'cms': 'cubic_meter__s',
        'cumecs': 'cubic_meter__s',
        'million gallons per hour': 'mil_us_g__hr',
        'million gallons per day': 'mil_us_g__day',
        'acre-inches per hour': 'acre_in__hr',
        'acre-inches per day': 'acre_in__day',
        'acre-feet per hour': 'acre_ft__hr',
        'acre-feet per day': 'acre_ft__day',
    }
