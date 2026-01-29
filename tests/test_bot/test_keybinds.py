import pytest
from pyrobloxbot.bot.keybinds import _BotKeybinds
from unittest.mock import patch


@pytest.fixture
def mock_keyboard():
    with patch("pyrobloxbot.bot.keybinds.keyboard") as m:
        yield m


@pytest.fixture
def keybinds(mock_keyboard):
    return _BotKeybinds()


def test_default_keybinds(keybinds):
    assert keybinds.walk_forward == "w"
    assert keybinds.walk_left == "a"
    assert keybinds.walk_right == "d"
    assert keybinds.walk_back == "s"

    assert keybinds.jump == "space"

    assert keybinds.toggle_shift_lock == "shift"

    assert keybinds.toggle_ui_navigation == "\\"

    assert keybinds.ui_navigate_up == "up"
    assert keybinds.ui_navigate_left == "left"
    assert keybinds.ui_navigate_right == "right"
    assert keybinds.ui_navigate_down == "down"
    assert keybinds.ui_click == "enter"

    assert keybinds.open_chat == "/"


def test_failsafe_enabled(keybinds, mock_keyboard):
    assert keybinds._FAILSAFE_HOTKEY == "ctrl+m"

    import _thread

    mock_keyboard.add_hotkey.assert_called_once_with("ctrl+m", _thread.interrupt_main)


def test_set_failsafe_hotkey(keybinds, mock_keyboard):
    default_hotkey = "ctrl+m"
    expected_new_hotkey = "ctrl+shift+y"

    keybinds.set_failsafe_hotkey("ctrl", "shift", "y")

    assert keybinds._FAILSAFE_HOTKEY == expected_new_hotkey

    mock_keyboard.clear_hotkey.assert_called_once_with(default_hotkey)

    import _thread

    mock_keyboard.add_hotkey.assert_called_with(
        expected_new_hotkey, _thread.interrupt_main
    )

    assert (
        mock_keyboard.add_hotkey.call_count == 2
    )  # the one is __post_init__ and the one we tested
