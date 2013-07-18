
Using Measurement Objects
=========================

You can import any of the above measures from `measurement.measures` 
and use it for easily handling measurements like so::

    from measurement.measures import Weight

    w = Weight(lb=135) # Represents 135lbs
    print w            # '135.0 lb'
    print w.kg         # '61.234919999999995'

