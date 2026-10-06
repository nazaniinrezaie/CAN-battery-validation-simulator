import subprocess
import sys
from pathlib import Path
import csv
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent

TEST_CASES = [
    {
        "id": "TC_001",
        "scenario": "normal",
        "expected_result": "PASS",
        "expected_fault": None
    },
    {
        "id": "TC_002",
        "scenario": "undervoltage",
        "expected_result": "FAIL",
        "expected_fault": "UNDERVOLTAGE"
    },
    {
        "id": "TC_003",
        "scenario": "overcurrent",
        "expected_result": "FAIL",
        "expected_fault": "OVERCURRENT"
    },
    {
        "id": "TC_004",
        "scenario": "overtemperature",
        "expected_result": "FAIL",
        "expected_fault": "OVERTEMPERATURE"
    },
    {
        "id": "TC_005",
        "scenario": "low_soc",
        "expected_result": "FAIL",
        "expected_fault": "LOW_SOC"
    }
]


def run_test_case(test_case):
    scenario = test_case["scenario"]

    result = subprocess.run(
        [sys.executable, str(BASE_DIR / "can_receiver.py"), scenario],
        capture_output=True,
        text=True
    )

    output = result.stdout

    expected_result = test_case["expected_result"]
    expected_fault = test_case["expected_fault"]

    result_matches = f"\n{expected_result}\n" in output and result.returncode == 0

    if expected_fault is None:
        fault_matches = "detected" not in output
    else:
        fault_matches = expected_fault in output

    test_passed = result_matches and fault_matches

    return test_passed, output


def generate_test_report(test_results, passed_tests, total_tests):
    report_path = BASE_DIR / "reports" / "test_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    overall_result = "PASS" if passed_tests == total_tests else "FAIL"

    with open(report_path, "w") as report_file:
        report_file.write("# Battery CAN Validation Test Report\n\n")
        report_file.write(f"Generated at: {now}\n\n")

        report_file.write("## Test Results\n\n")
        report_file.write("| Test ID | Scenario | Result |\n")
        report_file.write("|---|---|---|\n")

        for result in test_results:
            report_file.write(
                f"| {result['id']} | {result['scenario']} | {result['status']} |\n"
            )

        report_file.write("\n## Summary\n\n")
        report_file.write(f"Passed tests: {passed_tests}/{total_tests}\n\n")
        report_file.write(f"Overall Result: {overall_result}\n")

    return report_path


def generate_csv_log(test_results):
    log_path = BASE_DIR / "logs" / "test_log.csv"
    log_path.parent.mkdir(parents=True, exist_ok=True)

    with open(log_path, "w", newline="") as log_file:
        fieldnames = [
            "timestamp",
            "test_id",
            "scenario",
            "status",
            "expected_result",
            "expected_fault"
        ]

        writer = csv.DictWriter(log_file, fieldnames=fieldnames)

        writer.writeheader()

        for result in test_results:
            writer.writerow(
                {
                    "timestamp": result["timestamp"],
                    "test_id": result["id"],
                    "scenario": result["scenario"],
                    "status": result["status"],
                    "expected_result": result["expected_result"],
                    "expected_fault": result["expected_fault"] or ""
                }
            )

    return log_path


def main():
    print("Starting Automated Battery CAN Validation Tests...\n")

    total_tests = len(TEST_CASES)
    passed_tests = 0
    test_results = []

    for test_case in TEST_CASES:
        test_passed, output = run_test_case(test_case)

        if test_passed:
            passed_tests += 1
            status = "PASS"
        else:
            status = "FAIL"

        test_results.append(
            {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "id": test_case["id"],
                "scenario": test_case["scenario"],
                "status": status,
                "expected_result": test_case["expected_result"],
                "expected_fault": test_case["expected_fault"],
                "output": output
            }
        )

        print(f"{test_case['id']} - {test_case['scenario']}: {status}")

    print("\nTest Summary:")
    print(f"{passed_tests}/{total_tests} test cases passed")

    if passed_tests == total_tests:
        print("Overall Result: PASS")
    else:
        print("Overall Result: FAIL")

    report_path = generate_test_report(test_results, passed_tests, total_tests)
    log_path = generate_csv_log(test_results)

    print(f"\nTest report generated: {report_path}")
    print(f"CSV log generated: {log_path}")


if __name__ == "__main__":
    main()