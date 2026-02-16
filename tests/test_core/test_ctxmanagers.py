import pytest
from unittest.mock import MagicMock, patch

import pyrobloxbot as bot


@pytest.fixture
def mock_GetForegroundWindow():
    with patch("pyrobloxbot.core.ctxmanagers.win32gui.GetForegroundWindow") as m:
        yield m


@pytest.fixture
def mock_SetForegroundWindow():
    with patch("pyrobloxbot.core.ctxmanagers.win32gui.SetForegroundWindow") as m:
        yield m


def test_restore_focus(mock_GetForegroundWindow, mock_SetForegroundWindow):
    mock_hwnd = MagicMock()
    mock_GetForegroundWindow.return_value = mock_hwnd

    def dummy_function():
        return "success"

    with bot.restore_focus():
        assert dummy_function() == "success"

    mock_SetForegroundWindow.assert_called_once_with(mock_hwnd)
