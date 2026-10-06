# Battery CAN Validation Simulator

A Python learning project that models battery ECU signals and checks fault-detection logic across five scenarios. It represents CAN messages as Python dictionaries with CAN ID labels; it does **not** transmit frames on a physical or virtual CAN bus.

## What it covers

- Simulated battery voltage, current, temperature, state of charge (SOC), fault code, and heartbeat messages.
- Receiver-side decoding and threshold checks.
- Five scenarios: normal operation, undervoltage, overcurrent, overtemperature, and low SOC.
- Automated comparison of observed results with expected outcomes, plus a Markdown report and CSV test log.

## Run locally

Requires Python 3.8+; the three scripts below use only the Python standard library. From the repository folder:

```bash
python3 test_runner.py
```

The runner prints a summary and creates `reports/test_report.md` and `logs/test_log.csv`. A passing test case means the observed output matched its expected outcome; fault scenarios correctly produce a **FAIL** validation result in the receiver.

To inspect one scenario:

```bash
python3 can_receiver.py normal
python3 can_receiver.py overtemperature
```

To print continuously generated simulated messages (stop with Ctrl+C):

```bash
python3 battery_ecu_simulator.py
```

## Scenario expectations

| Scenario | Signal outside limit | Expected receiver result |
| --- | --- | --- |
| normal | None | PASS |
| undervoltage | Voltage below 300 V | FAIL, UNDERVOLTAGE |
| overcurrent | Current above 100 A | FAIL, OVERCURRENT |
| overtemperature | Temperature above 60 °C | FAIL, OVERTEMPERATURE |
| low_soc | SOC below 10% | FAIL, LOW_SOC |

## Files

- `battery_ecu_simulator.py`: creates labelled battery message dictionaries and prints a continuous nominal stream.
- `can_receiver.py`: creates each scenario, decodes signals, and checks limits.
- `test_runner.py`: runs all five receiver scenarios and writes report files.

This is a software simulation for demonstrating test design and verification logic; no CAN interface or external hardware is required.
