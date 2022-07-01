from measurement.base import AbstractMeasure, MetricUnit, Unit

__all__ = ["Energy", "Heat"]


class Energy(AbstractMeasure):
    joule = MetricUnit("1", ["J", "Joule"], ["J"], ["joule"])
    calorie = MetricUnit(
        "4184.0", ["c", "cal", "Cal", "Calorie", "C"], ["cal"], ["calorie"]
    )
    electronvolt = MetricUnit(
        "1.602177e-19",
        ["eV", "electron-volt", "electron volt"],
        ["eV"],
        ["electronvolt"],
    )
    tonne_tnt = Unit("4184000000")
    
    watthour = MetricUnit(
        "3600",
        ["wh", "watthour", "watt-hour"],
        ["wh"],
        ["watthour"],
    )
    

Heat = Energy

class Power(AbstractMeasure, metaclass=FractionMeasureBase):
    __numerator__ = Energy
    __denominator__ = Time

    watt = MetricUnit("1", ["W", "w", "Watt"], ["W"], ["Watt"])
    

    @classmethod
    def _attr_to_unit(cls, name):
        return super()._attr_to_unit(name.replace("__", "/"))

