Measures
========

There two different ways to instanciate a measure. The recommended way to instaciate
a measure object is with a :class:`Decimal<decicmal.Decimal>` value
and a :class:`String<str>` unit:

    >>> from measurement import measures
    >>> measures.Distance('1.0', 'm')
    Distance(metre="1.0")

Additinally, you may either pass a string
containing the value and unit separated by a string:

    >>> from measurement import measures
    >>> measures.Distance("1 m")
    Distance(metre="1")

or you can pass the value to the right unit argument:

    >>> from measurement import measures
    >>> measures.Distance(m=1)
    Distance(metre="1")

To concert a measure into another unit you can get the correct unit key:

    >>> from measurement import measures
    >>> measures.Distance("1 m")['ft']
    Decimal('3.280839895013123359580052493')

or attribute:

    >>> from measurement import measures
    >>> measures.Distance("1 m").ft
    Decimal('3.280839895013123359580052493')

.. note::
    Python has restrictions on attribute names.
    E.g. you can not use white spaces:

        >>> from measurement import measures
        >>> measures.Distance(Nautical Mile=1).km
        Traceback (most recent call last):
          File "<stdin>", line 1
            measures.Distance(Nautical Mile=1).km
                                          ^
        SyntaxError: invalid syntax

    In this case, you may use underscrose instead of spaces:

        >>> from measurement import measures
        >>> measures.Distance(nautical_mile=1).km
        Decimal('1.852')

    or preferably the string version:

        >>> measures.Distance('1 Nautical Mile').km
        Decimal('1.852')

    See also: https://docs.python.org/3/reference/lexical_analysis.html#identifiers

Some Units have `Metric Prefixes`_ like ``kilometre`` or ``kilogram``.
Prefixes are supported for all metric units in their short and long version, e.g:

    >>> from measurement import measures
    >>> measures.Distance('1 μm')['hectometer']
    Decimal('1E-8')

.. _`Metric Prefixes`: https://en.wikipedia.org/wiki/Metric_prefix

Supported Measures and Units
----------------------------

.. automodule:: measurement.measures
  :members:
  :undoc-members:
  :imported-members:

Units
-----

.. automodule:: measurement.utils
  :members:
  :undoc-members:
  :imported-members:
