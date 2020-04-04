import decimal

from measurement.base import AbstractMeasure, MeasureBase, MetricUnit, Unit

__all__ = ["Distance", "Area", "Volume"]


class Distance(AbstractMeasure):
    """
    A distance the factor for both :class:`Area` and :class:`Volume`.

    If you multiply a :class:`Distance` with another :class:`Distance`,
    you will get an :class:`Area`:

        >>> from measurement import measures
        >>> measures.Distance('2 m') * measures.Distance('3 m')
        Area(metre²="6")

    If you multiply a :class:`Distance` with an :class:`Area` or two
    :class:`Distances<Distance>`, you will get an :class:`Volume`:

        >>> from measurement import measures
        >>> measures.Distance('2 m') * measures.Area('6 m²')
        Volume(metre³="12")

    You can also build the second and thrid power of a :class:`Distance`,
    to get an :class:`Area` or :class:`Volume`.

        >>> from measurement import measures
        >>> measures.Distance('2 m') ** 2
        Area(metre²="4")
        >>> measures.Distance('2 m') ** 3
        Volume(metre³="8")

    """

    metre = MetricUnit("1", ["m", "meter", "Meter", "Metre"], ["m"], ["metre", "meter"])
    parsec = MetricUnit("3.0857E+16", ["Parsec", "pc"], ["pc"], ["parsec"])
    astronomical_unit = MetricUnit(
        "1.495978707E+11", ["au", "ua", "AU"], ["au", "ua", "AU"]
    )
    foot = Unit("0.3048", ["ft", "feet", "Foot (International)"])
    inch = Unit("0.0254", ["in", "inches"])
    mile = Unit("1609.344", ["mi"])
    chain = Unit("20.1168")
    chain_benoit = Unit("20.116782", ["Chain (Benoit)"])
    chain_sears = Unit("20.1167645", ["Chain (Sears)"])
    british_chain_benoit = Unit("20.1167824944", ["British chain (Benoit 1895 B)"])
    british_chain_sears = Unit("20.1167651216", ["British chain (Sears 1922)"])
    british_chain_sears_truncated = Unit(
        "20.116756", ["British chain (Sears 1922 truncated)"]
    )
    british_foot = Unit(
        "0.304799471539", ["british_ft", "British foot", "British foot (Sears 1922)"]
    )
    british_yard = Unit(
        "0.914398414616", ["british_yd", "British yard", "British yard (Sears 1922)"]
    )
    clarke_ft = Unit("0.3047972654", ["Clarke's Foot"])
    clarke_link = Unit("0.201166195164", ["Clarke's link"])
    fathom = Unit("1.8288")
    german_meter = Unit("1.0000135965", ["german_m", "German legal metre"])
    gold_coast_foot = Unit("0.304799710181508", ["gold_coast_ft", "Gold Coast foot"])
    indian_yard = Unit("0.914398530744", ["indian_yd", "Indian yard", "Yard (Indian)"])
    link = Unit("0.201168", ["Link"])
    link_benoit = Unit("0.20116782", ["Link (Benoit)"])
    link_sears = Unit("0.20116765", ["Link (Sears)"])
    nautical_mile = Unit("1852", ["Nautical Mile", "NM", "nmi"])
    nautical_mile_uk = Unit("1853.184", ["nm_uk", "Nautical Mile (UK)"])
    rod = Unit("5.0292")
    sears_yard = Unit("0.91439841", ["sears_yd", "Yard (Sears"])
    survey_foot = Unit("0.304800609601", ["survey_ft", "US survey foot", "U.S. Foot"])
    yard = Unit("0.9144", ["yd"])

    def __mul__(self, other):
        if isinstance(other, Distance):
            return Area(sq_metre=self.si_value * other.si_value)

        if isinstance(other, Area):
            return Volume(cubic_metre=self.si_value * other.si_value)

        return super().__mul__(other)

    def __pow__(self, power, modulo=None):
        if power == 2:
            return self * self
        if power == 3:
            return self * self * self
        return NotImplemented


class AreaBase(MeasureBase):
    def __new__(mcs, name, bases, attrs):
        mcs.freeze_org_units(attrs)
        x, y = attrs["__factors__"]
        if x is y:
            attrs.update(mcs.square(x))

        cls = super().__new__(mcs, name, bases, attrs)
        return cls

    @staticmethod
    def square(klass):
        for name, unit in klass._units.items():
            qs_unit = Unit(factor=unit.factor ** 2)
            qs_unit.name = f"{qs_unit.name}²"
            yield f"{name}²", qs_unit


class Area(AbstractMeasure, metaclass=AreaBase):
    """
    An area is defined as :class:`Distance` multipled by :class:`Distance`.

    This is why you can multiple two :class:`Distances<Distance>` to get
    an :class:`Area` or devide an :class:`Area` to get a :class:`Distance`:

        >>> from measurement import measures
        >>> measures.Distance('2 m') * measures.Distance('3 m')
        Area(metre²="6")
        >>> measures.Area('6 m²') / measures.Distance('2 m')
        Distance(metre="3")

    If if multiple an :class:`Area` with a :class:`Distance`,
    you will get a :class:`Volume`:

        >>> measures.Area('6 m²') * measures.Distance('2 m')
        Volume(metre³="12")

    """

    __factors__ = (Distance, Distance)

    acre = Unit(
        (decimal.Decimal("43560") * (Distance(ft=decimal.Decimal(1)).m ** 2)), ["Acre"],
    )
    hectare = Unit("10000", ["Hectare", "ha"])

    @classmethod
    def _attr_to_unit(cls, name):
        if name[:3] == "sq_":
            name = f"{name[3:]}²"
        return super()._attr_to_unit(name)

    def __truediv__(self, other):
        if isinstance(other, Distance):
            return Distance(metre=self.si_value / other.si_value)

        return super().__truediv__(other)

    def __mul__(self, other):
        if isinstance(other, Distance):
            return Volume(cubic_metre=self.si_value * other.si_value)

        return super().__mul__(other)


class VolumeBase(MeasureBase):
    def __new__(mcs, name, bases, attrs):
        mcs.freeze_org_units(attrs)
        if "__factors__" in attrs:
            x, y, z = attrs["__factors__"]
            attrs.update(mcs.cubic(x))
        cls = super().__new__(mcs, name, bases, attrs)
        return cls

    @staticmethod
    def cubic(klass):
        for name, unit in klass._units.items():
            qs_unit = Unit(factor=unit.factor ** 3)
            qs_unit.name = f"{qs_unit.name}³"
            yield f"{name}³", qs_unit


class Volume(AbstractMeasure, metaclass=VolumeBase):
    """
    A volume is defined as :class:`Area` multipled by :class:`Distance`.

    This is why you can multiple three :class:`Distances<Distance>` to get
    a :class:`Volume`, multiple an :class:`Area` by a :class:`Distance`
    or devide a :class:`Volume` by both :class:`Distance` and :class:`Area`:

        >>> from measurement import measures
        >>> measures.Distance('2 m') * measures.Distance('3 m') * measures.Distance('4 m')
        Volume(metre³="24")
        >>> measures.Distance('2 m') * measures.Area('6 m²')
        Volume(metre³="12")
        >>> measures.Volume('12 m³') / measures.Area('6 m²')
        Distance(metre="2")
        >>> measures.Volume('12 m³') / measures.Distance('6 m')
        Area(metre²="2")

    """

    __factors__ = (Distance, Distance, Distance)

    litre = MetricUnit(
        "1e-3", ["liter", "L", "l", "ℓ"], ["L", "l", "ℓ"], ["litre", "liter"]
    )

    us_gallon = Unit(
        "3.785411784e-3", ["US gallon", "US gal", "US fluid gallon", "gallon (US)"]
    )
    us_fluid_ounce = Unit("29.57353e-6", ["US oz", "US fl oz"])
    us_fluid_ounce_food = Unit("30e-6", ["US fluid ounce (food nutrition labelling)"])
    us_liquid_quart = Unit("0.946352946e-3", ["US liquid quart"])
    us_liquid_pint = Unit("473.176473e-6")
    us_gill = Unit("118.29411825e-6")
    us_tablespoon = Unit("14.78676478125e-6", ["US tablespoon", "Us tbsp", "Us Tbsp"])
    us_tsp = Unit("4.92892159375e-6", ["US tsp"])
    us_fluid_darm = Unit("3.6966911953125e-6")

    us_dry_gallon = Unit(
        "4.40488377086e-3", ["US dry gallon", "corn gallon", "grain gallon"]
    )
    us_dry_quart = Unit("1.101220942715e-3")
    us_dry_pint = Unit("550.6104713575e-6")
    us_bushel = Unit("35.23907016688e-3", ["US bsh", "US bu"])

    cubic_inch = Unit("16.387064e-6", ["cu in"])
    cubic_foot = Unit("0.02832", ["cu ft"])

    imperial_gallon = Unit(
        "4.54609e-3", ["Imperial gallon", "Imperial gal", "gallon (Imperial)"]
    )
    imperial_fluid_ounce = Unit("28.41306e-6", ["Imperial fluid ounce", "imp fl oz"])
    imperial_quart = Unit("1.1365225e-6", ["Imperial quart"])
    imperial_pint = Unit("568.26125e-6", ["Imperial pint"])
    imperial_gill = Unit("142.0653125e-6", ["Imperial gill"])
    imperial_bushel = Unit("36.36872e-3", ["imp bsh", "imp bu"])
    imperial_fluid_darm = Unit("3.5516328125e-6", ["luid drachm"])

    au_tablespoon = Unit("20e-6", ["Australian tablespoon", "Australian tbsp"])
    au_teaspoon = Unit(
        "5e-6",
        [
            "US tsp (food nutrition labelling)",
            "metic teaspoon",
            "metric tsp",
            "Australian tsp",
        ],
    )

    oil_barrel = Unit("158.987294928e-3", ["oil bbl", "bbl"])

    @classmethod
    def _attr_to_unit(cls, name):
        if name[:6] in ["cubic_", "cubic "]:
            name = f"{name[6:]}³"
        return super()._attr_to_unit(name)

    def __truediv__(self, other):
        if isinstance(other, Distance):
            return Area(sq_metre=self.si_value / other.si_value)

        if isinstance(other, Area):
            return Distance(metre=self.si_value / other.si_value)

        return super().__truediv__(other)
