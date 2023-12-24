from measurement.base import AbstractMeasure
from measurement.measures import *


class TestAllUnits:
    def test_all_units_function_as_expected(self):
        units_that_dont_work: list[str] = []

        for klass in AbstractMeasure.__subclasses__():
            base_unit: str = klass.get_base_unit_names()[0]
            measure: AbstractMeasure = klass(value=1.0, unit=base_unit)

            for unit in measure._units:
                try:
                    getattr(measure, unit)
                except AttributeError as error:
                    units_that_dont_work.append(f"{klass.__name__} => {unit}")

        error_message = "\n".join(
            [
                "Expected all units to be valid.",
                "However, the following units could not be used:",
            ]
            + units_that_dont_work
        )

        assert len(units_that_dont_work) == 0, error_message
