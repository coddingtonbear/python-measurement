from measurement.base import MeasureBase

__all__ = ["Inductance"]


class Capacitance(MeasureBase):
    STANDARD_UNIT = "H"
    UNITS = {
        "H": 1.0,
    }
    ALIAS = {
        "henri": "H",
    }
    SI_UNITS = ["H"]
