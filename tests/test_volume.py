from .base import MeasurementTestBase


from measurement.measures import Volume


class VolumeTest(MeasurementTestBase):
    def test_sub_one_base_si_measure(self):
        milliliters = Volume(ml=200)
        fl_oz = Volume(us_oz=6.76280454)

        self.assertAlmostEqual(
            milliliters.standard,
            fl_oz.standard
        )
