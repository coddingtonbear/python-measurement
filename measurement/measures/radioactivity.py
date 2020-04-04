from measurement.base import AbstractMeasure, MetricUnit

__all__ = ["Radioactivity"]


class Radioactivity(AbstractMeasure):
    """Radioactivity measurements."""

    becquerel = MetricUnit("1", ["Bq"], ["Bq"])
    curie = MetricUnit("37000000000", ["Ci"], ["Ci"])
    rutherford = MetricUnit("1000000", ["Rd"], ["Rd"])
