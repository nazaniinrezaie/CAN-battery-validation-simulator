import pytest
from src.can_receiver import get_scenario_values


def test_normal_scenario():
    values = get_scenario_values("normal")

    assert values == (380.5, 25.3, 32.7, 80, 0)

def test_undervoltage_scenario():
    values = get_scenario_values("undervoltage")

    assert values == (250.0, 25.3, 32.7, 80, 1)

def test_overcurrent_scenario():
    values = get_scenario_values("overcurrent")

    assert values == (380.5, 120.0, 32.7, 80, 2)

def test_overtemperature_scenario():
    values = get_scenario_values("overtemperature")

    assert values == (380.5, 25.3, 70.0, 80, 3)

def test_low_soc_scenario():
    values = get_scenario_values("low_soc")

    assert values == (380.5, 25.3, 32.7, 5, 4)

def test_invalid_scenario():
    with pytest.raises(SystemExit) as exc_info:
        get_scenario_values("invalid")

    assert exc_info.value.code == 1
