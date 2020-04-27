import decimal
from typing import List, Optional, Type

from measurement.base import AbstractMeasure


def guess(value: decimal.Decimal, unit: str, measures: Optional[List[Type[AbstractMeasure]]] = None) -> AbstractMeasure:
    """
    Return measurement instance based on given unit.

    Raises:
        ValueError: If measurement type cannot be guessed.

    Returns:
        AbstractMeasure: Measurement instance based on given unit.

    """
    all_measures: List[Type[AbstractMeasure]] = measures or AbstractMeasure.__subclasses__()

    for measure in all_measures:
        try:
            return measure(value=None, unit=None, **{unit: value})
        except KeyError:
            pass
    raise ValueError(f"can't guess measure for '{value} {unit}'")
