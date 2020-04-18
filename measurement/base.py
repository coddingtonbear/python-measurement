"""Collection of helpers and base classes to build measure."""
import abc
import dataclasses
import decimal
import inspect
import warnings
from functools import total_ordering
from typing import Any, Dict, Iterable, List, Optional, Tuple, Type, Union


def qualname(obj: Any) -> str:
    return obj.__qualname__ if inspect.isclass(obj) else type(obj).__qualname__


class ImmutableKeyDict(Dict):
    """Like :class:`.dict` but any key may only assigned to a value once."""

    def __setitem__(self, key, value):
        """
        Map item to key once and raise error if the same key is set twice.

        Raises:
            KeyError: If key has been already assigned to a different item.
        """
        if key in self.keys() and value is not self[key]:
            raise KeyError(f"Key '{key}' already exists with value '{self[key]}'.")
        dict.__setitem__(self, key, value)


class AbstractUnit(abc.ABC):
    """
    Helper class to define units of measurement in relation to their SI definition.

    Nowerdays all units of measurement are defined based on fundamental SI units.
    This class provides behavior to convert a SI unit based measure to another Unit.
    """

    name = None

    @abc.abstractmethod
    def to_si(self, value: decimal.Decimal) -> decimal.Decimal:
        """Return SI measure based on given value in the unit defined by this class."""

    @abc.abstractmethod
    def from_si(self, value: decimal.Decimal) -> decimal.Decimal:
        """Return measure in the unit defined by this class based on given SI measure."""

    @abc.abstractmethod
    def get_symbols(self) -> Iterable[Tuple[str, Type["AbstractUnit"]]]:
        """Return list of symbol names and their :class:`.AbstractUnit` representation."""

    def __str__(self):
        return str(self.name)


@dataclasses.dataclass
class Unit(AbstractUnit):
    """
    Helper class for units that are defined as a multiple of an SI unit.

    Usage::

        from measurements.base import AbstractMeasure, Unit


        class Distance(AbstractMeasure):
            metre = Unit("1", ['m', 'meter'])
            inch = Unit("0.0254", ["in", "inches"])

    In the example aboce we implemented a simple distance measure. This first
    argument of a unit is it's SI unit factor. For the SI unit itself –
    in this example metre – it's "1". For inches, the factor is by which number
    you would need to multiple a meter to get to an inch. Or, 0.0254 metres make
    an inch.

    The second argument is a list of symbols, that are used to describe the unit.
    In the case of a metre, it is ``m`` and also the American English `meter`.
    Note that the attribute name itself, will also be added automatically to
    the list of symboles.
    """

    factor: Union[str, decimal.Decimal] = None
    """
    Factor of given measure based on SI unit.

    The given value must be either a :class:`Decimal<decimal.Decimal>`
    or a string that can be used to construct a decimal.
    """

    symbols: List[str] = dataclasses.field(default_factory=list)
    """Symbols used to describe this unit."""

    def __post_init__(self):
        if self.factor is not None:
            self.factor = decimal.Decimal(self.factor)

    def to_si(self, value):
        return value * self.factor

    def from_si(self, value):
        return value / self.factor

    def get_symbols(self):
        yield self.name.replace("_", " "), Unit(self.factor)
        yield from ((name, Unit(self.factor)) for name in self.symbols)


@dataclasses.dataclass
class MetricUnit(Unit):
    """Like :class:`.Unit` but with metric prefixes like ``kilo`` for ``kilometre``."""

    small_metric_symbol: List[str] = dataclasses.field(default_factory=list)
    """
    List of symboles that are used with single letter metric prefixes,
    such as ``m`` for ``km`` or ``μm``.
    """

    metric_prefix: List[str] = dataclasses.field(default_factory=list)
    """
    List of symboles that are used with full words metric prefixes,
    such as ``metre`` for ``kilometre``.
    """

    SI_PREFIXE_SYMBOLS = {
        "y": decimal.Decimal("1e-24"),
        "z": decimal.Decimal("1e-21"),
        "a": decimal.Decimal("1e-18"),
        "f": decimal.Decimal("1e-15"),
        "p": decimal.Decimal("1e-12"),
        "n": decimal.Decimal("1e-9"),
        "u": decimal.Decimal("1e-6"),
        "μ": decimal.Decimal("1e-6"),
        "m": decimal.Decimal("1e-3"),
        "c": decimal.Decimal("1e-2"),
        "d": decimal.Decimal("1e-1"),
        "da": decimal.Decimal("1e1"),
        "h": decimal.Decimal("1e2"),
        "k": decimal.Decimal("1e3"),
        "M": decimal.Decimal("1e6"),
        "G": decimal.Decimal("1e9"),
        "T": decimal.Decimal("1e12"),
        "P": decimal.Decimal("1e15"),
        "E": decimal.Decimal("1e18"),
        "Z": decimal.Decimal("1e21"),
        "Y": decimal.Decimal("1e24"),
    }

    SI_PREFIXES = {
        "yocto": decimal.Decimal("1e-24"),
        "zepto": decimal.Decimal("1e-21"),
        "atto": decimal.Decimal("1e-18"),
        "femto": decimal.Decimal("1e-15"),
        "pico": decimal.Decimal("1e-12"),
        "nano": decimal.Decimal("1e-9"),
        "micro": decimal.Decimal("1e-6"),
        "milli": decimal.Decimal("1e-3"),
        "centi": decimal.Decimal("1e-2"),
        "deci": decimal.Decimal("1e-1"),
        "deca": decimal.Decimal("1e1"),
        "hecto": decimal.Decimal("1e2"),
        "kilo": decimal.Decimal("1e3"),
        "mega": decimal.Decimal("1e6"),
        "giga": decimal.Decimal("1e9"),
        "tera": decimal.Decimal("1e12"),
        "peta": decimal.Decimal("1e15"),
        "exa": decimal.Decimal("1e18"),
        "zeta": decimal.Decimal("1e21"),
        "yotta": decimal.Decimal("1e24"),
    }

    def get_symbols(self):
        yield from super().get_symbols()
        yield from (
            (f"{prefix}{s}", Unit(factor=self.factor * factor))
            for prefix, factor in self.SI_PREFIXE_SYMBOLS.items()
            for s in self.small_metric_symbol
        )
        yield from (
            (f"{prefix}{s}", Unit(factor=self.factor * factor))
            for prefix, factor in self.SI_PREFIXES.items()
            for s in self.metric_prefix
        )
        yield from (
            (f"{prefix}{s}".title(), Unit(factor=self.factor * factor))
            for prefix, factor in self.SI_PREFIXES.items()
            for s in self.metric_prefix
        )


class MeasureBase(type):
    """
    Create Measure class by unpacking all symbols into a dictionary.

    Units can be added to measure by adding :class:`.AbstractUnit` instances as
    class attributes to a Measure. This metaclass removes to attributes and
    creates a dictionary mapping all sympbols to their corresponding
    :class:`.AbstractUnit` implementation.

    Raises:
        KeyError: If the same symbol is used for multiple units.

    """

    def __new__(mcs, name, bases, attrs):
        mcs.freeze_org_units(attrs)
        symbols = ImmutableKeyDict()
        new_attr = {}
        for attr_name, attr in attrs.items():
            if isinstance(attr, AbstractUnit):
                attr.name = attr_name
                for symbol, unit in attr.get_symbols():
                    unit.name = attr_name
                    symbols[symbol] = unit
            else:
                new_attr[attr_name] = attr

        cls = super().__new__(mcs, name, bases, new_attr)
        cls._units = symbols
        return cls

    @staticmethod
    def freeze_org_units(attrs: Dict[str, Any]):
        if "_org_units" in attrs:
            return

        attrs["_org_units"] = {
            attr_name: attr
            for attr_name, attr in attrs.items()
            if isinstance(attr, Unit)
        }


@total_ordering
class AbstractMeasure(metaclass=MeasureBase):
    """Abstract super class to all measures."""

    def __init__(
        self,
        value: Union[str, decimal.Decimal, int, None] = None,
        unit: Optional[str] = None,
        **kwargs: Union[str, decimal.Decimal, int, None],
    ):
        if kwargs:
            unit, value = kwargs.popitem()
        if unit is None:
            value, unit = value.split(maxsplit=1)
            value = decimal.Decimal(value)

        if isinstance(value, int):
            value = decimal.Decimal(str(value))

        if not isinstance(value, (decimal.Decimal, str, int)):
            warnings.warn(f"'value' expects type Decimal not {qualname(value)}")
        value = decimal.Decimal(value)

        unit = self._attr_to_unit(unit)
        self.unit = self._units[unit]
        self.unit.org_name = unit
        self.si_value = self.unit.to_si(value)

    def __getattr__(self, name):
        try:
            unit = self._units[self._attr_to_unit(name)]
        except KeyError as e:
            raise AttributeError(
                f"{qualname(self)} object has no attribute '{name}'"
            ) from e
        else:
            return unit.from_si(self.si_value)

    def __getitem__(self, item):
        try:
            unit = self._units[self._attr_to_unit(item)]
        except KeyError as e:
            raise KeyError(f"{qualname(self)} object has no key '{item}'") from e
        else:
            return unit.from_si(self.si_value)

    @classmethod
    def _attr_to_unit(cls, name: str) -> str:
        return name.replace("_", " ")

    unit = None
    """Return :class:`~Unit` initially given to construct the measure."""

    @property
    def _value(self) -> decimal.Decimal:
        """Return :class:`~Decimal` value of measure in the given :attr:`.unit`."""
        return getattr(self, self.unit.name)

    def __repr__(self):
        return f'{qualname(self)}({self.unit.name}="{getattr(self, self.unit.name)}")'

    def __str__(self):
        return "%s %s" % (getattr(self, self.unit.org_name), self.unit.org_name)

    def __format__(self, format_spec):
        decimal_format = getattr(self, self.unit.org_name).__format__(format_spec)
        return f"{decimal_format} {self.unit.org_name}"

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.si_value == other.si_value

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.si_value < other.si_value

    def __gt__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.si_value > other.si_value

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"can't add type '{qualname(self)}' to '{qualname(other)}'")
        return type(self)(
            value=self._value + getattr(other, self.unit.name), unit=self.unit.name
        )

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(
                f"can't substract type '{qualname(other)}' from '{qualname(self)}'"
            )

        return type(self)(
            value=self._value - getattr(other, self.unit.name), unit=self.unit.name
        )

    def __isub__(self, other):
        return self - other

    def __mul__(self, other):
        try:
            value = getattr(self, self.unit.org_name) * other
            return type(self)(value=value, unit=self.unit.org_name)
        except TypeError as e:
            raise TypeError(
                f"can't multiply type '{qualname(self)}' and '{qualname(other)}'"
            ) from e

    def __imul__(self, other):
        return self * other

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, type(self)):
            return self.si_value / other.si_value
        try:
            value = getattr(self, self.unit.org_name) / other
        except TypeError as e:
            raise TypeError(
                f"can't devide type '{qualname(self)}' by '{qualname(other)}'"
            ) from e
        else:
            return type(self)(value=value, unit=self.unit.org_name)

    def __itruediv__(self, other):
        return self / other

    def __rtruediv__(self, other):
        return self / other

    def __bool__(self):
        return bool(self.si_value)
