
Creating your own Measure Class
===============================

You can create your own measures easily by subclassing either
``measurement.base.MeasureBase`` or ``measurement.base.BidimensionalMeasure``.


Simple Measures
---------------

If your measure is not a measure dependent upon another measure (e.g speed, 
distance/time) you can create new measurement by creating a subclass of
``measurement.base.MeasureBase``.

A simple example is Weight:

.. code-block:: python

   from measurement.base import MeasureBase

   class Weight(MeasureBase):
       STANDARD_UNIT = 'g'
       UNITS = {
           'g': 1.0,
           'tonne': 1000000.0,
           'oz': 28.3495,
           'lb': 453.592,
           'stone': 6350.29,
           'short_ton': 907185.0,
           'long_ton': 1016000.0,
       }
       ALIAS = {
           'gram': 'g',
           'ton': 'short_ton',
           'metric tonne': 'tonne',
           'metric ton': 'tonne',
           'ounce': 'oz',
           'pound': 'lb',
           'short ton': 'short_ton',
           'long ton': 'long_ton',
       }
       SI_UNITS = ['g']

Important details:

* ``STANDARD_UNIT`` defines what unit will be used internally by the library
  for storing the value of this measurement.
* ``UNITS`` provides a mapping relating a unit of your ``STANDRD_UNIT`` to 
  any number of defined units.  In the example above, you will see that
  we've established ``28.3495 g`` to be equal to ``1 oz``.
* ``ALIAS`` provides a list of aliases mapping keyword arguments to ``UNITS``.
  these values are allowed to be used as keyword arguments when either creating
  a new unit or guessing a measurement using ``measurement.utils.guess``.
* ``SI_UNITS`` provides a list of units that are SI Units.  Units in this list
  will automatically have new units and aliases created for each of the main
  SI magnitudes.  In the above example, this causes the list of ``UNITS`` 
  and ``ALIAS`` es to be extended to include the following units (aliases):
  ``yg`` (yottagrams), ``zg`` (zeptograms), ``ag`` (attograms),
  ``fg`` (femtograms), ``pg`` (picograms), ``ng`` (nanograms),
  ``ug`` (micrograms), ``mg`` (milligrams), ``kg`` (kilograms),
  ``Mg`` (megagrams), ``Gg`` (gigagrams), ``Tg`` (teragrams),
  ``Pg`` (petagrams), ``Eg`` (exagrams), ``Zg`` (zetagrams),
  ``Yg`` (yottagrams).

Using formula-based conversions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In some situations, your conversions between units may not be simple enough
to be accomplished by using simple conversions (e.g. temperature); for
situations like that, you should use ``sympy`` to create expressions relating
your measure's standard unit and the unit you're defining:

.. code-block:: python

   from sympy import S, Symbol
   from measurement.base import MeasureBase

   class Tempoerature(MeasureBase):
       SU = Symbol('kelvin')
       STANDARD_UNIT = 'k'
       UNITS = {
           'c': SU - S(273.15),
           'f': (SU - S(273.15)) * S('9/5') + 32,
           'k': 1.0
       }
       ALIAS = {
           'celsius': 'c',
           'fahrenheit': 'f',
           'kelvin': 'k',
       }

Important details:

* See above 'Important Details' under `Normal Measures`.
* ``SU`` must define the symbol used in expressions relating your measure's
  ``STANDARD_UNIT`` to the unit you're defining. 


Bi-dimensional Measures
-----------------------

Some measures are really just compositions of two separate measures -- Speed,
being a measure of the amount of distance covered over a unit of time, is one
common example of such a measure.

You can create such measures by subclassing
``measurement.base.BidimensionalMeasure``.

.. code-block:: python

   from measurement.base import BidimensionalMeasure

   from measurement.measures.distance import Distance
   from measurement.measures.time import Time


   class Speed(BidimensionalMeasure):
       PRIMARY_DIMENSION = Distance
       REFERENCE_DIMENSION = Time

       ALIAS = {
           'mph': 'mi__hr',
           'kph': 'km__hr',
       }

Important details:

* ``PRIMARY_DIMENSION`` is a class that measures the variable dimension of
  this measure.  In the case of 'miles-per-hour', this would be the 'miles'
  or 'distance' dimension of the measurement.
* ``REFERENCE_DIMENSION`` is a class that measures the unit (reference)
  dimension of the measure.  In the case of 'miles-per-hour', this would be
  the 'hour' or 'time' dimension of the measurement.
* ``ALIAS`` defines a list of convenient abbreviations for use either when
  creating or defining a new instance of this measurement.  In the above case,
  you can create an instance of speed like ``Speed(mph=10)`` (equivalent to
  ``Speed(mile__hour=10)``) or convert to an existing measurement (
  ``speed_measurement``) into one of the aliased measures by accessing
  the attribute named -- ``speed_measurement.kph`` (equivalent to 
  ``speed_measurement.kilometer__hour``).

.. note::

   Although unit aliases defined in a bi-dimensional measurement's ``ALIAS``
   dictionary can be used either as keyword arguments or as attributes used
   for conversion, unit aliases defined in simple measurements (those
   subclassing ``measurement.base.MeasureBase``) can be used only as keyword
   arguments.

