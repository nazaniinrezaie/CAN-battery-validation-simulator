# System Requirements — Battery CAN Validation

## SYS-001 — Undervoltage Detection

The system shall detect an UNDERVOLTAGE fault when the measured battery voltage is below 300.0 V.

### Verification Method
Automated testing using Boundary Value Analysis.

| Test ID | Input Voltage | Expected Result |
|---|---|---|
| TC-UV-001 | 299.9 V | UNDERVOLTAGE detected |
| TC-UV-002 | 300.0 V | No UNDERVOLTAGE detected |
| TC-UV-003 | 300.1 V | No UNDERVOLTAGE detected |


### Verification Result

- Test framework: pytest
- Test file: tests/test_voltage.py
- Tests executed: 3
- Tests passed: 3
- Tests failed: 0
- Status: PASSED

## SYS-002 — Overcurrent Detection

The system shall detect an OVERCURRENT fault when
the measured battery current exceeds 100.0 A.

### Verification Method

Automated testing using Boundary Value Analysis.

| Test ID | Input Current | Expected Result |
|---|---|---|
| TC-OC-001 | 99.9 A | No OVERCURRENT detected |
| TC-OC-002 | 100.0 A | No OVERCURRENT detected |
| TC-OC-003 | 100.1 A | OVERCURRENT detected |

### Verification Result

- Test framework: pytest
- Test file: tests/test_current.py
- Tests executed: 3
- Tests passed: 3
- Tests failed: 0
- Status: PASSED

## SYS-003 — Overtemperature Detection

The system shall detect an OVERTEMPERATURE fault
when the measured battery temperature exceeds 60.0°C.

### Verification Method

Automated testing using Boundary Value Analysis.

| Test ID | Input Temperature | Expected Result |
|---|---|---|
| TC-TEMP-001 | 59.9°C | No OVERTEMPERATURE |
| TC-TEMP-002 | 60.0°C | No OVERTEMPERATURE |
| TC-TEMP-003 | 60.1°C | OVERTEMPERATURE detected |

### Verification Result

- Test framework: pytest
- Test file: tests/test_temperature.py
- Tests executed: 3
- Tests passed: 3
- Tests failed: 0
- Status: PASSED

## SYS-004 — Low SOC Detection

The system shall detect a LOW_SOC fault when
the battery State of Charge (SOC) is below 10%.

### Verification Method

Automated testing using Boundary Value Analysis.

| Test ID | Input SOC | Expected Result |
|---|---|---|
| TC-SOC-001 | 9.9% | LOW_SOC detected |
| TC-SOC-002 | 10.0% | No LOW_SOC detected |
| TC-SOC-003 | 10.1% | No LOW_SOC detected |

### Verification Result

- Test framework: pytest
- Test file: tests/test_soc.py
- Tests executed: 3
- Tests passed: 3
- Tests failed: 0
- Status: PASSED
