from measurement.measures.mechanics import Speed


class TestSpeed:
    def test_attrconversion(self):
        assert Speed("10 m/s") == Speed("36 km/h")

    def test_addition(self):
        train_1 = Speed(mile__hour=10)
        train_2 = Speed(mile__hour=5)

        actual_value = train_1 + train_2
        expected_value = Speed(mile__hour=15)

        assert actual_value == expected_value

    def test_iadd(self):
        train_1 = Speed(mile__hour=10)
        train_2 = Speed(mile__hour=5)

        actual_value = train_1
        actual_value += train_2
        expected_value = Speed(mile__hour=15)

        assert actual_value == expected_value

    def test_sub(self):
        train_1 = Speed(mile__hour=10)
        train_2 = Speed(mile__hour=5)

        expected_value = Speed(mile__hour=5)
        actual_value = train_1 - train_2

        assert expected_value == actual_value

    def test_isub(self):
        train_1 = Speed(mile__hour=10)
        train_2 = Speed(mile__hour=5)

        expected_value = Speed(mile__hour=5)
        actual_value = train_1
        actual_value -= train_2

        assert expected_value == actual_value

    def test_mul(self):
        train_1 = Speed(mile__hour=10)
        multiplier = 2

        actual_value = multiplier * train_1
        expected_value = Speed(mile__hour=20)

        assert expected_value == actual_value

    def test_imul(self):
        train_1 = Speed(mile__hour=10)
        multiplier = 2

        actual_value = train_1
        actual_value *= multiplier
        expected_value = Speed(mile__hour=20)

        assert expected_value == actual_value

    def test_div(self):
        train_1 = Speed(mile__hour=10)
        divider = 2

        actual_value = train_1 / divider
        expected_value = Speed(mile__hour=5)

        assert expected_value == actual_value

    def test_idiv(self):
        train_1 = Speed(mile__hour=10)
        divider = 2

        actual_value = train_1
        actual_value /= divider
        expected_value = Speed(mile__hour=5)

        assert expected_value == actual_value

    def test_equals(self):
        train_1 = Speed(mile__hour=10)
        train_2 = Speed(mile__hour=10)

        assert train_1 == train_2

    def test_lt(self):
        train_1 = Speed(mile__hour=5)
        train_2 = Speed(mile__hour=10)

        assert train_1 < train_2

    def test_bool_true(self):
        train_1 = Speed(mile__hour=5)

        assert train_1

    def test_bool_false(self):
        train_1 = Speed(mile__hour=0)

        assert not train_1

    def test_abbreviations(self):
        train_1 = Speed(mph=4)
        train_2 = Speed(mile__hour=4)

        assert train_1 == train_2

    def test_different_units_addition(self):
        train = Speed(km__h=1)
        increase = Speed(m__h=10)

        assert train + increase == Speed("1.01 km/h")

    def test_mph(self):
        assert Speed(mph=10) == Speed(mi__h=10), Speed._units["mi__h"].factor

    def test_kph(self):
        assert Speed(kph=10) == Speed(km__h=10), Speed._units["km__h"].factor
