# CAN Message Matrix

## Project: CAN-Based Battery Test Automation Simulator

This document defines the CAN messages used by the simulated Battery ECU.

## CAN Messages

| CAN ID | Message Name | Cycle Time | Signals | Description |
|---|---|---:|---|---|
| 0x100 | Battery_Status | 100 ms | voltage, current | Sends battery voltage and current |
| 0x101 | Battery_Thermal | 100 ms | temperature | Sends battery temperature |
| 0x102 | Battery_SOC | 500 ms | soc | Sends battery state of charge |
| 0x103 | Battery_Fault | 100 ms | fault_code | Sends diagnostic fault status |
| 0x700 | Battery_Heartbeat | 100 ms | alive_counter | Confirms that the Battery ECU is alive |

## Signal Scaling

| Signal | Unit | Scale | Offset | Example |
|---|---|---:|---:|---|
| voltage | V | 0.1 | 0 | 380.5 V is sent as 3805 |
| current | A | 0.1 | 0 | 25.3 A is sent as 253 |
| temperature | °C | 0.1 | 0 | 32.7 °C is sent as 327 |
| soc | % | 1 | 0 | 80% is sent as 80 |
| fault_code | - | 1 | 0 | 0 means no fault |
| alive_counter | - | 1 | 0 | Counter increases from 0 to 255 |

## Fault Codes

| Fault Code | Fault Name | Description |
|---:|---|---|
| 0 | NO_FAULT | System is operating normally |
| 1 | UNDERVOLTAGE | Battery voltage is below 300 V |
| 2 | OVERCURRENT | Battery current is above 100 A |
| 3 | OVERTEMPERATURE | Battery temperature is above 60 °C |
| 4 | LOW_SOC | Battery SOC is below 10% |
| 5 | CAN_TIMEOUT | Heartbeat message is missing for more than 500 ms |

## Message Details

### 0x100 Battery_Status

| Byte | Signal | Format |
|---:|---|---|
| 0-1 | voltage | unsigned integer, scaled by 0.1 |
| 2-3 | current | unsigned integer, scaled by 0.1 |
| 4-7 | reserved | set to 0 |

### 0x101 Battery_Thermal

| Byte | Signal | Format |
|---:|---|---|
| 0-1 | temperature | unsigned integer, scaled by 0.1 |
| 2-7 | reserved | set to 0 |

### 0x102 Battery_SOC

| Byte | Signal | Format |
|---:|---|---|
| 0 | soc | unsigned integer, 0 to 100 |
| 1-7 | reserved | set to 0 |

### 0x103 Battery_Fault

| Byte | Signal | Format |
|---:|---|---|
| 0 | fault_code | unsigned integer |
| 1-7 | reserved | set to 0 |

### 0x700 Battery_Heartbeat

| Byte | Signal | Format |
|---:|---|---|
| 0 | alive_counter | unsigned integer, 0 to 255 |
| 1-7 | reserved | set to 0 |


