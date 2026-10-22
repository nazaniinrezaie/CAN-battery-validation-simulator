
import pytest
from src.can_receiver import (
    decode_battery_status_message,
    decode_battery_thermal_message,
    decode_battery_soc_message,
    decode_battery_fault_message,
)

def test_decode_battery_status():
    message = {
        "signals": {
            "voltage": 3805,
            "current": 253
        }
    }

    values = decode_battery_status_message(message)

    assert values == (380.5, 25.3)


def test_decode_battery_thermal():
    message = {
        "signals": {
            "temperature": 327
        }
    }

    values = decode_battery_thermal_message(message)

    assert values == pytest.approx(32.7)

def test_decode_battery_soc():
    message = {
        "signals": {
            "soc": 80
        }
    }

    values = decode_battery_soc_message(message)

    assert values == (80)

def test_decode_battery_fault():
    message = {
        "signals": {
            "fault_code": 2
        }
    }

    values = decode_battery_fault_message(message)

    assert values == "OVERCURRENT"

def test_unknown_fault():
    message = {
        "signals": {
            "fault_code": 99
        }
    }

    values = decode_battery_fault_message(message)

    assert values == "UNKNOWN_FAULT"