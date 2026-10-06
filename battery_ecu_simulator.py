import time


def create_battery_status_message(voltage, current):
    """
    Simulates CAN ID 0x100: Battery_Status
    voltage and current are scaled by 0.1
    Example: 380.5 V -> 3805
    """

    voltage_raw = int(voltage * 10)
    current_raw = int(current * 10)

    return {
        "can_id": "0x100",
        "message_name": "Battery_Status",
        "signals": {
            "voltage": voltage_raw,
            "current": current_raw
        }
    }


def create_battery_thermal_message(temperature):
    """
    Simulates CAN ID 0x101: Battery_Thermal
    temperature is scaled by 0.1
    Example: 32.7 C -> 327
    """

    temperature_raw = int(temperature * 10)

    return {
        "can_id": "0x101",
        "message_name": "Battery_Thermal",
        "signals": {
            "temperature": temperature_raw
        }
    }


def create_battery_soc_message(soc):
    """
    Simulates CAN ID 0x102: Battery_SOC
    SOC is sent as a percentage from 0 to 100
    """

    return {
        "can_id": "0x102",
        "message_name": "Battery_SOC",
        "signals": {
            "soc": int(soc)
        }
    }


def create_battery_fault_message(fault_code):
    """
    Simulates CAN ID 0x103: Battery_Fault
    0 means NO_FAULT
    """

    return {
        "can_id": "0x103",
        "message_name": "Battery_Fault",
        "signals": {
            "fault_code": fault_code
        }
    }


def create_heartbeat_message(alive_counter):
    """
    Simulates CAN ID 0x700: Battery_Heartbeat
    alive_counter increases from 0 to 255
    """

    return {
        "can_id": "0x700",
        "message_name": "Battery_Heartbeat",
        "signals": {
            "alive_counter": alive_counter
        }
    }


def run_simulator():
    voltage = 380.5
    current = 25.3
    temperature = 32.7
    soc = 80
    fault_code = 0
    alive_counter = 0

    print("Starting Battery ECU Simulator...")
    print("Press Ctrl + C to stop.\n")

    while True:
        messages = [
            create_battery_status_message(voltage, current),
            create_battery_thermal_message(temperature),
            create_battery_soc_message(soc),
            create_battery_fault_message(fault_code),
            create_heartbeat_message(alive_counter)
        ]

        for message in messages:
            print(message)

        print("-" * 60)

        alive_counter = (alive_counter + 1) % 256

        time.sleep(1)


if __name__ == "__main__":
    run_simulator()
