from measurement.base import AbstractMeasure, MetricUnit

__all__ = [
    "Capacitance",
    "Current",
    "ElectricPower",
    "Inductance",
    "Resistance",
    "Voltage",
]


class Capacitance(AbstractMeasure):
    farad = MetricUnit("1", ["F", "Farad"], ["F"], ["farad"])


class Current(AbstractMeasure):
    ampere = MetricUnit("1", ["A", "amp", "Ampere"], ["A"], ["ampere", "amp"])

    def __mul__(self, other):
        if isinstance(other, Voltage):
            return ElectricPower(self.si_value * other.si_value, "W")
        return super().__mul__(other)


class Resistance(AbstractMeasure):
    ohm = MetricUnit("1", ["Ohm", "Ω"], ["Ω"], ["ohm"])


class Voltage(AbstractMeasure):
    volt = MetricUnit("1", ["V", "Volt"], ["V"], ["volt"])

    def __mul__(self, other):
        if isinstance(other, Current):
            return ElectricPower(self.si_value * other.si_value, "W")
        return super().__mul__(other)


class Inductance(AbstractMeasure):
    henry = MetricUnit("1", ["H", "Henry"], ["H"], ["henry"])


class ElectricPower(AbstractMeasure):
    """
    Electric power can is defined as :class:`Voltage` multiplied by :class:`Current`.

    This is why you can devided :class:`Current` to get the :class:`Voltage`
    by :class:`Voltage` to get the :class:`Current`
    or by :class:`Current` to get the :class:`Voltage`:

        >>> from measurement import measures
        >>> measures.ElectricPower('24 W') / measures.Voltage('12 V')
        Current(ampere="2")
        >>> measures.ElectricPower('24 W') / measures.Current('4 A')
        Voltage(volt="6")


    Analog to this, you can also multiply both :class:`Current`
    and :class:`Voltage` to get :class:`Current` to get the :class:`Voltage`:

        >>> from measurement import measures
        >>> measures.Current('2 A') * measures.Voltage('12 V')
        ElectricPower(watt="24")

    """

    watt = MetricUnit(
        "1", ["W", "VA", "Watt", "Voltampere"], ["W", "VA"], ["watt", "voltampere"]
    )

    def __truediv__(self, other):
        if isinstance(other, Current):
            return Voltage(volt=self.si_value / other.si_value)

        if isinstance(other, Voltage):
            return Current(ampere=self.si_value / other.si_value)

        return super().__truediv__(other)
