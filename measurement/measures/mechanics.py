import decimal
from typing import Optional, Union

from measurement.base import AbstractMeasure, MeasureBase, MetricUnit, Unit

from .geometry import Distance, Volume
from .time import Time

__all__ = ["Mass", "Pressure", "VolumetricFlowRate", "Speed"]


class FractionMeasureBase(MeasureBase):
    def __new__(mcs, name, bases, attrs):
        mcs.freeze_org_units(attrs)
        numerator = attrs["__numerator__"]
        denominator = attrs["__denominator__"]
        attrs.update(mcs.div(numerator, denominator))

        cls = super().__new__(mcs, name, bases, attrs)
        return cls

    @staticmethod
    def div(numerator, denominator):
        for numerator_name, numerator_unit in numerator._units.items():
            for (
                denominator_name,
                denominator_unit,
            ) in denominator._units.items():
                name = f"{numerator_name}/{denominator_name}"
                factor = numerator_unit.factor / denominator_unit.factor
                unit = Unit(factor=factor)
                unit.name = name
                yield name, unit


class VolumetricFlowRate(AbstractMeasure, metaclass=FractionMeasureBase):
    """Volumetric Flow measurements (generally for water flow)."""

    def __init__(
        self,
        value: Union[str, decimal.Decimal, int, None] = None,
        unit: Optional[str] = None,
        **kwargs: Union[str, decimal.Decimal, int, None],
    ):
        # Maually setting the base unit, because the process of iterating through
        # all combinations for square/cubic/fractional measures is intense
        self.base_unit_names = [
            "cms",
            "cumecs",
            "CMS",
            "kL/second",
            "kL/s",
            "kL/sec",
            "kL/seconds",
            "kl/second",
            "kl/s",
            "kl/sec",
            "kl/seconds",
            "kℓ/second",
            "kℓ/s",
            "kℓ/sec",
            "kℓ/seconds",
            "kilolitre/second",
            "kilolitre/s",
            "kilolitre/sec",
            "kilolitre/seconds",
            "kiloliter/second",
            "kiloliter/s",
            "kiloliter/sec",
            "kiloliter/seconds",
            "Kilolitre/second",
            "Kilolitre/s",
            "Kilolitre/sec",
            "Kilolitre/seconds",
            "Kiloliter/second",
            "Kiloliter/s",
            "Kiloliter/sec",
            "Kiloliter/seconds",
            "metre³/second",
            "metre³/s",
            "metre³/sec",
            "metre³/seconds",
            "m³/second",
            "m³/s",
            "m³/sec",
            "m³/seconds",
            "meter³/second",
            "meter³/s",
            "meter³/sec",
            "meter³/seconds",
            "Meter³/second",
            "Meter³/s",
            "Meter³/sec",
            "Meter³/seconds",
            "Metre³/second",
            "Metre³/s",
            "Metre³/sec",
            "Metre³/seconds",
        ]

        return super().__init__(value, unit, **kwargs)

    __numerator__ = Volume
    __denominator__ = Time

    cms = Unit("1", ["cumecs", "CMS"])
    cfs = Unit(1 / decimal.Decimal("35.31466672148859025043801035"), ["CFS"])

    miners_inch_50 = Unit("566.33693184e-6", ["mi_50"])
    miners_inch_40 = Unit("707.9211648e-6", ["mi_40"])
    miners_inch_38_4 = Unit("737.41788e-6", ["mi_38_4"])

    @classmethod
    def _attr_to_unit(cls, name):
        return super()._attr_to_unit(name.replace("__", "/"))


class Speed(AbstractMeasure, metaclass=FractionMeasureBase):
    def __init__(
        self,
        value: Union[str, decimal.Decimal, int, None] = None,
        unit: Optional[str] = None,
        **kwargs: Union[str, decimal.Decimal, int, None],
    ):
        # Maually setting the base unit, because the process of iterating through
        # all combinations for square/cubic/fractional measures is intense
        self.base_unit_names = [
            "metre/second",
            "metre/s",
            "metre/sec",
            "metre/seconds",
            "m/second",
            "m/s",
            "m/sec",
            "m/seconds",
            "meter/second",
            "meter/s",
            "meter/sec",
            "meter/seconds",
            "Meter/second",
            "Meter/s",
            "Meter/sec",
            "Meter/seconds",
            "Metre/second",
            "Metre/s",
            "Metre/sec",
            "Metre/seconds",
        ]

        return super().__init__(value, unit, **kwargs)

    __numerator__ = Distance
    __denominator__ = Time

    mph = Unit("0.44704")
    kph = Unit(1 / decimal.Decimal("3.6"))

    @classmethod
    def _attr_to_unit(cls, name):
        return super()._attr_to_unit(name.replace("__", "/"))


class Mass(AbstractMeasure):
    gram = MetricUnit("1", ["g", "Gram"], ["g"], ["gram"])
    tonne = Unit("1000000", ["t", "metric ton", "metric tonne"])
    ounce = Unit("28.34952", ["oz"])
    pound = Unit("453.59237", ["lb"])
    stone = Unit("6350.293")
    short_ton = Unit("907185.0", ["ton"])
    long_ton = Unit("1016000.0")


class Pressure(AbstractMeasure):
    pascal = MetricUnit("1", ["pa"], ["pa"], ["pascal"])
    bar = Unit("100000")
    atmosphere = Unit("101325", ["atm"])
    technical_atmosphere = Unit("98066.5", ["at"])
    torr = Unit("133.322")
    psi = Unit("6894.757293168", ["pounds per square inch"])
