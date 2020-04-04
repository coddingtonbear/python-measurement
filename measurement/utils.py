def guess(value, unit, measures=None):
    """
    Return measurement instance based on given unit.

    Raises:
        ValueError: If measurement type cannot be guessed.

    Returns:
        MeasureBase: Measurement instance based on given unit.

    """
    from measurement.base import AbstractMeasure

    for measure in measures or AbstractMeasure.__subclasses__():
        try:
            return measure(**{unit: value})
        except KeyError:
            pass
    raise ValueError(f"can't guess measure for '{value} {unit}'")
