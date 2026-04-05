import pytest
from main import get_report
from reports.median_coffee import MedianCoffeeReport

def test_register_report():
    from reports.registry import register_report, REPORTS
    assert "median-coffee" in REPORTS.keys()

def test_get_report():
    report = get_report("median-coffee")
    assert isinstance(report, MedianCoffeeReport)

def test_unknown_report():
    with pytest.raises(ValueError):
        get_report("unknown")