
import pytest

from src.battery_ecu_simulator import (
    create_battery_status_message,
    create_battery_thermal_message,
)

from src.can_receiver import (
    decode_battery_status_message,
    decode_battery_thermal_message,
    check_faults,
)


def test_undervoltage_integration():
    # Step 1: Create CAN message
    message = create_battery_status_message(299.9, 25.0)

    # Step 2: Decode message
    voltage, current = decode_battery_status_message(message)

    # Step 3: Check faults
    faults = check_faults(voltage, current, 30.0, 80)

    # Step 4: Verify results
    assert voltage == pytest.approx(299.9)
    assert current == pytest.approx(25.0)
    assert "UNDERVOLTAGE" in faults


def test_overtemperature_integration():
    # Step 1: Create CAN message
    message = create_battery_thermal_message(60.1)

    # Step 2: Decode message
    temperature = decode_battery_thermal_message(message)

    # Step 3: Check faults
    faults = check_faults(380.0, 25.0, temperature, 80)

    # Step 4: Verify results
    assert temperature == pytest.approx(60.1)
    assert "OVERTEMPERATURE" in faults

def test_multiple_faults_integration():
    # Create simulated CAN messages
    status_message = create_battery_status_message(299.9, 25.0)
    thermal_message = create_battery_thermal_message(60.1)

    # Decode both messages
    voltage, current = decode_battery_status_message(status_message)
    temperature = decode_battery_thermal_message(thermal_message)

    # Check faults
    faults = check_faults(voltage, current, temperature, 80)

    # Verify both faults are detected
    assert "UNDERVOLTAGE" in faults
    assert "OVERTEMPERATURE" in faults

    # Verify no unexpected faults
    assert len(faults) == 2
