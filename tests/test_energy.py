from measurement.measures import Energy

from .base import MeasurementTestBase


class EnergyTest(MeasurementTestBase):
    def test_dietary_calories_kwarg(self):
        calories = Energy(Calorie=2000)
        kilojoules = Energy(kJ=8368)

        self.assertEqual(
            calories.standard, kilojoules.standard,
        )
