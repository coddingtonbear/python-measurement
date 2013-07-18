# Copyright (c) 2007, Robert Coup <robert.coup@onetrackmind.co.nz>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#
#   2. Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#
#   3. Neither the name of Distance nor the names of its contributors may be used
#      to endorse or promote products derived from this software without
#      specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
from decimal import Decimal

import six
import sympy
from sympy.solvers import solve_linear

from measurement.utils import total_ordering


NUMERIC_TYPES = six.integer_types + (float, Decimal)


def pretty_name(obj):
    return obj.__name__ if obj.__class__ == type else obj.__class__.__name__


@total_ordering
class MeasureBase(object):
    STANDARD_UNIT = None
    ALIAS = {}
    UNITS = {}
    LALIAS = {}

    def __init__(self, default_unit=None, **kwargs):
        value, self._default_unit = self.default_units(kwargs)
        setattr(self, self.STANDARD_UNIT, value)
        if default_unit and isinstance(default_unit, six.string_types):
            self._default_unit = default_unit

    def _get_standard(self):
        return getattr(self, self.STANDARD_UNIT)

    def _set_standard(self, value):
        setattr(self, self.STANDARD_UNIT, value)

    standard = property(_get_standard, _set_standard)

    def __getattr__(self, name):
        if name in self.UNITS:
            return self._convert_value_to(
                self.UNITS[name],
                self.standard,
            )
        else:
            raise AttributeError('Unknown unit type: %s' % name)

    def __repr__(self):
        return '%s(%s=%s)' % (
            pretty_name(self),
            self._default_unit,
            getattr(self, self._default_unit)
        )

    def __str__(self):
        return '%s %s' % (
            getattr(self, self._default_unit),
            self._default_unit
        )

    # **** Comparison methods ****

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.standard == other.standard
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.standard < other.standard
        else:
            return NotImplemented

    # **** Operators methods ****

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(
                default_unit=self._default_unit,
                **{self.STANDARD_UNIT: (self.standard + other.standard)}
            )
        else:
            raise TypeError(
                '%(class)s must be added with %(class)s' % {
                    "class": pretty_name(self)
                }
            )

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.standard += other.standard
            return self
        else:
            raise TypeError(
                '%(class)s must be added with %(class)s' % {
                    "class": pretty_name(self)
                }
            )

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(
                default_unit=self._default_unit,
                **{self.STANDARD_UNIT: (self.standard - other.standard)}
            )
        else:
            raise TypeError(
                '%(class)s must be subtracted from %(class)s' % {
                    "class": pretty_name(self)
                }
            )

    def __isub__(self, other):
        if isinstance(other, self.__class__):
            self.standard -= other.standard
            return self
        else:
            raise TypeError(
                '%(class)s must be subtracted from %(class)s' % {
                    "class": pretty_name(self)
                }
            )

    def __mul__(self, other):
        if isinstance(other, NUMERIC_TYPES):
            return self.__class__(
                default_unit=self._default_unit,
                **{self.STANDARD_UNIT: (self.standard * other)}
            )
        else:
            raise TypeError(
                '%(class)s must be multiplied with number' % {
                    "class": pretty_name(self)
                }
            )

    def __imul__(self, other):
        if isinstance(other, NUMERIC_TYPES):
            self.standard *= float(other)
            return self
        else:
            raise TypeError(
                '%(class)s must be multiplied with number' % {
                    "class": pretty_name(self)
                }
            )

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return self.standard / other.standard
        if isinstance(other, NUMERIC_TYPES):
            return self.__class__(
                default_unit=self._default_unit,
                **{self.STANDARD_UNIT: (self.standard / other)}
            )
        else:
            raise TypeError(
                '%(class)s must be divided with number or %(class)s' % {
                    "class": pretty_name(self)
                }
            )

    def __div__(self, other):   # Python 2 compatibility
        return type(self).__truediv__(self, other)

    def __itruediv__(self, other):
        if isinstance(other, NUMERIC_TYPES):
            self.standard /= float(other)
            return self
        else:
            raise TypeError(
                '%(class)s must be divided with number' % {
                    "class": pretty_name(self)
                }
            )

    def __idiv__(self, other):  # Python 2 compatibility
        return type(self).__itruediv__(self, other)

    def __bool__(self):
        return bool(self.standard)

    def __nonzero__(self):      # Python 2 compatibility
        return type(self).__bool__(self)

    def _convert_value_to(self, unit, value):
        if not isinstance(value, float):
            value = float(value)

        if isinstance(unit, sympy.Expr):
            result = unit.evalf(
                subs={
                    self.SU: value
                }
            )
            return float(result)
        return unit / value

    def _convert_value_from(self, unit, value):
        if not isinstance(value, float):
            value = float(value)

        if isinstance(unit, sympy.Expr):
            _, result = solve_linear(unit, value)
            return result
        return unit * value

    def default_units(self, kwargs):
        """
        Return the unit value and the default units specified
        from the given keyword arguments dictionary.
        """
        val = 0.0
        default_unit = self.STANDARD_UNIT
        for unit, value in six.iteritems(kwargs):
            if unit in self.UNITS:
                val = self._convert_value_from(self.UNITS[unit], value)
                default_unit = unit
            elif unit in self.ALIAS:
                u = self.ALIAS[unit]
                val = self._convert_value_from(self.UNITS[u], value)
                default_unit = u
            else:
                lower = unit.lower()
                if lower in self.UNITS:
                    val = self._convert_value_from(self.UNITS[lower], value)
                    default_unit = lower
                elif lower in self.LALIAS:
                    u = self.LALIAS[lower]
                    val = self._convert_value_from(self.UNITS[u], value)
                    default_unit = u
                else:
                    raise AttributeError('Unknown unit type: %s' % unit)
        return val, default_unit

    @classmethod
    def unit_attname(cls, unit_str):
        """
        Retrieves the unit attribute name for the given unit string.
        For example, if the given unit string is 'metre', 'm' would be returned.
        An exception is raised if an attribute cannot be found.
        """
        lower = unit_str.lower()
        if unit_str in cls.UNITS:
            return unit_str
        elif lower in cls.UNITS:
            return lower
        elif lower in cls.LALIAS:
            return cls.LALIAS[lower]
        else:
            raise Exception(
                'Could not find a unit keyword associated with "%s"' % (
                    unit_str,
                )
            )
