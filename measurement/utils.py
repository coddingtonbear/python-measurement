import inspect
from measurement import measures


def get_all_measures():

    m = []
    for name, obj in inspect.getmembers(measures):
        if inspect.isclass(obj):
            m.append(obj)
    return m

def guess(value, unit, measures=None, decimal=False):
    if measures is None:
        measures = get_all_measures()
    for measure in measures:
        try:
            return measure(**{unit: value}, decimal=decimal)
        except AttributeError:
            pass
    raise ValueError(
        "No valid measure found for %s %s; checked %s"
        % (value, unit, ", ".join([m.__name__ for m in measures]))
    )
