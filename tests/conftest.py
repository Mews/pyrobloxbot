import pytest
from unittest.mock import patch


@pytest.fixture(autouse=True)
def mock_require_focus():
    with (
        patch("pyrobloxbot.core.input.GetWindowText", return_value="Roblox"),
        patch("pyrobloxbot.core.input.GetForegroundWindow"),
    ):
        yield


@pytest.fixture(autouse=True)
def mock_sleep():
    with patch("pyrobloxbot.utils.sleep"):
        yield
