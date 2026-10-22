
# Battery CAN Validation Simulator

A Python-based learning project that simulates battery ECU signals and validates fault-detection logic.

The project represents CAN messages as Python dictionaries with CAN ID labels. It does not transmit frames on a physical or virtual CAN bus.

## Project Features

- Simulation of battery voltage, current, temperature, state of charge (SOC), fault codes, and heartbeat messages.
- CAN signal decoding and scaling.
- Battery fault detection using predefined thresholds.
- Five test scenarios: normal, undervoltage, overcurrent, overtemperature, and low SOC.
- Automated verification with Python and Pytest.
- Boundary-value and negative testing.
- Requirements documentation and test traceability.
- GitHub Actions continuous integration (CI).
- Automated Markdown test reports and CSV logs.

## Run Locally

The simulation scripts use the Python standard library.

Run the five battery scenarios:

```bash
python3 src/test_runner.py
```

The test runner generates:

- `reports/test_report.md`
- `logs/test_log.csv`

Run individual scenarios:

```bash
python3 src/can_receiver.py normal
python3 src/can_receiver.py overtemperature
```

Run the battery ECU simulator:

```bash
python3 src/battery_ecu_simulator.py
```

Press Ctrl+C to stop the continuous simulation.

## Automated Testing

The project includes two automated testing approaches:

### Battery Scenario Testing

Five scenarios validate the receiver's behavior against expected results.

A `FAIL` battery validation result is expected for fault scenarios and does not mean the automated test failed.

### Pytest Unit Testing

The project currently includes 23 passing Pytest tests covering:

- Fault detection and boundary conditions.
- Scenario selection.
- Invalid scenario handling.
- Battery voltage and current decoding.
- Battery temperature decoding.
- Battery SOC decoding.
- Fault-code interpretation.
- Unknown fault-code handling.

Run all Pytest tests:

```bash
python3 -m pytest tests/ -v
```

## Code Coverage

Statement coverage of `src/can_receiver.py` reached 55% in local testing, with 23 passing Pytest tests.

Install testing dependencies:

```bash
python3 -m pip install pytest pytest-cov
```

Measure coverage:

```bash
python3 -m pytest tests/ --cov=src.can_receiver --cov-report=term-missing
```

Coverage is being improved incrementally by identifying untested code and designing additional test cases.

## Continuous Integration

GitHub Actions runs automated checks on pushes and pull requests.

The CI workflow includes:

- Python environment setup.
- Execution of five battery scenario tests.
- Execution of Pytest tests.

Workflow configuration:

`.github/workflows/ci.yml`

## Scenario Expectations

| Scenario | Signal outside limit | Expected receiver result |
|---|---|---|
| normal | None | PASS |
| undervoltage | Voltage below 300 V | FAIL, UNDERVOLTAGE |
| overcurrent | Current above 100 A | FAIL, OVERCURRENT |
| overtemperature | Temperature above 60 °C | FAIL, OVERTEMPERATURE |
| low_soc | SOC below 10% | FAIL, LOW_SOC |

## Verification Documentation

The project includes:

- `docs/system_requirements.md` — battery fault-detection requirements.
- `docs/traceability_matrix.md` — mapping between system requirements and test cases.

Four documented system requirements cover undervoltage, overcurrent, overtemperature, and low SOC.

## Project Structure

```text
can-battery-test-automation/
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   ├── system_requirements.md
│   └── traceability_matrix.md
├── src/
│   ├── battery_ecu_simulator.py
│   ├── can_receiver.py
│   └── test_runner.py
├── tests/
│   ├── test_voltage.py
│   ├── test_current.py
│   ├── test_temperature.py
│   ├── test_soc.py
│   ├── test_scenarios.py
│   └── test_decoder.py
├── reports/
├── logs/
├── .gitignore
└── README.md
```

## Technologies

- Python
- Pytest
- pytest-cov
- Git and GitHub
- GitHub Actions (CI)
- CAN message simulation
- Automated software verification

## Project Scope

This is a software simulation and verification practice project.

It demonstrates test design, fault detection, signal decoding, boundary-value analysis, requirements traceability, and automated testing.

It does not use a physical CAN interface, external hardware, or real CAN bus communication.
