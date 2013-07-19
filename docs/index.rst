.. python-measurement documentation master file, created by
   sphinx-quickstart on Tue Jan 22 20:02:38 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

python-measurement
==================

.. image:: https://travis-ci.org/latestrevision/python-measurement.png?branch=master
   :target: https://travis-ci.org/latestrevision/python-measurement

Easily use and manipulate unit-aware measurement objects in Python.

`django.contrib.gis.measure <https://github.com/django/django/blob/master/django/contrib/gis/measure.py>`_
has these wonderful 'Distance' objects that can be used not only for storing a
unit-aware distance measurement, but also for converting between different
units and adding/subtracting these objects from one another.

This module not only provides those Distance and Area measurement objects
(courtesy of Django), but also other measurements including Weight, Volume, and
Temperature.

.. warning::
   Measurements are stored internally by converting them to a
   floating-point number of a (generally) reasonable SI unit.  Given that 
   floating-point numbers are very slightly lossy, you should be aware of
   any inaccuracies that this might cause.

   TLDR: Do not use this in
   `navigation algorithms guiding probes into the atmosphere of extraterrestrial worlds <http://en.wikipedia.org/wiki/Mars_Climate_Orbiter>`_.

Contents:

.. toctree::
   :maxdepth: 2
   :glob:

   topics/*


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

