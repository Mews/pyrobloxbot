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


@patch("pyrobloxbot.decorators.state")
def test_resets_state(mock_state):
    @bot.decorators.resets_state
    def dummy_function():
        return "success"

    assert dummy_function() == "success"
    mock_state._reset.assert_called_once()


@patch("pyrobloxbot.decorators.state")
def test_resets_state_still_resets_if_fn_raises(mock_state):
    @bot.decorators.resets_state
    def dummy_function():
        raise Exception

    with pytest.raises(Exception):
        dummy_function()

    mock_state._reset.assert_called_once()


@pytest.fixture
def mock_toggle_ui_navigation():
    with patch("pyrobloxbot.core.ui.toggle_ui_navigation") as m:

        def toggle_value():
            bot.state._UI_NAV_ENABLED = not bot.state._UI_NAV_ENABLED

        m.side_effect = toggle_value

        yield m


@pytest.mark.parametrize("initial_nav_state", [True, False])
@pytest.mark.parametrize("function_behavior", ["success", "fail", "toggle"])
def test_requires_ui_navigation_mode_final_state_is_starting_state(
    mock_toggle_ui_navigation, initial_nav_state, function_behavior
):
    @bot.decorators.requires_ui_navigation_mode
    def dummy_function():
        if function_behavior == "fail":
            raise Exception
        if function_behavior == "success":
            return "success"
        if function_behavior == "toggle":
            mock_toggle_ui_navigation()

    bot.state._UI_NAV_ENABLED = initial_nav_state

    try:
        dummy_function()
    except Exception:
        assert function_behavior == "fail"

    assert bot.state.is_ui_nav_enabled() == initial_nav_state, (
        "Didn't restore state correctly"
    )


def test_requires_ui_navigation_mode(mock_toggle_ui_navigation):
    @bot.decorators.requires_ui_navigation_mode
    def dummy_function():
        return "success"

    bot.state._UI_NAV_ENABLED = False
    assert dummy_function() == "success"
    assert mock_toggle_ui_navigation.call_count == 2


def test_requires_ui_navigation_mode_already_enabled(mock_toggle_ui_navigation):
    @bot.decorators.requires_ui_navigation_mode
    def dummy_function():
        return "success"

    bot.state._UI_NAV_ENABLED = True
    assert dummy_function() == "success"
    assert mock_toggle_ui_navigation.call_count == 0
