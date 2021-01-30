import decimal

import pytest

from measurement.base import ImmutableKeyDict, MetricUnit, Unit, qualname
from measurement.measures import Distance, Mass


def test_qualname():
    assert qualname(Distance) == "Distance"
    assert qualname(Distance("1 m")) == "Distance"


class TestImmutableKeyDict:
    def test_setitem(self):
        d = ImmutableKeyDict()
        d["foo"] = "bar"
        d["foo"] = "bar"
        with pytest.raises(KeyError) as e:
            d["foo"] = "baz"

        assert "Key 'foo' already exists with value 'bar'." in str(e.value)


class TestUnit:
    def test_post_init(self):
        inch = Unit("0.0254", ["in", "inches"])
        assert inch.factor == decimal.Decimal("0.0254")

    def test_get_symbols(self):
        inch = Unit("0.0254", ["in", "inches"])
        inch.name = "inch"
        assert list(inch.get_symbols()) == [
            ("inch", Unit("0.0254")),
            ("in", Unit("0.0254")),
            ("inches", Unit("0.0254")),
        ]

    def test_to_si(self):
        assert Unit("1").to_si(decimal.Decimal("10")) == decimal.Decimal("10")
        assert Unit("10").to_si(decimal.Decimal("10")) == decimal.Decimal("100")
        assert Unit("1E-3").to_si(decimal.Decimal("10")) == decimal.Decimal("1E-2")

    def test_from_si(self):
        assert Unit("1").from_si(decimal.Decimal("10")) == decimal.Decimal("10")
        assert Unit("10").from_si(decimal.Decimal("10")) == decimal.Decimal("1")
        assert Unit("1E-3").from_si(decimal.Decimal("10")) == decimal.Decimal("1E+4")


class TestMetricUnit:
    def test_get_symbols(self):
        metre = MetricUnit("1", ["m", "meter"], ["m"], ["metre", "meter"])
        metre.name = "metre"
        symbols = list(metre.get_symbols())

        assert ("metre", Unit("1")) in symbols
        assert ("m", Unit("1")) in symbols
        assert ("meter", Unit("1")) in symbols

        assert ("km", Unit("1E+3")) in symbols
        assert ("μm", Unit("1E-6")) in symbols

        assert ("Kilometre", Unit("1E+3")) in symbols
        assert ("kilometre", Unit("1E+3")) in symbols

        assert ("Kilometer", Unit("1E+3")) in symbols
        assert ("kilometer", Unit("1E+3")) in symbols

        assert ("nanometer", Unit("1E-9")) in symbols

    def test_get_symbols__unique_names(self):
        metre = MetricUnit("1", ["m", "meter"], ["m"], ["metre", "meter"])
        metre.name = "metre"
        symbols = list(metre.get_symbols())
        assert len([k for k, v in symbols]) == len({k for k, v in symbols})


class TestAbstractMeasure:
    measure = Distance
    unit = "m"

    def test_update_org_name(self):
        assert str(Distance("0.001 m")) == "1 mm"

    def test_repr(self):
        assert repr(Distance("1 km")) == 'Distance(metre="1E+3")'

    def test_str(self):
        assert str(Distance("1 km")) == "1 km"

    def test_format(self):
        assert f"{Distance('1 km') / 3:5.3f}" == "0.333 km"
        assert f"{Distance(km=1/3):5.3f}" == "0.333 km"
        with pytest.raises(ValueError):
            f"{Distance('1 km') / 3:5.3x}"

    def test_getitem(self):
        assert Distance("1 km")["m"] == decimal.Decimal("1000")
        with pytest.raises(KeyError) as e:
            Distance("1 km")["does not exist"]

        assert "Distance object has no key 'does not exist'" in str(e.value)

    def test_custom_string(self):
        m = Distance("1 km") / 3
        assert f"{m._value:.3f} {m.unit}" == "333.333 metre"

    def test_eq(self):
        assert self.measure(**{self.unit: 1}) == self.measure(**{self.unit: 1})

    def test_eq__not_implemented(self):
        assert self.measure(**{self.unit: 1}).__eq__("not-valid") is NotImplemented

    def test_tl(self):
        assert self.measure(**{self.unit: 1}) < self.measure(**{self.unit: 2})
        assert not self.measure(**{self.unit: 2}) < self.measure(**{self.unit: 1})

    def test_lt__not_implemented(self):
        assert self.measure(**{self.unit: 1}).__lt__("not-valid") is NotImplemented

    def test_gt(self):
        assert self.measure(**{self.unit: 2}) > self.measure(**{self.unit: 1})
        assert not self.measure(**{self.unit: 1}) > self.measure(**{self.unit: 1})

    def test_gt__not_implemented(self):
        assert self.measure(**{self.unit: 1}).__gt__("not-valid") is NotImplemented

    def test_add(self):
        assert self.measure(**{self.unit: 2}) + self.measure(
            **{self.unit: 1}
        ) == self.measure(**{self.unit: 3})

    def test_add__raise__type_error(self):
        with pytest.raises(TypeError) as e:
            self.measure(**{self.unit: 2}) + "not-allowed"
        assert str(e.value) == f"can't add type '{qualname(self.measure)}' to 'str'"

    def test_iadd(self):
        d = self.measure(**{self.unit: 2})
        d += self.measure(**{self.unit: 1})
        assert d == self.measure(**{self.unit: 3})

    def test_sub(self):
        assert self.measure(**{self.unit: 2}) - self.measure(
            **{self.unit: 1}
        ) == self.measure(**{self.unit: 1})

    def test_sub__raise__type_error(self):
        with pytest.raises(TypeError) as e:
            self.measure(**{self.unit: 2}) - "not-allowed"
        assert (
            str(e.value) == f"can't subtract type 'str' from '{qualname(self.measure)}'"
        )

    def test_isub(self):
        d = self.measure(**{self.unit: 2})
        d -= self.measure(**{self.unit: 1})
        assert d == self.measure(**{self.unit: 1})

    def test_mul(self):
        assert self.measure(**{self.unit: 2}) * 2 == self.measure(**{self.unit: 4})

    def test_mul__raise__type_error(self):
        with pytest.raises(TypeError) as e:
            self.measure(**{self.unit: 2}) * "not-allowed"
        assert (
            str(e.value) == f"can't multiply type '{qualname(self.measure)}' and 'str'"
        )

    def test_mul__raise_for_same_type(self):
        with pytest.raises(TypeError) as e:
            Mass("1 kg") * Mass("1 kg")
        assert str(e.value) == "can't multiply type 'Mass' and 'Mass'"

    def test_imul(self):
        d = self.measure(**{self.unit: 2})
        d *= 2
        assert d == self.measure(**{self.unit: 4})

        d = 2
        d *= self.measure(**{self.unit: 2})
        assert d == self.measure(**{self.unit: 4})

    def test_rmul(self):
        assert 2 * self.measure(**{self.unit: 2}) == self.measure(**{self.unit: 4})

    def test_truediv(self):
        assert self.measure(**{self.unit: 2}) / 2 == self.measure(**{self.unit: 1})
        assert self.measure(**{self.unit: 2}) / self.measure(**{self.unit: 2}) == 1

    def test_truediv__raise__type_error(self):
        with pytest.raises(TypeError) as e:
            self.measure(**{self.unit: 2}) / "not-allowed"
        assert str(e.value) == f"can't divide type '{qualname(self.measure)}' by 'str'"

    def test_itruediv(self):
        d = self.measure(**{self.unit: 2})
        d /= 2
        assert d == self.measure(**{self.unit: 1})

        d = 2
        d /= self.measure(**{self.unit: 2})
        assert d == self.measure(**{self.unit: 1})

        d = self.measure(**{self.unit: 2})
        d /= self.measure(**{self.unit: 2})
        assert d == 1

    def test_rtruediv(self):
        assert 2 / self.measure(**{self.unit: 2}) == self.measure(**{self.unit: 1})

    def test_bool(self):
        assert self.measure(**{self.unit: 1})
        assert self.measure(**{self.unit: -11})
        assert not self.measure(**{self.unit: 0})

    def test_getattr(self):
        assert Distance(m=1).inch == pytest.approx(decimal.Decimal("40"), abs=1)
        with pytest.raises(AttributeError):
            Distance(m=1).does_not_exist
