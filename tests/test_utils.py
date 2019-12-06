from measurement.measures import Distance, Mass, Temperature
from measurement.utils import guess

from .base import MeasurementTestBase


class UtilsTest(MeasurementTestBase):
    def test_guess_weight(self):
        result = guess(23, "g")

        self.assertEqual(result, Mass(g=23))

    def test_guess_distance(self):
        result = guess(30, "mi")

        self.assertEqual(result, Distance(mi=30))

    def test_guess_temperature(self):
        result = guess(98, "f")

        self.assertEqual(result, Temperature(f=98))
