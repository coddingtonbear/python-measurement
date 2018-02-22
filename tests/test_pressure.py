from decimal import Decimal

from .base import MeasurementTestBase


from measurement.measures import Pressure


class PressureTest(MeasurementTestBase):
    def test_sanity(self):
        bar = Pressure(bar=2)
        atm = Pressure(atm=Decimal('1.973846533432'))

        self.assertAlmostEqual(
            bar.Pa,
            atm.Pa
        )

    def test_conversion_to_non_si(self):
        bar = Pressure(bar=2)
        expected_torr = Decimal('1500.1275108384')
        self.assertAlmostEqual(
            bar.torr,
            expected_torr
        )

    def test_ensure_that_we_always_output_decimal(self):
        bar = Pressure(bar=2)

        atm = bar.atm

        self.assertTrue(
            isinstance(atm, Decimal)
        )
