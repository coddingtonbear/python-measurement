import inspect


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
