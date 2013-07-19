from .base import MeasurementTestBase


from measurement.measures import Weight, Distance, Temperature
from measurement.utils import guess


class UtilsTest(MeasurementTestBase):
    def test_guess_weight(self):
        result = guess(23, 'g')

        self.assertEqual(
            result,
            Weight(g=23)
        )

    def test_guess_distance(self):
        result = guess(30, 'mi')

        self.assertEqual(
            result,
            Distance(mi=30)
        )

    def test_guess_temperature(self):
        result = guess(98, 'f')

        self.assertEqual(
            result,
            Temperature(f=98)
        )
