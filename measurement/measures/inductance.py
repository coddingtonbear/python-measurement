from measurement.base import MeasureBase

__all__ = ["Inductance"]


class Inductance(MeasureBase):
    STANDARD_UNIT = "H"
    UNITS = {
        "H": 1.0,
    }
    ALIAS = {
        "henry": "H",
    }
    SI_UNITS = ["H"]
