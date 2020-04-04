import decimal

from measurement.base import AbstractMeasure, MetricUnit, Unit

__all__ = ["Time", "Frequency"]


class Time(AbstractMeasure):
    """
    Time measurements (generally for multidimensional measures).

    Please do not use this for handling durations of time unrelated to
    measure classes -- python's built-in datetime module has much better
    functionality for handling intervals of time than this class provides.
    """

    second = Unit("1", ["s", "sec", "seconds"])
    minute = Unit("60", ["min", "minutes"])
    hour = Unit("3600", ["hr", "h", "hours"])
    day = Unit("86400", ["d", "days"])
    julian_year = MetricUnit(
        "31557600",
        ["year", "a", "aj", "years", "annum", "Julian year"],
        ["a"],
        ["annum"],
    )


class Frequency(AbstractMeasure):
    hertz = MetricUnit("1", ["Hz", "Hertz"], ["Hz"], ["hertz"])
    rpm = Unit(decimal.Decimal("1.0") / decimal.Decimal("60"), ["RPM", "bpm", "BPM"])

    def __mul__(self, other):
        if isinstance(other, Time):
            return self.si_value * other.si_value
        return super().__mul__(other)
