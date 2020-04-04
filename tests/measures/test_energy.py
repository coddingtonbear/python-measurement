from measurement.measures import Energy


class TestEnergy:
    def test_dietary_calories_kwarg(self):
        calories = Energy(Calorie=2000)
        kilojoules = Energy(kJ=8368)

        assert calories.si_value == kilojoules.si_value
