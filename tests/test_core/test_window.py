import pytest
from unittest.mock import patch, MagicMock

import pyrobloxbot as bot


@pytest.fixture
def mock_win32gui():
    with patch("pyrobloxbot.core.window.win32gui") as m:
        yield m


def test_wait_for_focus(mock_win32gui):
    mock_hwnd = MagicMock()
    mock_win32gui.GetForegroundWindow.return_value = mock_hwnd
    mock_win32gui.GetWindowText.return_value = "Roblox"

    assert bot.wait_for_focus() == mock_hwnd
