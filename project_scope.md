# CAN-Based Battery Test Automation Simulator

## Project Goal

This project simulates a CAN-based Battery ECU and develops a Python-based validation tool for monitoring battery signals, injecting fault scenarios, detecting abnormal behavior, logging CAN messages and generating pass/fail test results.

## System Components

1. Battery ECU Simulator
   - Generates simulated CAN messages for battery voltage, current, temperature, SOC, fault status and heartbeat.

2. CAN Receiver / Validation Tool
   - Receives and decodes CAN messages.
   - Checks signal values against defined thresholds.
   - Detects undervoltage, overcurrent, overtemperature and CAN timeout.

3. Test Reporting
   - Logs CAN messages and test results.
   - Generates pass/fail reports for each scenario.

## Fault Scenarios

| Scenario | Description |
|---|---|
| normal | Battery signals remain within safe operating limits |
| undervoltage | Battery voltage drops below the defined safe threshold |
| overcurrent | Battery current rises above the defined safe threshold |
| overtemperature | Battery temperature rises above the defined safe threshold |
| can_timeout | Heartbeat messages stop for longer than the allowed timeout |

## Signal Thresholds

| Signal | Normal Range | Fault Condition |
|---|---|---|
| Voltage | 320V to 420V | Voltage < 300V |
| Current | 0A to 80A | Current > 100A |
| Temperature | 20°C to 45°C | Temperature > 60°C |
| SOC | 20% to 100% | SOC < 10% |
| Heartbeat | Every 100ms | Missing for more than 500ms |