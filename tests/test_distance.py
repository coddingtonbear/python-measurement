# -*- coding: utf-8 -*-
from decimal import Decimal
from measurement.measures import Area, Distance

from .base import MeasurementTestBase


class DistanceTest(MeasurementTestBase):
    def test_conversion_equivalence(self):
        miles = Distance(mi=1)
        kilometers = Distance(km=1.609344)

        self.assertAlmostEqual(miles.km, kilometers.km)

    def test_attrib_conversion(self):
        kilometers = Distance(km=1)
        expected_meters = 1000

        self.assertAlmostEqual(kilometers.m, expected_meters)

    def test_identity_conversion(self):
        expected_miles = 10
        miles = Distance(mi=expected_miles)

        self.assertAlmostEqual(miles.mi, expected_miles)

    def test_auto_si_kwargs(self):
        meters = Distance(meter=1e6)
        megameters = Distance(megameter=1)

        self.assertEqual(
            meters, megameters,
        )

    def test_auto_si_attrs(self):
        one_meter = Distance(m=1)

        micrometers = one_meter.um

        self.assertEqual(one_meter.value * 10 ** 6, micrometers)

    def test_area_sq_km(self):
        one_sq_km = Area(sq_km=10)
        miles_sqd = Area(sq_mi=3.8610216)

        self.assertAlmostEqual(one_sq_km.standard, miles_sqd.standard, places=1)

    def test_set_value(self):
        distance = Distance(mi=10)

        expected_standard = 16093.44
        self.assertEqual(
            distance.standard, expected_standard,
        )

        distance.value = 11

        expected_standard = 17702.784
        self.assertEqual(distance.standard, expected_standard)

    def test_conversion_equivalence_decimal(self):
        miles = Distance(mi="1.0", decimal=True)
        kilometers = Distance(km="1.609344", decimal=True)

        print("test_conversion_equivalence_decimal", miles.km, kilometers.km)

        self.assertAlmostEqual(miles.km, kilometers.km)

    def test_attrib_conversion_decimal(self):
        kilometers = Distance(km="1.0", decimal=True)
        expected_meters = Decimal("1000")

        print("test_attrib_conversion_decimal", kilometers.m, expected_meters)

        self.assertAlmostEqual(kilometers.m, expected_meters)

    def test_identity_conversion_decimal(self):
        miles = Distance(mi="10", decimal=True)
        expected_miles = Decimal("10")

        print("test_identity_conversion_decimal", miles.mi, expected_miles)

        self.assertAlmostEqual(miles.mi, expected_miles)

    def test_auto_si_kwargs_decimal(self):
        meters = Distance(meter="1e6", decimal=True)
        megameters = Distance(megameter="1", decimal=True)

        print("test_auto_si_kwargs_decimal", meters, megameters)

        self.assertEqual(meters, megameters)

    def test_auto_si_attrs_decimal(self):
        one_meter = Distance(m="1", decimal=True)
        micrometers = one_meter.um

        print("test_auto_si_attrs_decimal", one_meter.value * 10 ** 6, micrometers)

        self.assertEqual(one_meter.value * 10 ** 6, micrometers)

    def test_area_sq_km_decimal(self):
        one_sq_km = Area(sq_km="10", decimal=True)
        miles_sqd = Area(sq_mi="3.8610215854244585", decimal=True)

        print("test_area_sq_km_decimal", one_sq_km.standard, miles_sqd.standard)

        self.assertAlmostEqual(one_sq_km.standard, miles_sqd.standard, places=9)

    def test_set_value_decimal(self):
        distance = Distance(mi="10", decimal=True)
        expected_standard = Decimal("16093.44")

        print("test_set_value_decimal", distance.standard, expected_standard)

        self.assertEqual(distance.standard, expected_standard)

        distance.value = Decimal("11")
        expected_standard = Decimal("17702.784")

        print("test_set_value_decimal part 2", distance.standard, expected_standard)

        self.assertEqual(distance.standard, expected_standard)
