
from src.can_receiver import check_faults


def test_overtemperature_below_threshold():
    faults = check_faults(
        voltage=380.5,
        current=25.3,
        temperature=59.9,
        soc=80
    )
    assert "OVERTEMPERATURE" not in faults


def test_overtemperature_at_threshold():
    faults = check_faults(
        voltage=380.5,
        current=25.3,
        temperature=60.0,
        soc=80
    )
    assert "OVERTEMPERATURE" not in faults


def test_overtemperature_above_threshold():
    faults = check_faults(
        voltage=380.5,
        current=25.3,
        temperature=60.1,
        soc=80
    )
    assert "OVERTEMPERATURE" in faults
