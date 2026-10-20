
from src.can_receiver import check_faults


def test_undervoltage_below_threshold():
    faults = check_faults(
        voltage=299.9,
        current=25.3,
        temperature=32.7,
        soc=80
    )

    assert "UNDERVOLTAGE" in faults

def test_undervoltage_at_threshold():
    faults = check_faults(
        voltage=300.0,
        current=25.3,
        temperature=32.7,
        soc=80
    )

    assert "UNDERVOLTAGE" not in faults


def test_undervoltage_above_threshold():
    faults = check_faults(
        voltage=300.1,
        current=25.3,
        temperature=32.7,
        soc=80
    )

    assert "UNDERVOLTAGE" not in faults
