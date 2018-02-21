from decimal import Decimal

from .base import MeasurementTestBase


from measurement.measures import Radiation, AbsorbedDose, Exposure


class RaditionTest(MeasurementTestBase):
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

class AbsorbedDoseTest(MeasurementTestBase):
    def test_sanity(self):
        gy = AbsorbedDose(Gy=2)
        rad = AbsorbedDose(rad=200)

        self.assertAlmostEqual(
            gy.Gy,
            rad.Gy
        )
    
    def test_conversion_to_non_si(self):
        rad = AbsorbedDose(rad=50)
        expected_ci = Decimal('.5')
        self.assertAlmostEqual(
            rad.Gy,
            expected_ci
        )

class ExposureTest(MeasurementTestBase):
    def test_sanity(self):
        c_kg = Exposure(C_kg=1)
        roentgen = Exposure(R=Decimal('3875.968992248062'))

        self.assertAlmostEqual(
            c_kg.C_kg,
            roentgen.C_kg
        )
    
    def test_conversion_to_non_si(self):
        r = Exposure(R=Decimal('3875.968992248062'))
        expected_ci = 1
        self.assertAlmostEqual(
            r.C_kg,
            expected_ci
        )