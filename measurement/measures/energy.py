from decimal import Decimal

from measurement.base import MeasureBase

__all__ = ["Energy"]


class Energy(MeasureBase):
    STANDARD_UNIT = "J"
    UNITS = {
        "c": Decimal("4.18400"),
        "C": Decimal("4184.0"),
        "J": Decimal("1.0"),
        "eV": Decimal("1.602177e-19"),
        "tonne_tnt": Decimal("4184000000"),
    }
    ALIAS = {
        "joule": "J",
        "calorie": "c",
        "Calorie": "C",
    }
    SI_UNITS = ["J", "c", "eV", "tonne_tnt"]
