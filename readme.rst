.. image:: https://travis-ci.org/latestrevision/python-measurement.png?branch=master
   :target: https://travis-ci.org/latestrevision/python-measurement

Easily use and manipulate unit-aware measurement objects in Python.

`django.contrib.gis.measure <https://github.com/django/django/blob/master/django/contrib/gis/measure.py>`_
has these wonderful 'Distance' objects that can be used not only for storing a
unit-aware distance measurement, but also for converting between different
units and adding/subtracting these objects from one another.

This module not only provides those Distance (Length) and Area measurement
objects, but also other measurements including Weight, Volume, and Temperature.

.. warning::
   Measurements are stored internally by converting them to a
   floating-point number of a (generally) reasonable SI unit.  Given that 
   floating-point numbers are very slightly lossy, you should be aware of
   any inaccuracies that this might cause.

TLDR: Do not use this in
`navigation algorithms guiding probes into the atmosphere of extraterrestrial worlds <http://en.wikipedia.org/wiki/Mars_Climate_Orbiter>`_.

- Documentation for python-measurement is available an
  `ReadTheDocs <http://python-measurement.readthedocs.org/>`_.
- Please post issues on
  `BitBucket <http://bitbucket.org/latestrevision/python-measurement/issues?status=new&status=open>`_.
- Test status available on
  `Travis-CI <https://travis-ci.org/latestrevision/python-measurement>`_.

