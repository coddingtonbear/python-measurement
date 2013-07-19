
Using Measurement Objects
=========================

You can import any of the above measures from `measurement.measures` 
and use it for easily handling measurements like so::

    from measurement.measures import Weight

    w = Weight(lb=135) # Represents 135lbs
    print w
    >> '135.0 lb'
    print w.kg
    >> 61.234919999999995

You can create a measurement unit using any compatible unit and can transform
it into any compatible unit.  See :doc:`measures` for information about which
units are supported by which measures.


Guessing Measurements
=====================

If you happen to be in a situation where you are processing a list of
value/unit pairs (like you might find at the beginning of a recipe), you can
use the `guess` function to give you a measurement object.::

    from measurement.utils import guess

    m = guess(10, 'mg')

    print repr(m)
    >> 'Weight(g=10.0)'

By default, this will check all built-in measures, and will return the first
measure having an appropriate unit.  You may want to constrain the list of
measures checked (or check your own measurement classes, too) to make sure
that your measurement is not mis-guessed, and you can do that by specifying
the ``measures`` keyword argument::

    from measurement.utils import guess
    from measurement.measures import Distance, Temperature, Volume

    m = guess(24, 'f', measures=[Distance, Volume, Temperature])
    
    print repr(m)
    >> 'Temperature(f=24)'

If no match is found, a ``ValueError`` exception will be raised::

    m = guess(24, 'f', measures=[Distance, Volume])
    >> Traceback (most recent call last):
    >>   File "<stdin>", line 1, in <module>
    >>   File "measurement/utils.py", line 61, in guess
    >>     ', '.join([m.__name__ for m in measures])
    >> ValueError: No valid measure found for 24 f; checked Distance, Volume

