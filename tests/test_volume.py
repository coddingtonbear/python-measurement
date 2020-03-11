from measurement.measures import Volume

from .base import MeasurementTestBase


class VolumeTest(MeasurementTestBase):
    def test_sub_one_base_si_measure(self):
        milliliters = Volume(ml=200)
        fl_oz = Volume(us_oz=6.76280454)

        self.assertAlmostEqual(milliliters.standard, fl_oz.standard)


    def test_sub_one_base_si_measure_decimal(self):
        milliliters = Volume(ml="200", decimal=True)
        fl_oz = Volume(us_oz="6.76280454", decimal=True)

        print("test_sub_one_base_si_measure_decimal", milliliters.standard, fl_oz.standard)

        self.assertAlmostEqual(milliliters.standard, fl_oz.standard)
