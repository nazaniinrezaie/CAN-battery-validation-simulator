
from pathlib import Path

def test_all_requirements_in_rtm():
    project_root = Path(__file__).resolve().parents[1]

    rtm_path = (
        project_root / "docs" / "traceability_matrix.md"
    )

    content = rtm_path.read_text(encoding="utf-8")

    required_ids = [
        "SYS-001",
        "SYS-002",
        "SYS-003",
        "SYS-004",
    ]

    for requirement_id in required_ids:
        assert requirement_id in content, (
            f"Missing requirement: {requirement_id}"
        )

def test_rtm_test_files_exist():
    project_root = Path(__file__).resolve().parents[1]

    test_files = [
        "tests/test_voltage.py",
        "tests/test_current.py",
        "tests/test_temperature.py",
        "tests/test_soc.py",
    ]

    for test_file in test_files:
        file_path = project_root / test_file

        assert file_path.is_file(), (
            f"Missing test file: {test_file}"
        )

def test_rtm_linked_test_files_exist():
    project_root = Path(__file__).resolve().parents[1]
    rtm_path = project_root / "docs" / "traceability_matrix.md"

    content = rtm_path.read_text(encoding="utf-8")

    rows_checked = 0

    for line in content.splitlines():
        if not line.startswith("| SYS-"):
            continue

        columns = [col.strip() for col in line.split("|")[1:-1]]

        assert len(columns) == 4, (
            f"Invalid RTM row: {line}"
        )

        requirement_id, test_ids, test_file, status = columns

        assert test_ids, (
            f"No test cases linked to {requirement_id}"
        )

        assert (project_root / test_file).is_file(), (
            f"Missing test file for {requirement_id}: {test_file}"
        )

        rows_checked += 1

    assert rows_checked > 0, "No requirements found in RTM"
