import pytest

from measurement.measures import Distance, Mass, Temperature
from measurement.utils import guess


def test_guess_weight():
    assert guess(23, "g") == Mass(g=23)


def test_guess_distance():
    assert guess(30, "mi") == Distance(mi=30)


def test_guess_temperature():
    assert guess(98, "°F") == Temperature(fahrenheit=98)


def test_guess__raise__value_error():
    with pytest.raises(ValueError) as e:
        guess(98, "does-not-exist")
    assert str(e.value) == "can't guess measure for '98 does-not-exist'"
