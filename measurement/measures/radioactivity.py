from decimal import Decimal

from measurement.base import MeasureBase

__all__ = ["Radioactivity"]


class Radioactivity(MeasureBase):
    """Radioactivity measurements."""

    STANDARD_UNIT = "bq"
    UNITS = {
        "bq": Decimal("1"),
        "ci": Decimal("37000000000"),
        "rd": Decimal("1000000"),
        "dpm": Decimal("1") / Decimal("60"),
    }
    ALIAS = {
        "becquerel": "bq",
        "Bq": "bq",
        "curie": "ci",
        "Ci": "ci",
        "rutherford": "rd",
        "disintegrations per minute": "dpm",
    }
    SI_UNITS = ["bq"]
