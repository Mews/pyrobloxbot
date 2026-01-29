import pytest
from unittest.mock import patch, call, MagicMock

import pyrobloxbot as bot


@pytest.fixture
def mock_pydirectinput():
    with patch("pyrobloxbot.core.input.pydirectinput") as m:
        yield m


@pytest.fixture
def mock_key_down():
    with patch("pyrobloxbot.core.input.key_down") as m:
        yield m


@pytest.fixture
def mock_key_up():
    with patch("pyrobloxbot.core.input.key_up") as m:
        yield m


def test_press_key_single(mock_pydirectinput):
    bot.press_key("esc")

    mock_pydirectinput.press.assert_called_once_with("esc")


def test_press_key_multiple(mock_pydirectinput):
    keys = ["w", "a", "s", "d"]

    bot.press_key(*keys)

    mock_pydirectinput.press.assert_has_calls([call(key) for key in keys])


def test_hold_key_single(mock_key_down, mock_key_up, mock_wait):
    bot.hold_key("esc", duration=10)

    mock_key_down.assert_called_once_with("esc")
    mock_wait.assert_called_once_with(10)
    mock_key_up.assert_called_once_with("esc")


def test_hold_key_multiple(mock_key_down, mock_key_up, mock_wait):
    keys = ["w", "a", "s", "d"]

    bot.hold_key(*keys, duration=10)

    mock_key_down.assert_has_calls([call(key) for key in keys])

    mock_wait.assert_called_once_with(10)

    mock_key_up.assert_has_calls([call(key) for key in keys])


def test_aliases():
    assert bot.keyboard_action == bot.press_key
    assert bot.hold_keyboard_action == bot.hold_key


def test_key_down(mock_pydirectinput):
    bot.key_down("esc")
    mock_pydirectinput.keyDown.assert_called_once_with("esc")


def test_key_up(mock_pydirectinput):
    bot.key_up("esc")
    mock_pydirectinput.keyUp.assert_called_once_with("esc")


@patch("pyrobloxbot.core.input.GetForegroundWindow")
@patch("pyrobloxbot.core.input.GetWindowText", return_value="Roblox")
def test_require_focus_window_already_active(_, __):
    @bot.require_focus
    def dummy_function():
        return "success"

    assert dummy_function() == "success"


@patch("pyrobloxbot.core.input.GetForegroundWindow")
@patch("pyrobloxbot.core.input.GetWindowText", return_value="Not Roblox")
@patch("pyrobloxbot.core.input.getWindowsWithTitle", return_value=[])
def test_require_focus_no_roblox_window(_, __, ___):
    @bot.require_focus
    def dummy_function():
        return "success"

    with pytest.raises(bot.exceptions.NoRobloxWindowException):
        dummy_function()


@patch("pyrobloxbot.core.input.getActiveWindow", return_value="Not None")
@patch("pyrobloxbot.core.input.pyautogui")
@patch("pyrobloxbot.core.input.getWindowsWithTitle")
@patch("pyrobloxbot.core.input.GetWindowText", return_value="Not Roblox")
@patch("pyrobloxbot.core.input.GetForegroundWindow")
def test_require_focus_window_not_already_active(
    _, __, mock_getWindowsWithTitle, mock_pyautogui, ___
):
    mock_window = MagicMock()
    mock_window.title = "Roblox"

    mock_getWindowsWithTitle.return_value = [mock_window]

    @bot.require_focus
    def dummy_function():
        return "success"

    assert dummy_function() == "success"

    mock_pyautogui.press.assert_called_once_with("altleft")
    mock_window.maximize.assert_called_once()
    mock_window.activate.assert_called_once()
