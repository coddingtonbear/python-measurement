from measurement.base import MeasureBase

__all__ = ["Inductance"]


class Capacitance(MeasureBase):
    STANDARD_UNIT = "L"
    UNITS = {
        "L": 1.0,
    }
    ALIAS = {}
    SI_UNITS = ["L"]
