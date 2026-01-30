import pytest

from unittest.mock import patch, MagicMock
import pyrobloxbot as bot


@patch("pyrobloxbot.core.decorators.GetForegroundWindow")
@patch("pyrobloxbot.core.decorators.GetWindowText", return_value="Roblox")
def test_require_focus_window_already_active(_, __):
    @bot.decorators.require_focus
    def dummy_function():
        return "success"

    assert dummy_function() == "success"


@patch("pyrobloxbot.core.decorators.GetForegroundWindow")
@patch("pyrobloxbot.core.decorators.GetWindowText", return_value="Not Roblox")
@patch("pyrobloxbot.core.decorators.getWindowsWithTitle", return_value=[])
def test_require_focus_no_roblox_window(_, __, ___):
    @bot.decorators.require_focus
    def dummy_function():
        return "success"

    with pytest.raises(bot.exceptions.NoRobloxWindowException):
        dummy_function()


@patch("pyrobloxbot.core.decorators.getActiveWindow", return_value="Not None")
@patch("pyrobloxbot.core.decorators.pyautogui")
@patch("pyrobloxbot.core.decorators.getWindowsWithTitle")
@patch("pyrobloxbot.core.decorators.GetWindowText", return_value="Not Roblox")
@patch("pyrobloxbot.core.decorators.GetForegroundWindow")
def test_require_focus_window_not_already_active(
    _, __, mock_getWindowsWithTitle, mock_pyautogui, ___
):
    mock_window = MagicMock()
    mock_window.title = "Roblox"

    mock_getWindowsWithTitle.return_value = [mock_window]

    @bot.decorators.require_focus
    def dummy_function():
        return "success"

    assert dummy_function() == "success"

    mock_pyautogui.press.assert_called_once_with("altleft")
    mock_window.maximize.assert_called_once()
    mock_window.activate.assert_called_once()
