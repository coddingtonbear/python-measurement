from measurement.measures.mechanics import Speed


class TestSpeed:
    def test_attrconversion(self) -> None:
        assert Speed("10 m/s") == Speed("36 km/h")

    def test_addition(self) -> None:
        train_1 = Speed(mile__hour=10)
        train_2 = Speed(mile__hour=5)

        actual_value = train_1 + train_2
        expected_value = Speed(mile__hour=15)

        assert actual_value == expected_value

    def test_iadd(self) -> None:
        train_1 = Speed(mile__hour=10)
        train_2 = Speed(mile__hour=5)

        actual_value = train_1
        actual_value += train_2
        expected_value = Speed(mile__hour=15)

        assert actual_value == expected_value

    def test_sub(self) -> None:
        train_1 = Speed(mile__hour=10)
        train_2 = Speed(mile__hour=5)

        expected_value = Speed(mile__hour=5)
        actual_value = train_1 - train_2

        assert expected_value == actual_value

    def test_isub(self) -> None:
        train_1 = Speed(mile__hour=10)
        train_2 = Speed(mile__hour=5)

        expected_value = Speed(mile__hour=5)
        actual_value = train_1
        actual_value -= train_2

        assert expected_value == actual_value

    def test_mul(self) -> None:
        train_1 = Speed(mile__hour=10)
        multiplier = 2

        actual_value = multiplier * train_1
        expected_value = Speed(mile__hour=20)

        assert expected_value == actual_value

    def test_imul(self) -> None:
        train_1 = Speed(mile__hour=10)
        multiplier = 2

        actual_value = train_1
        actual_value *= multiplier
        expected_value = Speed(mile__hour=20)

        assert expected_value == actual_value

    def test_div(self) -> None:
        train_1 = Speed(mile__hour=10)
        divider = 2

        actual_value = train_1 / divider
        expected_value = Speed(mile__hour=5)

        assert expected_value == actual_value

    def test_idiv(self) -> None:
        train_1 = Speed(mile__hour=10)
        divider = 2

        actual_value = train_1
        actual_value /= divider
        expected_value = Speed(mile__hour=5)

        assert expected_value == actual_value

    def test_equals(self) -> None:
        train_1 = Speed(mile__hour=10)
        train_2 = Speed(mile__hour=10)

        assert train_1 == train_2

    def test_lt(self) -> None:
        train_1 = Speed(mile__hour=5)
        train_2 = Speed(mile__hour=10)

        assert train_1 < train_2

    def test_bool_true(self) -> None:
        train_1 = Speed(mile__hour=5)

        assert train_1

    def test_bool_false(self) -> None:
        train_1 = Speed(mile__hour=0)

        assert not train_1

    def test_abbreviations(self) -> None:
        train_1 = Speed(mph=4)
        train_2 = Speed(mile__hour=4)

        assert train_1 == train_2

    def test_different_units_addition(self) -> None:
        train = Speed(km__h=1)
        increase = Speed(m__h=10)

        assert train + increase == Speed("1.01 km/h")

    def test_mph(self) -> None:
        assert Speed(mph=10) == Speed(mi__h=10), Speed._units["mi__h"].factor

    def test_kph(self) -> None:
        assert Speed(kph=10) == Speed(km__h=10), Speed._units["km__h"].factor
