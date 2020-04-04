import dataclasses
import decimal
from typing import List

from ..base import AbstractMeasure, AbstractUnit, MetricUnit

__all__ = ["Temperature"]


@dataclasses.dataclass
class DegreeUnit(AbstractUnit):
    symbols: List[str] = dataclasses.field(default_factory=list)
    """Symbols used to describe this unit."""

    def get_symbols(self):
        yield self.name.replace("_", " "), type(self)()
        yield from ((name, type(self)()) for name in self.symbols)


class DegreeCelcius(DegreeUnit):
    def to_si(self, value):
        return value + decimal.Decimal("273.15")

    def from_si(self, value):
        return value - decimal.Decimal("273.15")


class DegreeFahrenheit(DegreeUnit):
    def to_si(self, value):
        celsius = (value - 32) * 5 / 9
        return celsius + decimal.Decimal("273.15")

    def from_si(self, value):
        celsius = value - decimal.Decimal("273.15")
        return celsius * 9 / 5 + 32


class Temperature(AbstractMeasure):
    kelvin = MetricUnit("1", ["K", "Kelvin"], ["K"], ["kelvin"])
    celsius = DegreeCelcius(["°C"])
    fahrenheit = DegreeFahrenheit(["°F"])
