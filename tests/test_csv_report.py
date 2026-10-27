
import csv
from pathlib import Path

def test_csv_required_columns():
    csv_path = (
        Path(__file__).resolve().parents[1]
        / "logs"
        / "test_log.csv"
    )

    with open(csv_path, newline="") as file:
        reader = csv.DictReader(file)

        required_columns = {
            "timestamp",
            "test_id",
            "scenario",
            "status",
            "expected_result",
            "expected_fault",
        }

        assert required_columns.issubset(
            set(reader.fieldnames or [])
        ), "CSV report is missing required columns"

def test_unique_test_ids():
    csv_path = (
        Path(__file__).resolve().parents[1]
        / "logs"
        / "test_log.csv"
    )

    with open(csv_path, newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    # The same test ID can appear in different runs.
    # Check duplicates within the same timestamp.
    test_keys = [
        (row["timestamp"], row["test_id"])
        for row in rows
    ]

    assert len(test_keys) == len(set(test_keys)), (
        "Duplicate test IDs found within the same run"
    )

def test_csv_valid_status_values():
    csv_path = (
        Path(__file__).resolve().parents[1]
        / "logs"
        / "test_log.csv"
    )

    with open(csv_path, newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    assert rows, "CSV report is empty"

    valid_values = {"PASS", "FAIL"}

    for row in rows:
        assert row["status"] in valid_values, (
            f"Invalid status for {row['test_id']}"
        )

        assert row["expected_result"] in valid_values, (
            f"Invalid expected result for {row['test_id']}"
        )
