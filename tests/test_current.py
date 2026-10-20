
from src.can_receiver import check_faults


def test_overcurrent_below_threshold():
    faults = check_faults(
        voltage=380.5,
        current=99.9,
        temperature=32.7,
        soc=80
    )

    assert "OVERCURRENT" not in faults


def test_overcurrent_at_threshold():
    faults = check_faults(
        voltage=380.5,
        current=100.0,
        temperature=32.7,
        soc=80
    )

    assert "OVERCURRENT" not in faults


def test_overcurrent_above_threshold():
    faults = check_faults(
        voltage=380.5,
        current=100.1,
        temperature=32.7,
        soc=80
    )

    assert "OVERCURRENT" in faults
