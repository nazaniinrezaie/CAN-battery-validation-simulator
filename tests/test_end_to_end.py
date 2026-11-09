
import subprocess
import csv
from pathlib import Path


def test_full_validation_workflow():
    # Step 1: Run the complete test runner
    result = subprocess.run(
        ["python3", "src/test_runner.py"],
        capture_output=True,
        text=True,
        timeout=30
    )

    # Step 2: Verify successful execution
    assert result.returncode == 0
    assert "5/5 test cases passed" in result.stdout

    # Step 3: Verify report files exist
    report_path = Path("reports/test_report.md")
    csv_path = Path("logs/test_log.csv")

    assert report_path.exists()
    assert csv_path.exists()

    # Step 4: Verify report content
    report = report_path.read_text()

    assert "Passed tests: 5/5" in report
    assert "Overall Result: PASS" in report

    # Step 5: Validate CSV test records
    with csv_path.open(newline="") as csv_file:
        rows = list(csv.DictReader(csv_file))

    # Verify exactly five test records
    assert len(rows) == 5

    # Verify all expected test IDs are present
    expected_ids = {
        "TC_001",
        "TC_002",
        "TC_003",
        "TC_004",
        "TC_005",
    }

    actual_ids = {row["test_id"] for row in rows}

    assert actual_ids == expected_ids

    # Verify every test passed
    assert all(row["status"] == "PASS" for row in rows)
