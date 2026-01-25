import pytest
from unittest.mock import patch


@pytest.fixture(autouse=True)
def mock_require_focus():
    with (
        patch("pyrobloxbot.core.GetWindowText", return_value="Roblox"),
        patch("pyrobloxbot.core.GetForegroundWindow"),
    ):
        yield
