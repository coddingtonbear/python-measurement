# -*- coding: utf-8 -*-
from decimal import Decimal

from measurement.base import MeasureBase


__all__ = [
    'Radiation',
    'RadiationAbsorbedDose',
    'RadiationExposure',
]


class Radiation(MeasureBase):
    STANDARD_UNIT = 'Bq'
    UNITS = {
        'Bq': Decimal('1'),
        'Ci': Decimal('37000000000'),
        'Rd': Decimal('1000000'),
        'dpm': Decimal('0.0166666666666666666666666667'),
    }
    ALIAS = {
        'becquerel': 'Bq',
        'curie': 'Ci',
        'rutherford': 'Rd',
        'disintegrations per minute': 'dpm', 
    }
    SI_UNITS = ['Bq']

class RadiationAbsorbedDose(MeasureBase):
    STANDARD_UNIT = 'Gy'
    UNITS = {
        'Gy': Decimal('1'),
        'rad': Decimal('0.010'),
    }
    ALIAS = {
        'gray': 'Gy',
        'rad': 'rad',
    }
    SI_UNITS = ['Gy']
    
class RadiationExposure(MeasureBase):
    STANDARD_UNIT = 'C_kg'
    UNITS = {
        'C_kg': Decimal('1'),
        'R': Decimal('0.000258'),
    }
    
    ALIAS = {
        'coulomb per kilogram': 'C_kg',
        'roentgen': 'R',
    }
    
    SI_UNITS = ['C_kg']    