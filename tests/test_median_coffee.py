import pytest
from reports.median_coffee import MedianCoffeeReport

def test_report():
    rows = [
                {"student": "A", "coffee_spent": "100"},
                {"student": "A", "coffee_spent": "300"},
                {"student": "B", "coffee_spent": "200"},
                {"student": "B", "coffee_spent": "400"},
            ]
    report = MedianCoffeeReport()
    result = report.generate(rows)

    assert result == [('B', 300.0), ('A', 200.0)]

def test_one_student():
    rows = [
        {"student": "A", "coffee_spent": "100"},
        {"student": "A", "coffee_spent": "200"},
    ]

    report = MedianCoffeeReport()
    result = report.generate(rows)

    assert result == [('A', 150.0)]

def test_same_students():
    rows = [
        {"student": "A", "coffee_spent": "100"},
        {"student": "A", "coffee_spent": "200"},
        {"student": "B", "coffee_spent": "150"},
        {"student": "B", "coffee_spent": "150"},
    ]

    report = MedianCoffeeReport()
    result = report.generate(rows)

    assert result == [('A', 150.0), ('B', 150.0)]

def test_empty_rows():
    report = MedianCoffeeReport()
    result = report.generate([])

    assert result == []