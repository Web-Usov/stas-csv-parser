import csv

def read_csv(file_path: str) -> list[dict[str, str]]:
    with open(file_path, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        
        return [
            {key: value.strip() for key, value in row.items()}
            for row in reader
        ]