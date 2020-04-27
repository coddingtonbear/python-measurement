from measurement import measures


class TestFrequency:
    def test_mul(self) -> None:
        assert measures.Frequency("60 Hz") * measures.Time("2 s") == 120

    def test_mul__super(self) -> None:
        assert measures.Frequency("60 Hz") * 2 == measures.Frequency("120 Hz")
