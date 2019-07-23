.. image:: https://travis-ci.org/coddingtonbear/python-measurement.svg?branch=master
   :target: https://travis-ci.org/coddingtonbear/python-measurement

Easily use and manipulate unit-aware measurement objects in Python.

`django.contrib.gis.measure <https://github.com/django/django/blob/master/django/contrib/gis/measure.py>`_
has these wonderful 'Distance' objects that can be used not only for storing a
unit-aware distance measurement, but also for converting between different
units and adding/subtracting these objects from one another.

This module not only provides those Distance and Area measurement
objects, but also other measurements including:

- Energy
- Speed
- Temperature
- Time
- Volume
- Weight

Example:

.. code-block:: python

   >>> from measurement.measures import Weight
   >>> weight_1 = Weight(lb=125)
   >>> weight_2 = Weight(kg=40)
   >>> added_together = weight_1 + weight_2
   >>> added_together
   Weight(lb=213.184976807)
   >>> added_together.kg  # Maybe I actually need this value in kg?
   96.699

.. warning::
   Measurements are stored internally by converting them to a
   floating-point number of a (generally) reasonable SI unit.  Given that 
   floating-point numbers are very slightly lossy, you should be aware of
   any inaccuracies that this might cause.

   TLDR: Do not use this in
   `navigation algorithms guiding probes into the atmosphere of extraterrestrial worlds <http://en.wikipedia.org/wiki/Mars_Climate_Orbiter>`_.

- Documentation for python-measurement is available an
  `ReadTheDocs <https://python-measurement.readthedocs.org/>`_.
- Please post issues on
  `Github <https://github.com/coddingtonbear/python-measurement/issues>`_.
- Test status available on
  `Travis-CI <https://travis-ci.org/coddingtonbear/python-measurement>`_.



.. image:: https://d2weczhvl823v0.cloudfront.net/coddingtonbear/python-measurement/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

