from __future__ import print_function

from measurement.base import MeasureBase, BidimensionalMeasure
from measurement.utils import get_all_measures

for measure in get_all_measures():
    classname = measure.__name__
    print(classname)
    print('-' * len(classname))
    print()
    if issubclass(measure, MeasureBase):
        units = measure.get_units()
        aliases = measure.get_aliases()
        print(
            '* *Acceptable as Arguments or Attributes*: %s' % (
                ', '.join(sorted(['``%s``' % unit for unit in units]))
            )
        )
        print(
            '* *Acceptable as Arguments*: %s' % (
                ', '.join(sorted(['``%s``' % alias for alias in aliases]))
            )
        )
    elif issubclass(measure, BidimensionalMeasure):
        print(".. note::")
        print("   This is a bi-dimensional measurement; bi-dimensional")
        print("   measures are created by finding an appropriate unit in the")
        print("   measure's primary measurement class, and an appropriate")
        print("   in the measure's reference class, and using them as a")
        print("   double-underscore-separated keyword argument (or, if")
        print("   converting to another unit, as an attribute).")
        print()
        print("   For example, to create an object representing 24 miles-per")
        print("   hour::")
        print()
        print("      >>> from measurement.measure import Speed")
        print("      >>> my_speed = Speed(mile__hour=24)")
        print("      >>> print my_speed")
        print("      24.0 mi/hr")
        print("      >>> print my_speed.km__hr")
        print("      38.624256")
        print()
        print(
            "* *Primary Measurement*: %s" % (
                measure.PRIMARY_DIMENSION.__name__
            )
        )
        print(
            "* *Reference Measurement*: %s" % (
                measure.REFERENCE_DIMENSION.__name__
            )
        )
    print()
