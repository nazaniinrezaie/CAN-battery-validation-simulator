import csv

with open("logs/test_log.csv", "r") as file:
    reader = csv.DictReader(file)
    tests = list(reader)

passed = 0

for test in tests:
    if test["status"] == "PASS":
        passed += 1

print("Total tests:", len(tests))
print("Passed tests:", passed)
print("Failed tests:", len(tests) - passed)

print("\nBattery fault scenarios:")

for test in tests:
    if test["expected_fault"]:
        print(test["test_id"], "-", test["expected_fault"])