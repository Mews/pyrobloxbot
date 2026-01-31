import pytest
from unittest.mock import patch, call

import pyrobloxbot as bot


@pytest.fixture
def mock_press_key():
    with patch("pyrobloxbot.core.ui.press_key") as m:
        yield m


@pytest.fixture(autouse=True)
def mock_toggle_ui_navigation(mock_press_key):
    with patch("pyrobloxbot.core.ui.toggle_ui_navigation") as m:
        yield m


@pytest.fixture
def mock_ui_navigate(mock_press_key, mock_toggle_ui_navigation):
    with patch("pyrobloxbot.core.ui.ui_navigate") as m:
        yield m


@pytest.fixture
def mock_pynput_Key():
    with patch("pyrobloxbot.core.ui.Key") as m:
        yield m


@pytest.fixture
def mock_pynput_Controller(mock_pynput_Key):
    with patch("pyrobloxbot.core.ui.Controller") as m:
        yield m


def test_toggle_ui_navigation(mock_press_key):
    bot.state._UI_NAV_ENABLED = False

    bot.toggle_ui_navigation()
    mock_press_key.assert_called_once_with(bot.keybinds.toggle_ui_navigation)

    assert bot.state.is_ui_nav_enabled()


def test_toggle_ui_navigation_different_keybind(mock_press_key):
    bot.state._UI_NAV_ENABLED = False
    bot.keybinds.toggle_ui_navigation = "~"

    bot.toggle_ui_navigation()
    mock_press_key.assert_called_once_with("~")

    assert bot.state.is_ui_nav_enabled()


def test_ui_navigate_enables_ui_navigation(mock_toggle_ui_navigation):
    bot.state._UI_NAV_ENABLED = False
    bot.ui_navigate("up")
    mock_toggle_ui_navigation.assert_called_once()


def test_ui_navigate_dont_enable_ui_navigation_already_on(mock_toggle_ui_navigation):
    bot.state._UI_NAV_ENABLED = True
    bot.ui_navigate("up")
    mock_toggle_ui_navigation.assert_not_called()


@pytest.mark.parametrize("action", ["up", "u"])
def test_ui_navigate_up_actions(action, mock_press_key):
    bot.ui_navigate(action)
    mock_press_key.assert_called_with(bot.keybinds.ui_navigate_up)


@pytest.mark.parametrize("action", ["down", "d"])
def test_ui_navigate_down_actions(action, mock_press_key):
    bot.ui_navigate(action)
    mock_press_key.assert_called_with(bot.keybinds.ui_navigate_down)


@pytest.mark.parametrize("action", ["left", "l"])
def test_ui_navigate_left_actions(action, mock_press_key):
    bot.ui_navigate(action)
    mock_press_key.assert_called_with(bot.keybinds.ui_navigate_left)


@pytest.mark.parametrize("action", ["right", "r"])
def test_ui_navigate_right_actions(action, mock_press_key):
    bot.ui_navigate(action)
    mock_press_key.assert_called_with(bot.keybinds.ui_navigate_right)


def test_ui_navigate_multiple_actions_cardinal_only(mock_press_key):
    bot.ui_navigate("u", "u", "d", "d", "l", "r", "l", "r")  # B A Start :)
    mock_press_key.assert_has_calls(
        [
            call(bot.keybinds.ui_navigate_up),
            call(bot.keybinds.ui_navigate_up),
            call(bot.keybinds.ui_navigate_down),
            call(bot.keybinds.ui_navigate_down),
            call(bot.keybinds.ui_navigate_left),
            call(bot.keybinds.ui_navigate_right),
            call(bot.keybinds.ui_navigate_left),
            call(bot.keybinds.ui_navigate_right),
        ]
    )


def test_ui_navigate_invalid_action(mock_press_key):
    with pytest.raises(bot.exceptions.InvalidUiActionException):
        bot.ui_navigate("Hello world!")


def test_ui_navigate_up(mock_ui_navigate):
    bot.ui_navigate_up()
    mock_ui_navigate.assert_called_once_with("u")


def test_ui_navigate_up_multiple_times(mock_ui_navigate):
    bot.ui_navigate_up(10)
    mock_ui_navigate.assert_has_calls([call("u")] * 10)


def test_ui_navigate_down(mock_ui_navigate):
    bot.ui_navigate_down()
    mock_ui_navigate.assert_called_once_with("d")


def test_ui_navigate_down_multiple_times(mock_ui_navigate):
    bot.ui_navigate_down(10)
    mock_ui_navigate.assert_has_calls([call("d")] * 10)


def test_ui_navigate_left(mock_ui_navigate):
    bot.ui_navigate_left()
    mock_ui_navigate.assert_called_once_with("l")


def test_ui_navigate_left_multiple_times(mock_ui_navigate):
    bot.ui_navigate_left(10)
    mock_ui_navigate.assert_has_calls([call("l")] * 10)


def test_ui_navigate_right(mock_ui_navigate):
    bot.ui_navigate_right()
    mock_ui_navigate.assert_called_once_with("r")


def test_ui_navigate_right_multiple_times(mock_ui_navigate):
    bot.ui_navigate_right(10)
    mock_ui_navigate.assert_has_calls([call("r")] * 10)


def test_ui_click_enables_ui_navigation(mock_toggle_ui_navigation):
    bot.state._UI_NAV_ENABLED = False
    bot.ui_click()
    mock_toggle_ui_navigation.assert_called_once()


def test_ui_click_doesnt_enable_ui_navigation_already_on(mock_toggle_ui_navigation):
    bot.state._UI_NAV_ENABLED = True
    bot.ui_click()
    mock_toggle_ui_navigation.assert_not_called()


def test_ui_click(mock_press_key):
    bot.ui_click()
    mock_press_key.assert_called_with(bot.keybinds.ui_click)


def test_ui_click_different_hotkey(mock_press_key):
    bot.keybinds.ui_click = "space"
    bot.ui_click()
    mock_press_key.assert_called_with("space")


def test_ui_scroll_up_enables_ui_navigation(
    mock_toggle_ui_navigation, mock_pynput_Controller
):
    bot.state._UI_NAV_ENABLED = False
    bot.ui_scroll_up(1)
    mock_toggle_ui_navigation.assert_called_once()


def test_ui_scroll_up_doesnt_enable_ui_navigation_already_on(
    mock_toggle_ui_navigation, mock_pynput_Controller
):
    bot.state._UI_NAV_ENABLED = True
    bot.ui_scroll_up(1)
    mock_toggle_ui_navigation.assert_not_called()


def test_ui_scroll_down_enables_ui_navigation(
    mock_toggle_ui_navigation, mock_pynput_Controller
):
    bot.state._UI_NAV_ENABLED = False
    bot.ui_scroll_down(1)
    mock_toggle_ui_navigation.assert_called_once()


def test_ui_scroll_down_doesnt_enable_ui_navigation_already_on(
    mock_toggle_ui_navigation, mock_pynput_Controller
):
    bot.state._UI_NAV_ENABLED = True
    bot.ui_scroll_down(1)
    mock_toggle_ui_navigation.assert_not_called()


def test_ui_scroll_up(mock_pynput_Controller, mock_pynput_Key, mock_wait):
    bot.ui_scroll_up(10, 0.5)

    mock_pynput_Controller.return_value.press.assert_has_calls(
        [call(mock_pynput_Key.page_up)] * 10
    )
    mock_pynput_Controller.return_value.release.assert_has_calls(
        [call(mock_pynput_Key.page_up)] * 10
    )
    mock_wait.assert_has_calls([call(0.5)] * 10)


def test_ui_scroll_down(mock_pynput_Controller, mock_pynput_Key, mock_wait):
    bot.ui_scroll_down(10, 0.5)

    mock_pynput_Controller.return_value.press.assert_has_calls(
        [call(mock_pynput_Key.page_down)] * 10
    )
    mock_pynput_Controller.return_value.release.assert_has_calls(
        [call(mock_pynput_Key.page_down)] * 10
    )
    mock_wait.assert_has_calls([call(0.5)] * 10)
