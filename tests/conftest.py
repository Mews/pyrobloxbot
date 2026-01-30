import pytest
from unittest.mock import patch
import pyrobloxbot as bot


@pytest.fixture(autouse=True)
def mock_active_window():
    with (
        patch("pyrobloxbot.core.decorators.GetForegroundWindow"),
        patch("pyrobloxbot.core.decorators.GetWindowText", return_value="Roblox"),
    ):
        yield


@pytest.fixture(autouse=True)
def mock_wait():
    with patch("pyrobloxbot.utils.sleep") as m:
        yield m


@pytest.fixture(autouse=True)
def reset_bot():
    bot.state._reset()
    bot.keybinds._reset()
