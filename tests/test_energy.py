from measurement.measures import Energy

from .base import MeasurementTestBase


class EnergyTest(MeasurementTestBase):
    def test_dietary_calories_kwarg(self):
        calories = Energy(Calorie=2000)
        kilojoules = Energy(kJ=8368)

        self.assertEqual(calories.standard, kilojoules.standard)


    def test_dietary_calories_kwarg_decimal(self):
        calories = Energy(Calorie="2000", decimal=True)
        kilojoules = Energy(kJ="8368", decimal=True)

        print("test_dietary_calories_kwarg_decimal", calories.standard, kilojoules.standard)

        self.assertEqual(calories.standard, kilojoules.standard)
