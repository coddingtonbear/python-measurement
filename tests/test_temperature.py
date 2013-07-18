from .base import MeasurementTestBase


from measurement.measures import Temperature


class TemperatureTest(MeasurementTestBase):
    def test_sanity(self):
        fahrenheit = Temperature(fahrenheit=70)
        celsius = Temperature(celsius=21.1111111)

        self.assertAlmostEqual(
            fahrenheit.k,
            celsius.k
        )

    def test_conversion_to_non_si(self):
        celsius = Temperature(celsius=21.1111111)
        expected_farenheit = 70

        self.assertAlmostEqual(
            celsius.f,
            expected_farenheit
        )

    def test_ensure_that_we_always_output_float(self):
        kelvin = Temperature(kelvin=10)

        celsius = kelvin.c

        self.assertTrue(
            isinstance(celsius, float)
        )
