from decimal import Decimal

from .base import MeasurementTestBase


from measurement.measures import Radiation, RadiationAbsorbedDose, RadiationExposure


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

class RadiationAbsorbedDoseTest(MeasurementTestBase):
    def test_sanity(self):
        gy = RadiationAbsorbedDose(Gy=2)
        rad = RadiationAbsorbedDose(rad=200)

        self.assertAlmostEqual(
            gy.Gy,
            rad.Gy
        )
    
    def test_conversion_to_non_si(self):
        rad = RadiationAbsorbedDose(rad=50)
        expected_ci = Decimal('.5')
        self.assertAlmostEqual(
            rad.Gy,
            expected_ci
        )

class RadiationExposureTest(MeasurementTestBase):
    def test_sanity(self):
        c_kg = RadiationExposure(C_kg=1)
        roentgen = RadiationExposure(R=Decimal('3875.968992248062'))

        self.assertAlmostEqual(
            c_kg.C_kg,
            roentgen.C_kg
        )
    
    def test_conversion_to_non_si(self):
        r = RadiationExposure(R=Decimal('3875.968992248062'))
        r2 = RadiationExposure(mR=Decimal('3875.968992248062') * 1000)
        expected_ci = 1
        self.assertAlmostEqual(
            r.C_kg,
            expected_ci
        )
        self.assertAlmostEqual(
            r2.C_kg,
            expected_ci
        )