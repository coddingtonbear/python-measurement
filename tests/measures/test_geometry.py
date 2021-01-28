import decimal

import pytest

from measurement.measures import Area, Distance, Volume


class TestDistance:
    def test_conversion_equivalence(self) -> None:
        miles = Distance(mi=1)
        kilometers = Distance(km=decimal.Decimal("1.609344"))

        assert miles.km == kilometers.km

    def test_attrib_conversion(self) -> None:
        kilometers = Distance(km=1)
        expected_meters = 1000

        assert kilometers.m == expected_meters

    def test_identity_conversion(self) -> None:
        expected_miles = 10
        miles = Distance(mi=expected_miles)

        assert miles.mi == expected_miles

    def test_auto_si_kwargs(self) -> None:
        meters = Distance(meter=1e6)
        megameters = Distance(megameter=1)

        assert meters == megameters

    def test_auto_si_attrs(self) -> None:
        one_meter = Distance(m=1)

        micrometers = one_meter.um

        assert one_meter.si_value * 10 ** 6 == micrometers

    def test_area_sq_km(self) -> None:
        one_sq_km = Area(sq_km=10)
        miles_sqd = Area(sq_mi=decimal.Decimal("3.861021585424458472628811394"))

        assert one_sq_km.si_value == miles_sqd.si_value

    def test_mul__distance(self) -> None:
        assert Distance(m=1) * Distance(m=1) == Area("1 m²")

    def test_mul__area(self) -> None:
        assert Distance(m=1) * Area(sq_m=1) == Volume("1 m³")

    def test_mul__super(self) -> None:
        assert Distance(m=1) * 3 == Distance("3 m")

    def test_pow(self) -> None:
        assert Distance(m=1) ** 2 == Area("1 m²")
        assert Distance(m=1) ** 3 == Volume("1 m³")

        with pytest.raises(TypeError):
            Distance(m=1) ** 4


class TestArea:
    def test_truediv(self) -> None:
        assert Area("1 m²") / Distance("1 m") == Distance("1 m")

    def test_truediv__super(self) -> None:
        assert Area("1 m²") / 2 == Area("0.5 m²")

    def test_mul(self) -> None:
        assert Area("1 m²") * Distance("1 m") == Volume("1 m³")

    def test_mul__super(self) -> None:
        assert Area("1 m²") * 2 == Area("2 m²")

    def test_attr_to_unit(self) -> None:
        assert Area._attr_to_unit("sq_m") == "m²"
        assert Area._attr_to_unit("sq m") == "m²"
        assert Area._attr_to_unit("square_m") == "m²"
        assert Area._attr_to_unit("square m") == "m²"
        assert Area._attr_to_unit("m²") == "m²"


class TestVolume:
    def test_truediv__distance(self) -> None:
        assert Volume("1 m³") / Distance("1 m") == Area("1 m²")

    def test_truediv__area(self) -> None:
        assert Volume("1 m³") / Area("1 m²") == Distance("1 m")

    def test_truediv__super(self) -> None:
        assert Volume("1 m³") / 2 == Volume("0.5 m³")

    def test_litre(self) -> None:
        assert Volume("1 cubic metre") == Volume("1000 L")
        assert Volume("1 mL") == Volume("1e-6 m³")

    def test_us_fluid_ounce(self) -> None:
        assert Volume("29.57353 mL") == Volume("1 US fl oz")

    def test_imperial_flud_ounce(self) -> None:
        assert Volume("28.41306 mL") == Volume("1 imp fl oz")
