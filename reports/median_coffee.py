from statistics import median
from collections import defaultdict
from .base import Report
from .registry import register_report

@register_report("median-coffee")
class MedianCoffeeReport(Report[float]):

    def generate(self, rows: list[dict[str, str]]) -> list[tuple[str, float]]:
        data: dict[str, list[float]] = defaultdict(list)
        for row in rows:
            student = row["student"]
            coffee_spent = float(row["coffee_spent"])
            data[student].append(coffee_spent) 
        
        medians = [
                    (student, median(values)) 
                    for student, values in data.items() 
                    if values
                ]

        return sorted(medians, key=lambda x: round(x[1], 2), reverse=True)