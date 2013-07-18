from .base import MeasurementTestBase


from measurement.measures import Distance


class DistanceTest(MeasurementTestBase):
    def test_conversion_equivalence(self):
        miles = Distance(mi=1)
        kilometers = Distance(km=1.609344)

        self.assertAlmostEqual(
            miles.km,
            kilometers.km
        )

    def test_attrib_conversion(self):
        kilometers = Distance(km=1)
        expected_meters = 1000

        self.assertAlmostEqual(
            kilometers.m,
            expected_meters
        )

    def test_identity_conversion(self):
        expected_miles = 10
        miles = Distance(mi=expected_miles)

        self.assertAlmostEqual(
            miles.mi,
            expected_miles
        )
