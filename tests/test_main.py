import sys
from src.can_receiver import main


def test_main_normal_scenario(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["can_receiver.py", "normal"])

    main()

    output = capsys.readouterr().out

    assert "Scenario: normal" in output
    assert "Battery_Heartbeat: Alive Counter=1" in output
    assert "PASS" in output
    assert "All battery signals are within safe limits" in output

def test_main_overtemperature_scenario(monkeypatch, capsys):
    monkeypatch.setattr(
        sys, "argv", ["can_receiver.py", "overtemperature"]
    )

    main()

    output = capsys.readouterr().out

    assert "Scenario: overtemperature" in output
    assert "FAIL" in output
    assert "OVERTEMPERATURE detected" in output

def test_main_default_scenario(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["can_receiver.py"])

    main()

    output = capsys.readouterr().out

    assert "Scenario: normal" in output
    assert "PASS" in output