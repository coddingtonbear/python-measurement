from measurement import measures


class TestCurrent:
    def test_mul(self):
        assert measures.Current("2 A") * measures.Voltage(
            "12 V"
        ) == measures.ElectricPower("24 W")

    def test_mul__super(self):
        assert measures.Current("2 A") * 2 == measures.Current("4 A")


class TestVoltage:
    def test_mul(self):
        assert measures.Voltage("12 V") * measures.Current(
            "2 A"
        ) == measures.ElectricPower("24 W")

    def test_mul__super(self):
        assert measures.Voltage("6 V") * 2 == measures.Voltage("12 V")


class TestElectricPower:
    def test_truediv__voltage(self):
        assert measures.ElectricPower("24 W") / measures.Voltage(
            "12 V"
        ) == measures.Current("2 A")

    def test_truediv__current(self):
        assert measures.ElectricPower("24 W") / measures.Current(
            "4 A"
        ) == measures.Voltage("6 V")

    def test_truediv__super(self):
        assert measures.ElectricPower("24 W") / 2 == measures.ElectricPower("12 W")
