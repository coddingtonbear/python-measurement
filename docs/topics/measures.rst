Measures
========

This application provides the following measures:

.. note::
   Python has restrictions on what can be used as a method attribute; if you
   are not very familiar with python, the below chart outlines which
   units can be used only when creating a new measurement object ('Acceptable
   as Arguments') and which are acceptable for use either when creating a
   new measurement object, or for converting a measurement object to a
   different unit ('Acceptable as Arguments or Attributes')

   Units that are acceptable as arguments (like the distance measurement 
   term ``km``) can be used like::

      >>> from measurement.measures import Distance
      >>> distance = Distance(km=10)

   or can be used for converting other measures into kilometers:

      >>> from measurement.measures import Distance
      >>> distance = Distance(mi=10).km

   but units that are only acceptable as arguments (like the distance
   measurement term ``kilometer``) can *only* be used to create a measurement:

      >>> from measurement.measures import Distance
      >>> distance = Distance(kilometer=10)

   You also might notice that some measures have arguments having spaces in
   their name marked as 'Acceptable as Arguments'; their primary use is for
   when using ``measurement.guess``::

      >>> from measurement.utils import guess
      >>> unit = 'U.S. Foot'
      >>> value = 10
      >>> measurement = guess(value, unit)
      >>> print measurement
      10.0 U.S. Foot


Area
----

* *Acceptable as Arguments or Attributes*: ``sq_Em``, ``sq_Gm``, ``sq_Mm``, ``sq_Pm``, ``sq_Tm``, ``sq_Ym``, ``sq_Zm``, ``sq_am``, ``sq_british_chain_benoit``, ``sq_british_chain_sears_truncated``, ``sq_british_chain_sears``, ``sq_british_ft``, ``sq_british_yd``, ``sq_chain_benoit``, ``sq_chain_sears``, ``sq_chain``, ``sq_clarke_ft``, ``sq_clarke_link``, ``sq_cm``, ``sq_dam``, ``sq_dm``, ``sq_fathom``, ``sq_fm``, ``sq_ft``, ``sq_german_m``, ``sq_gold_coast_ft``, ``sq_hm``, ``sq_inch``, ``sq_indian_yd``, ``sq_km``, ``sq_link_benoit``, ``sq_link_sears``, ``sq_link``, ``sq_m``, ``sq_mi``, ``sq_mm``, ``sq_nm_uk``, ``sq_nm``, ``sq_pm``, ``sq_rod``, ``sq_sears_yd``, ``sq_survey_ft``, ``sq_um``, ``sq_yd``, ``sq_ym``, ``sq_zm``
* *Acceptable as Arguments*: ``British chain (Benoit 1895 B)``, ``British chain (Sears 1922 truncated)``, ``British chain (Sears 1922)``, ``British foot (Sears 1922)``, ``British foot``, ``British yard (Sears 1922)``, ``British yard``, ``Chain (Benoit)``, ``Chain (Sears)``, ``Clarke's Foot``, ``Clarke's link``, ``Foot (International)``, ``German legal metre``, ``Gold Coast foot``, ``Indian yard``, ``Link (Benoit)``, ``Link (Sears)``, ``Nautical Mile (UK)``, ``Nautical Mile``, ``U.S. Foot``, ``US survey foot``, ``Yard (Indian)``, ``Yard (Sears)``, ``attometer``, ``attometre``, ``centimeter``, ``centimetre``, ``decameter``, ``decametre``, ``decimeter``, ``decimetre``, ``exameter``, ``exametre``, ``femtometer``, ``femtometre``, ``foot``, ``gigameter``, ``gigametre``, ``hectometer``, ``hectometre``, ``in``, ``inches``, ``kilometer``, ``kilometre``, ``megameter``, ``megametre``, ``meter``, ``metre``, ``micrometer``, ``micrometre``, ``mile``, ``millimeter``, ``millimetre``, ``nanometer``, ``nanometre``, ``petameter``, ``petametre``, ``picometer``, ``picometre``, ``terameter``, ``terametre``, ``yard``, ``yoctometer``, ``yoctometre``, ``yottameter``, ``yottametre``, ``zeptometer``, ``zeptometre``, ``zetameter``, ``zetametre``

Distance
--------

* *Acceptable as Arguments or Attributes*: ``Em``, ``Gm``, ``Mm``, ``Pm``, ``Tm``, ``Ym``, ``Zm``, ``am``, ``british_chain_benoit``, ``british_chain_sears_truncated``, ``british_chain_sears``, ``british_ft``, ``british_yd``, ``chain_benoit``, ``chain_sears``, ``chain``, ``clarke_ft``, ``clarke_link``, ``cm``, ``dam``, ``dm``, ``fathom``, ``fm``, ``ft``, ``german_m``, ``gold_coast_ft``, ``hm``, ``inch``, ``indian_yd``, ``km``, ``link_benoit``, ``link_sears``, ``link``, ``m``, ``mi``, ``mm``, ``nm_uk``, ``nm``, ``pm``, ``rod``, ``sears_yd``, ``survey_ft``, ``um``, ``yd``, ``ym``, ``zm``
* *Acceptable as Arguments*: ``British chain (Benoit 1895 B)``, ``British chain (Sears 1922 truncated)``, ``British chain (Sears 1922)``, ``British foot (Sears 1922)``, ``British foot``, ``British yard (Sears 1922)``, ``British yard``, ``Chain (Benoit)``, ``Chain (Sears)``, ``Clarke's Foot``, ``Clarke's link``, ``Foot (International)``, ``German legal metre``, ``Gold Coast foot``, ``Indian yard``, ``Link (Benoit)``, ``Link (Sears)``, ``Nautical Mile (UK)``, ``Nautical Mile``, ``U.S. Foot``, ``US survey foot``, ``Yard (Indian)``, ``Yard (Sears)``, ``attometer``, ``attometre``, ``centimeter``, ``centimetre``, ``decameter``, ``decametre``, ``decimeter``, ``decimetre``, ``exameter``, ``exametre``, ``femtometer``, ``femtometre``, ``foot``, ``gigameter``, ``gigametre``, ``hectometer``, ``hectometre``, ``inches``, ``kilometer``, ``kilometre``, ``megameter``, ``megametre``, ``meter``, ``metre``, ``micrometer``, ``micrometre``, ``mile``, ``millimeter``, ``millimetre``, ``nanometer``, ``nanometre``, ``petameter``, ``petametre``, ``picometer``, ``picometre``, ``terameter``, ``terametre``, ``yard``, ``yoctometer``, ``yoctometre``, ``yottameter``, ``yottametre``, ``zeptometer``, ``zeptometre``, ``zetameter``, ``zetametre``

Energy
------

* *Acceptable as Arguments or Attributes*: ``C``, ``EJ``, ``Ec``, ``GJ``, ``Gc``, ``J``, ``MJ``, ``Mc``, ``PJ``, ``Pc``, ``TJ``, ``Tc``, ``YJ``, ``Yc``, ``ZJ``, ``Zc``, ``aJ``, ``ac``, ``cJ``, ``c``, ``cc``, ``dJ``, ``daJ``, ``dac``, ``dc``, ``fJ``, ``fc``, ``hJ``, ``hc``, ``kJ``, ``kc``, ``mJ``, ``mc``, ``nJ``, ``nc``, ``pJ``, ``pc``, ``uJ``, ``uc``, ``yJ``, ``yc``, ``zJ``, ``zc``
* *Acceptable as Arguments*: ``Calorie``, ``attocalorie``, ``attojoule``, ``calorie``, ``centicalorie``, ``centijoule``, ``decacalorie``, ``decajoule``, ``decicalorie``, ``decijoule``, ``exacalorie``, ``exajoule``, ``femtocalorie``, ``femtojoule``, ``gigacalorie``, ``gigajoule``, ``hectocalorie``, ``hectojoule``, ``joule``, ``kilocalorie``, ``kilojoule``, ``megacalorie``, ``megajoule``, ``microcalorie``, ``microjoule``, ``millicalorie``, ``millijoule``, ``nanocalorie``, ``nanojoule``, ``petacalorie``, ``petajoule``, ``picocalorie``, ``picojoule``, ``teracalorie``, ``terajoule``, ``yoctocalorie``, ``yoctojoule``, ``yottacalorie``, ``yottajoule``, ``zeptocalorie``, ``zeptojoule``, ``zetacalorie``, ``zetajoule``

Speed
-----

.. note::
   This is a bi-dimensional measurement; bi-dimensional
   measures are created by finding an appropriate unit in the
   measure's primary measurement class, and an appropriate
   in the measure's reference class, and using them as a
   double-underscore-separated keyword argument (or, if
   converting to another unit, as an attribute).

   For example, to create an object representing 24 miles-per
   hour::

      >>> from measurement.measure import Speed
      >>> my_speed = Speed(mile__hour=24)
      >>> print my_speed
      24.0 mi/hr
      >>> print my_speed.km__hr
      38.624256

* *Primary Measurement*: Distance
* *Reference Measurement*: Time

Temperature
-----------

* *Acceptable as Arguments or Attributes*: ``c``, ``f``, ``k``
* *Acceptable as Arguments*: ``celsius``, ``fahrenheit``, ``kelvin``

.. warning::

   Be aware that, unlike other measures, the zero points of the Celsius
   and Farenheit scales are arbitrary and non-zero.
   
   If you attempt, for example, to calculate the average of a series of
   temperatures using ``sum``, be sure to supply your 'start' (zero)
   value as zero Kelvin (read: absolute zero) rather than zero
   degrees Celsius (which is rather warm comparatively)::

      >>> temperatures = [Temperature(c=10), Temperature(c=20)]
      >>> average = sum(temperatures, Temperature(k=0)) / len(temperatures)
      >>> print average  # The value will be shown in Kelvin by default since that is the starting unit
      288.15 k
      >>> print average.c  # But, you can easily get the Celsius value
      15.0
      >>> average.unit = 'c'  # Or, make the measurement report its value in Celsius by default
      >>> print average
      15.0 c

Time
----

* *Acceptable as Arguments or Attributes*: ``Esec``, ``Gsec``, ``Msec``, ``Psec``, ``Tsec``, ``Ysec``, ``Zsec``, ``asec``, ``csec``, ``dasec``, ``day``, ``dsec``, ``fsec``, ``hr``, ``hsec``, ``ksec``, ``min``, ``msec``, ``nsec``, ``psec``, ``sec``, ``usec``, ``ysec``, ``zsec``
* *Acceptable as Arguments*: ``attosecond``, ``centisecond``, ``day``, ``decasecond``, ``decisecond``, ``exasecond``, ``femtosecond``, ``gigasecond``, ``hectosecond``, ``hour``, ``kilosecond``, ``megasecond``, ``microsecond``, ``millisecond``, ``minute``, ``nanosecond``, ``petasecond``, ``picosecond``, ``second``, ``terasecond``, ``yoctosecond``, ``yottasecond``, ``zeptosecond``, ``zetasecond``

Volume
------

* *Acceptable as Arguments or Attributes*: ``El``, ``Gl``, ``Ml``, ``Pl``, ``Tl``, ``Yl``, ``Zl``, ``al``, ``cl``, ``acre_ft``, ``acre_in``, ``cubic_centimeter``, ``cubic_foot``, ``cubic_inch``, ``cubic_meter``, ``dal``, ``dl``, ``fl``, ``hl``, ``imperial_g``, ``imperial_oz``, ``imperial_pint``, ``imperial_qt``, ``imperial_tbsp``, ``imperial_tsp``, ``kl``, ``l``, ``mil_us_gal``, ``ml``, ``nl``, ``pl``, ``ul``, ``us_cup``, ``us_g``, ``us_oz``, ``us_pint``, ``us_qt``, ``us_tbsp``, ``us_tsp``, ``yl``, ``zl``
* *Acceptable as Arguments*: ``af``, ``acre-ft``, ``acre-in``, ``Imperial Gram``, ``Imperial Ounce``, ``Imperial Pint``, ``Imperial Quart``, ``Imperial Tablespoon``, ``Imperial Teaspoon``, ``Million US Gallons``, ``US Cup``, ``US Fluid Ounce``, ``US Gallon``, ``US Ounce``, ``US Pint``, ``US Quart``, ``US Tablespoon``, ``US Teaspoon``, ``attoliter``, ``attolitre``, ``centiliter``, ``centilitre``, ``cubic centimeter``, ``cubic foot``, ``cubic inch``, ``cubic meter``, ``decaliter``, ``decalitre``, ``deciliter``, ``decilitre``, ``exaliter``, ``exalitre``, ``femtoliter``, ``femtolitre``, ``gigaliter``, ``gigalitre``, ``hectoliter``, ``hectolitre``, ``kiloliter``, ``kilolitre``, ``liter``, ``litre``, ``megaliter``, ``megalitre``, ``microliter``, ``microlitre``, ``milliliter``, ``millilitre``, ``nanoliter``, ``nanolitre``, ``petaliter``, ``petalitre``, ``picoliter``, ``picolitre``, ``teraliter``, ``teralitre``, ``yoctoliter``, ``yoctolitre``, ``yottaliter``, ``yottalitre``, ``zeptoliter``, ``zeptolitre``, ``zetaliter``, ``zetalitre``

Weight
------

* *Acceptable as Arguments or Attributes*: ``Eg``, ``Gg``, ``Mg``, ``Pg``, ``Tg``, ``Yg``, ``Zg``, ``ag``, ``cg``, ``dag``, ``dg``, ``fg``, ``g``, ``hg``, ``kg``, ``lb``, ``long_ton``, ``mg``, ``ng``, ``oz``, ``pg``, ``short_ton``, ``stone``, ``tonne``, ``ug``, ``yg``, ``zg``
* *Acceptable as Arguments*: ``attogram``, ``centigram``, ``decagram``, ``decigram``, ``exagram``, ``femtogram``, ``gigagram``, ``gram``, ``hectogram``, ``kilogram``, ``long ton``, ``mcg``, ``megagram``, ``metric ton``, ``metric tonne``, ``microgram``, ``milligram``, ``nanogram``, ``ounce``, ``petagram``, ``picogram``, ``pound``, ``short ton``, ``teragram``, ``ton``, ``yoctogram``, ``yottagram``, ``zeptogram``, ``zetagram``

