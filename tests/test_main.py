from main import get_report
from services.csv_reader import read_csv

def test_csv_integration(tmp_path):
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Алексей Смирнов,2024-06-01,450,4.5,12,норм,Математика\n"
    )

    rows = read_csv(csv_file)
    report = get_report("median-coffee")
    result = report.generate(rows)
    assert result == [("Алексей Смирнов", 450.0)]

def test_main_cli(monkeypatch, tmp_path, capsys):
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n" \
        "Алексей Смирнов,2024-06-01,450,4.5,12,норм,Математика\n" \
        "Алексей Смирнов,2024-06-02,500,4.0,14,устал,Математика\n" \
        "Алексей Смирнов,2024-06-03,550,3.5,16,зомби,Математика\n" \
        "Дарья Петрова,2024-06-01,200,7.0,6,отл,Математика"
    )

    import main

    monkeypatch.setattr("sys.argv", ["main.py", "-f", str(csv_file), "-r", "median-coffee"])
    main.main()
    captured = capsys.readouterr()
    assert "Алексей Смирнов" in captured.out
    assert "500" in captured.out
    assert "Дарья Петрова" in captured.out
    assert "200" in captured.out