[![Build Status](https://travis-ci.org/latestrevision/python-measurement.png?branch=master)](https://travis-ci.org/latestrevision/python-measurement)

Python-Measurement
==================

Easily use and manipulate unit-aware measurement objects in Python.

[django.contrib.gis.measure](https://github.com/django/django/blob/master/django/contrib/gis/measure.py)
has these wonderful 'Distance' objects that can be used not only for storing a
unit-aware distance measurement, but also for converting between different
units and adding/subtracting these objects from one another.

This module not only provides those Distance (Length) and Area measurement
objects, but also other measurements including Weight and Volume.

Installation
------------

You can either install from pip:

    pip install measurement

*or* checkout and install the source from the [bitbucket repository](https://bitbucket.org/latestrevision/python-measurement):

    hg clone https://bitbucket.org/latestrevision/python-measurement
    cd python-measurement
    python setup.py install

*or* checkout and install the source from the [github repository](https://github.com/latestrevision/python-measurement):

    git clone https://github.com/latestrevision/python-measurement
    cd python-measurement
    python setup.py install
