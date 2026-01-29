import pytest
from unittest.mock import patch


@pytest.fixture(autouse=True)
def mock_active_window():
    with (
        patch("pyrobloxbot.core.input.GetForegroundWindow"),
        patch("pyrobloxbot.core.input.GetWindowText", return_value="Roblox"),
    ):
        yield


@pytest.fixture(autouse=True)
def mock_wait():
    with patch("pyrobloxbot.utils.sleep") as m:
        yield m
