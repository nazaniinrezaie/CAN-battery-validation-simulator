from src.can_receiver import decode_heartbeat_message


def test_decode_heartbeat_message():
    message = {
        "signals": {
            "alive_counter": 5
        }
    }

    result = decode_heartbeat_message(message)

    assert result == 5