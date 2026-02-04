import pytest
from unittest.mock import patch, MagicMock
from pyrobloxbot.bot.keybinds import _BotKeybinds


@pytest.fixture(autouse=True)
def mock_util_pynput_key_parse():
    with patch("pyrobloxbot.bot.keybinds.parse_special_key_for_pynput") as m:
        m.side_effect = {
            "ctrl": "<ctrl>",
            "m": "m",
            "shift": "<shift>",
            "y": "y",
            "x": "x",
        }.get
        yield m


@pytest.fixture(autouse=True)
def mock_failsafe_function():
    with patch("pyrobloxbot.bot.keybinds._failsafe") as m:
        yield m


@pytest.fixture
def keybinds(mock_pynput_keyboard, mock_util_pynput_key_parse, mock_failsafe_function):
    return _BotKeybinds()


def assert_keybinds_are_default(keybinds):
    assert keybinds.walk_forward == "w"
    assert keybinds.walk_left == "a"
    assert keybinds.walk_right == "d"
    assert keybinds.walk_back == "s"

    assert keybinds.jump == "space"

    assert keybinds.toggle_shift_lock == "shift"

    assert keybinds.toggle_ui_navigation == "\\"

    assert keybinds.toggle_inventory == "`"

    assert keybinds.ui_navigate_up == "up"
    assert keybinds.ui_navigate_left == "left"
    assert keybinds.ui_navigate_right == "right"
    assert keybinds.ui_navigate_down == "down"
    assert keybinds.ui_click == "enter"

    assert keybinds.open_chat == "/"


def test_default_keybinds(keybinds):
    assert_keybinds_are_default(keybinds)


def test_failsafe_enabled(keybinds, mock_pynput_keyboard, mock_failsafe_function):
    mock_pynput_keyboard.GlobalHotKeys.reset_mock()

    mock_listener = MagicMock()
    mock_pynput_keyboard.GlobalHotKeys.return_value = mock_listener

    keybinds = _BotKeybinds()

    assert keybinds._FAILSAFE_HOTKEY == "<ctrl>+m"
    assert keybinds._FAILSAFE_LISTENER is mock_listener
    mock_pynput_keyboard.GlobalHotKeys.assert_called_once_with(
        {"<ctrl>+m": mock_failsafe_function}
    )

    mock_listener.start.assert_called_once()
    assert mock_listener.daemon


def test_set_failsafe_hotkey(keybinds, mock_pynput_keyboard, mock_failsafe_function):
    old_listener = MagicMock()
    new_listener = MagicMock()

    mock_pynput_keyboard.GlobalHotKeys.side_effect = [old_listener, new_listener]

    keybinds = _BotKeybinds()

    keybinds.set_failsafe_hotkey("ctrl", "shift", "y")

    assert keybinds._FAILSAFE_HOTKEY == "<ctrl>+<shift>+y"
    old_listener.stop.assert_called_once()
    new_listener.start.assert_called_once()
    assert keybinds._FAILSAFE_LISTENER is new_listener

    mock_pynput_keyboard.GlobalHotKeys.assert_any_call(
        {"<ctrl>+<shift>+y": mock_failsafe_function}
    )


def test__reset_resets_failsafe_fields(keybinds, mock_pynput_keyboard):
    first_listener = MagicMock()
    second_listener = MagicMock()
    third_listener = MagicMock()

    mock_pynput_keyboard.GlobalHotKeys.side_effect = [
        first_listener,
        second_listener,
        third_listener,
    ]

    keybinds = _BotKeybinds()

    assert keybinds._FAILSAFE_LISTENER is first_listener
    assert keybinds._FAILSAFE_HOTKEY == "<ctrl>+m"

    keybinds.set_failsafe_hotkey("shift", "x")

    assert keybinds._FAILSAFE_LISTENER is second_listener
    assert keybinds._FAILSAFE_HOTKEY == "<shift>+x"

    keybinds._reset()

    assert keybinds._FAILSAFE_LISTENER is third_listener
    assert keybinds._FAILSAFE_HOTKEY == "<ctrl>+m"


def test__reset(keybinds):
    for attr in keybinds.__dict__:
        if not attr.startswith("_"):
            setattr(keybinds, attr, "esc")

    assert keybinds.jump == "esc"
    assert keybinds.open_chat == "esc"

    keybinds._reset()

    assert_keybinds_are_default(keybinds)
