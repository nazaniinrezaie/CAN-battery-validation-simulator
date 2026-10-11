import sys

from battery_ecu_simulator import (
    create_battery_status_message,
    create_battery_thermal_message,
    create_battery_soc_message,
    create_battery_fault_message,
    create_heartbeat_message
)


VOLTAGE_MIN = 300.0
CURRENT_MAX = 100.0
TEMPERATURE_MAX = 60.0
SOC_MIN = 10


def get_scenario_values(scenario):
    if scenario == "normal":
        return 380.5, 25.3, 32.7, 80, 0

    elif scenario == "undervoltage":
        return 250.0, 25.3, 32.7, 80, 1

    elif scenario == "overcurrent":
        return 380.5, 120.0, 32.7, 80, 2

    elif scenario == "overtemperature":
        return 380.5, 25.3, 70.0, 80, 3

    elif scenario == "low_soc":
        return 380.5, 25.3, 32.7, 5, 4

    else:
        print(f"Unknown scenario: {scenario}")
        print("Available scenarios: normal, undervoltage, overcurrent, overtemperature, low_soc")
        sys.exit(1)


def decode_battery_status_message(message):
    voltage_raw = message["signals"]["voltage"]
    current_raw = message["signals"]["current"]

    voltage = voltage_raw * 0.1
    current = current_raw * 0.1

    return voltage, current


def decode_battery_thermal_message(message):
    temperature_raw = message["signals"]["temperature"]
    temperature = temperature_raw * 0.1

    return temperature


def decode_battery_soc_message(message):
    soc = message["signals"]["soc"]

    return soc


def decode_battery_fault_message(message):
    fault_code = message["signals"]["fault_code"]

    fault_names = {
        0: "NO_FAULT",
        1: "UNDERVOLTAGE",
        2: "OVERCURRENT",
        3: "OVERTEMPERATURE",
        4: "LOW_SOC",
        5: "CAN_TIMEOUT"
    }

    return fault_names.get(fault_code, "UNKNOWN_FAULT")


def decode_heartbeat_message(message):
    alive_counter = message["signals"]["alive_counter"]

    return alive_counter


def check_faults(voltage, current, temperature, soc):
    detected_faults = []

    if voltage < VOLTAGE_MIN:
        detected_faults.append("UNDERVOLTAGE")

    if current > CURRENT_MAX:
        detected_faults.append("OVERCURRENT")

    if temperature > TEMPERATURE_MAX:
        detected_faults.append("OVERTEMPERATURE")

    if soc < SOC_MIN:
        detected_faults.append("LOW_SOC")

    return detected_faults


def main():
    if len(sys.argv) > 1:
        scenario = sys.argv[1]
    else:
        scenario = "normal"

    voltage, current, temperature, soc, fault_code = get_scenario_values(scenario)
    alive_counter = 1

    messages = [
        create_battery_status_message(voltage, current),
        create_battery_thermal_message(temperature),
        create_battery_soc_message(soc),
        create_battery_fault_message(fault_code),
        create_heartbeat_message(alive_counter)
    ]

    print("Starting CAN Receiver with Fault Injection...")
    print(f"Scenario: {scenario}\n")

    decoded_voltage = None
    decoded_current = None
    decoded_temperature = None
    decoded_soc = None
    decoded_fault = None
    decoded_alive_counter = None

    for message in messages:
        can_id = message["can_id"]

        if can_id == "0x100":
            decoded_voltage, decoded_current = decode_battery_status_message(message)
            print(f"Battery_Status: Voltage={decoded_voltage:.1f} V, Current={decoded_current:.1f} A")

        elif can_id == "0x101":
            decoded_temperature = decode_battery_thermal_message(message)
            print(f"Battery_Thermal: Temperature={decoded_temperature:.1f} C")

        elif can_id == "0x102":
            decoded_soc = decode_battery_soc_message(message)
            print(f"Battery_SOC: SOC={decoded_soc}%")

        elif can_id == "0x103":
            decoded_fault = decode_battery_fault_message(message)
            print(f"Battery_Fault Message: {decoded_fault}")

        elif can_id == "0x700":
            decoded_alive_counter = decode_heartbeat_message(message)
            print(f"Battery_Heartbeat: Alive Counter={decoded_alive_counter}")

    detected_faults = check_faults(
        decoded_voltage,
        decoded_current,
        decoded_temperature,
        decoded_soc
    )

    print("\nValidation Result:")

    if detected_faults:
        print("FAIL")
        for fault in detected_faults:
            print(f"- {fault} detected")
    else:
        print("PASS")
        print("- All battery signals are within safe limits")


if __name__ == "__main__":
    main()
