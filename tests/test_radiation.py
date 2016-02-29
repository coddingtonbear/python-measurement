from decimal import Decimal

from .base import MeasurementTestBase


from measurement.measures import Radiation


class PressureTest(MeasurementTestBase):
    def test_sanity(self):
        bq = Radiation(Bq=2)
        ci = Radiation(Ci=Decimal('5.4054054054054E-11'))

        self.assertAlmostEqual(
            bq.Bq,
            ci.Bq
        )

    def test_conversion_to_non_si(self):
        bar = Radiation(Bq=2)
        expected_ci = Decimal('5.4054054054054E-11')
        self.assertAlmostEqual(
            bar.Ci,
            expected_ci
        )

