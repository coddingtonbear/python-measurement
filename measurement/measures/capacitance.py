from decimal import Decimal

from measurement.base import MeasureBase

__all__ = ["Capacitance"]


class Capacitance(MeasureBase):
    STANDARD_UNIT = "F"
    UNITS = {"F": Decimal("1.0")}
    ALIAS = {
        "farad": "F",
    }
    SI_UNITS = ["F"]
