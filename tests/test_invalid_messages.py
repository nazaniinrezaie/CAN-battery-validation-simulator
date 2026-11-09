
import pytest

from src.can_receiver import (
    decode_battery_status_message,
    safe_decode_battery_status_message,
)


def test_missing_voltage():
    # Create an invalid message without voltage
    message = {
        "can_id": "0x100",
        "signals": {
            "current": 250
        }
    }

    # Verify that the original decoder raises KeyError
    with pytest.raises(KeyError, match="voltage"):
        decode_battery_status_message(message)


def test_safe_decoder_valid_message():
    # Create a valid CAN message
    message = {
        "can_id": "0x100",
        "signals": {
            "voltage": 3805,
            "current": 250
        }
    }

    # Decode using the safe decoder
    result = safe_decode_battery_status_message(message)

    # Verify successful decoding
    assert result["status"] == "OK"
    assert result["voltage"] == pytest.approx(380.5)
    assert result["current"] == pytest.approx(25.0)


def test_safe_decoder_missing_voltage():
    # Create an invalid message without voltage
    message = {
        "can_id": "0x100",
        "signals": {
            "current": 250
        }
    }

    # Decode using the safe decoder
    result = safe_decode_battery_status_message(message)

    # Verify the invalid message is handled
    assert result["status"] == "INVALID_MESSAGE"
    assert "voltage" in result["error"]

