import pytest
from unittest.mock import patch, MagicMock

import pyrobloxbot as bot


@pytest.fixture
def mock_win32gui():
    with patch("pyrobloxbot.core.window.win32gui") as m:
        yield m


@pytest.fixture(autouse=True)
def mock_pydirectinput():
    with patch("pyrobloxbot.core.window.pydirectinput") as m:
        yield m


def test_wait_for_focus(mock_win32gui, mock_pydirectinput):
    mock_roblox_hwnd = MagicMock()
    mock_desktop_hwnd = MagicMock()
    mock_win32gui.GetForegroundWindow.return_value = mock_roblox_hwnd
    mock_win32gui.GetWindowText.return_value = "Roblox"
    mock_win32gui.GetDesktopWindow.return_value = mock_desktop_hwnd

    assert bot.wait_for_focus() == mock_roblox_hwnd
    mock_pydirectinput.press.assert_called_once_with("altleft")
    mock_win32gui.SetForegroundWindow.assert_called_once_with(mock_desktop_hwnd)


def test_wait_for_focus_take_away_focus_false(mock_win32gui, mock_pydirectinput):
    mock_roblox_hwnd = MagicMock()
    mock_desktop_hwnd = MagicMock()
    mock_win32gui.GetForegroundWindow.return_value = mock_roblox_hwnd
    mock_win32gui.GetWindowText.return_value = "Roblox"
    mock_win32gui.GetDesktopWindow.return_value = mock_desktop_hwnd

    assert bot.wait_for_focus(take_away_focus=False) == mock_roblox_hwnd
    mock_pydirectinput.press.assert_not_called()
    mock_win32gui.SetForegroundWindow.assert_not_called()
