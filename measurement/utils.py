import inspect
import sys

if sys.version_info >= (2, 7, 2):
    from functools import total_ordering
else:
    # For Python < 2.7.2. Python 2.6 does not have total_ordering, and
    # total_ordering in 2.7 versions prior to 2.7.2 is buggy. See
    # http://bugs.python.org/issue10042 for details. For these versions use
    # code borrowed from Python 2.7.3.
    def total_ordering(cls):
        """Fill in missing ordering methods."""
        convert = {
            "__lt__": [
                ("__gt__", lambda self, other: not (self < other or self == other)),
                ("__le__", lambda self, other: self < other or self == other),
                ("__ge__", lambda self, other: not self < other),
            ],
            "__le__": [
                ("__ge__", lambda self, other: not self <= other or self == other),
                ("__lt__", lambda self, other: self <= other and not self == other),
                ("__gt__", lambda self, other: not self <= other),
            ],
            "__gt__": [
                ("__lt__", lambda self, other: not (self > other or self == other)),
                ("__ge__", lambda self, other: self > other or self == other),
                ("__le__", lambda self, other: not self > other),
            ],
            "__ge__": [
                ("__le__", lambda self, other: (not self >= other) or self == other),
                ("__gt__", lambda self, other: self >= other and not self == other),
                ("__lt__", lambda self, other: not self >= other),
            ],
        }
        roots = set(dir(cls)) & set(convert)
        if not roots:
            raise ValueError("must define at least one ordering operation: < > <= >=")
        root = max(roots)  # prefer __lt__ to __le__ to __gt__ to __ge__
        for opname, opfunc in convert[root]:
            if opname not in roots:
                opfunc.__name__ = opname
                opfunc.__doc__ = getattr(int, opname).__doc__
                setattr(cls, opname, opfunc)
        return cls


def get_all_measures():
    from measurement import measures

    m = []
    for name, obj in inspect.getmembers(measures):
        if inspect.isclass(obj):
            m.append(obj)
    return m


def guess(value, unit, measures=None):
    if measures is None:
        measures = get_all_measures()
    for measure in measures:
        try:
            return measure(**{unit: value})
        except AttributeError:
            pass
    raise ValueError(
        "No valid measure found for %s %s; checked %s"
        % (value, unit, ", ".join([m.__name__ for m in measures]))
    )
