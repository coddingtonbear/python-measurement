from .base import MeasurementTestBase


from measurement.measures import Speed


class SpeedTest(MeasurementTestBase):
    def test_attrconversion(self):
        meters_per_second = Speed(meter__second=10)
        miles_per_hour = 22.3694

        self.assertAlmostEqual(
            miles_per_hour,
            meters_per_second.mi__hr,
            places=3
        )

    def test_attrconversion_nonstandard(self):
        miles_per_hour = Speed(mi__hr=22.3694)
        kilometers_per_minute = 0.599748864

        self.assertAlmostEqual(
            kilometers_per_minute,
            miles_per_hour.km__min,
            places=3
        )

    def test_addition(self):
        train_1 = Speed(mile__hour=10)
        train_2 = Speed(mile__hour=5)

        actual_value = train_1 + train_2
        expected_value = Speed(mile__hour=15)

        self.assertEqual(
            actual_value,
            expected_value
        )

    def test_iadd(self):
        train_1 = Speed(mile__hour=10)
        train_2 = Speed(mile__hour=5)

        actual_value = train_1
        actual_value += train_2
        expected_value = Speed(mile__hour=15)

        self.assertEqual(
            actual_value,
            expected_value,
        )

    def test_sub(self):
        train_1 = Speed(mile__hour=10)
        train_2 = Speed(mile__hour=5)

        expected_value = Speed(mile__hour=5)
        actual_value = train_1 - train_2

        self.assertEqual(
            expected_value,
            actual_value
        )

    def test_isub(self):
        train_1 = Speed(mile__hour=10)
        train_2 = Speed(mile__hour=5)

        expected_value = Speed(mile__hour=5)
        actual_value = train_1
        actual_value -= train_2

        self.assertEqual(
            expected_value,
            actual_value,
        )

    def test_mul(self):
        train_1 = Speed(mile__hour=10)
        multiplier = 2

        actual_value = multiplier * train_1
        expected_value = Speed(mile__hour=20)

        self.assertEqual(
            actual_value,
            expected_value,
        )

    def test_imul(self):
        train_1 = Speed(mile__hour=10)
        multiplier = 2

        actual_value = train_1
        actual_value *= multiplier
        expected_value = Speed(mile__hour=20)

        self.assertEqual(
            actual_value,
            expected_value,
        )

    def test_div(self):
        train_1 = Speed(mile__hour=10)
        divider = 2

        actual_value = train_1 / divider
        expected_value = Speed(mile__hour=5)

        self.assertEqual(
            actual_value,
            expected_value,
        )

    def test_idiv(self):
        train_1 = Speed(mile__hour=10)
        divider = 2

        actual_value = train_1
        actual_value /= divider
        expected_value = Speed(mile__hour=5)

        self.assertEqual(
            actual_value,
            expected_value,
        )

    def test_equals(self):
        train_1 = Speed(mile__hour=10)
        train_2 = Speed(mile__hour=10)

        self.assertEqual(
            train_1,
            train_2,
        )

    def test_lt(self):
        train_1 = Speed(mile__hour=5)
        train_2 = Speed(mile__hour=10)

        self.assertTrue(
            train_1 < train_2
        )

    def test_bool_true(self):
        train_1 = Speed(mile__hour=5)

        self.assertTrue(
            train_1
        )

    def test_bool_false(self):
        train_1 = Speed(mile__hour=0)

        self.assertFalse(
            train_1
        )

    def test_abbreviations(self):
        train_1 = Speed(mph=4)
        train_2 = Speed(mile__hour=4)

        self.assertEqual(
            train_1,
            train_2
        )

    def test_different_units_addition(self):
        train = Speed(mile__hour=10)
        increase = Speed(km__day=2)

        two_km_day_in_mph = 0.0517809327

        expected_speed = Speed(mile__hour=10 + two_km_day_in_mph)
        actual_speed = train + increase

        self.assertAlmostEqual(
            expected_speed.standard,
            actual_speed.standard,
        )

    def test_aliases(self):
        speed = Speed(mph=10)

        expected_kph = 16.09344
        actual_kph = speed.kph

        self.assertAlmostEqual(
            expected_kph,
            actual_kph,
        )

    def test_set_unit(self):
        speed = Speed(mi__hr=10)
        speed.unit = 'm__sec'

        expected_value = 4.4704
        actual_value = speed.value

        self.assertAlmostEqual(
            expected_value,
            actual_value,
        )
