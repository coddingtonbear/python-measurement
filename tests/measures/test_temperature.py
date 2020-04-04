import decimal

import pytest

from measurement.measures import Temperature


class TestTemperature:
    def test_sanity(self):
        fahrenheit = Temperature(fahrenheit=70)
        celsius = Temperature(celsius=21.1111111)

        assert fahrenheit.K == pytest.approx(celsius.K)

    def test_conversion_to_non_si(self):
        celsius = Temperature(celsius=21.1111111)
        expected_farenheit = decimal.Decimal("70")

        assert celsius.fahrenheit == pytest.approx(expected_farenheit)

    def test_ensure_that_we_always_output_float(self):
        kelvin = Temperature(kelvin=10)
        assert isinstance(kelvin.celsius, decimal.Decimal)
