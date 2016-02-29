from decimal import Decimal

from .base import MeasurementTestBase


from measurement.measures import Radiation


class PressureTest(MeasurementTestBase):
    def test_sanity(self):
        bq = Radiation(bq=2)
        ci = Radiation(ci=Decimal('5.4054054054054E-11'))

        self.assertAlmostEqual(
            bq.bq,
            ci.bq
        )

    def test_conversion_to_non_si(self):
        bar = Radiation(bq=2)
        expected_ci = Decimal('5.4054054054054E-11')
        self.assertAlmostEqual(
            bar.ci,
            expected_ci
        )

