
from src.can_receiver import check_faults


def test_low_soc_below_threshold():
    faults = check_faults(
        voltage=380.5,
        current=25.3,
        temperature=32.7,
        soc=9.9
    )

    assert "LOW_SOC" in faults


def test_low_soc_at_threshold():
    faults = check_faults(
        voltage=380.5,
        current=25.3,
        temperature=32.7,
        soc=10.0
    )

    assert "LOW_SOC" not in faults


def test_low_soc_above_threshold():
    faults = check_faults(
        voltage=380.5,
        current=25.3,
        temperature=32.7,
        soc=10.1
    )

    assert "LOW_SOC" not in faults
