import argparse
from tabulate import tabulate
from services.csv_reader import read_csv
import reports.median_coffee
from reports.base import Report
from reports.registry import REPORTS, get_report

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Генерирует отчет из CSV файла"
    )
    parser.add_argument("-f",
                        "--files",
                        type=str,
                        nargs="+",
                        required=True,
                        help="CSV файлы для обработки"
                    )
    parser.add_argument("-r",
                        "--report", 
                        type=str,
                        required=False,
                        choices=REPORTS.keys(),
                        default="median",
                        help="Тип отчета для генерации"
                        )
    
    return parser.parse_args()
    
def main():
    args = parse_args()

    rows: list[dict[str, str]] = []
    for file_path in args.files:
        try:
            rows.extend(read_csv(file_path))
        except FileNotFoundError:
            print(f"Файл не найден: {file_path}")
            return

    report = get_report(args.report)
    
    generated_report = report.generate(rows)
    
    table = tabulate(
            generated_report,
            headers=["Студент", "Траты на кофе"],
            tablefmt="github")
    
    print(table)

if __name__ == '__main__':
    main()