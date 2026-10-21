
from src.can_receiver import decode_battery_status_message

def test_decode_battery_status():
    message = {
        "signals": {
            "voltage": 3805,
            "current": 253
        }
    }

    values = decode_battery_status_message(message)

    assert values == (380.5, 25.3)
