import pytest
from unittest.mock import patch, call

import pyrobloxbot as bot


@pytest.fixture
def mock_press_key():
    with patch("pyrobloxbot.core.character.press_key") as m:
        yield m


@pytest.fixture
def mock_hold_key():
    with patch("pyrobloxbot.core.character.hold_key") as m:
        yield m


@pytest.fixture
def mock_pyperclip():
    with patch("pyrobloxbot.core.character.pyperclip") as m:
        yield m


@pytest.fixture
def mock_toggle_inventory(mock_press_key):
    with patch("pyrobloxbot.core.character.toggle_inventory") as m:
        yield m


def test_reset_player(mock_press_key, mock_wait):
    bot.reset_player(3)

    mock_press_key.assert_has_calls([call("esc"), call("r"), call("enter")])
    mock_wait.assert_has_calls([call(3)] * 2)


def test_chat(mock_pyperclip, mock_press_key, mock_hold_key):
    original_clipboard = "original clipboard"
    mock_pyperclip.paste.return_value = original_clipboard
    message = "Hello world!"

    bot.chat(message)

    mock_press_key.assert_has_calls([call(bot.keybinds.open_chat), call("enter")])
    mock_hold_key.assert_called_with("ctrl", "v", duration=0.5)

    mock_pyperclip.paste.assert_called_once()
    mock_pyperclip.copy.assert_has_calls([call(message), call(original_clipboard)])


def test_chat_different_chat_key(mock_pyperclip, mock_press_key, mock_hold_key):
    original_clipboard = "original clipboard"
    mock_pyperclip.paste.return_value = original_clipboard
    message = "Hello world!"

    bot.keybinds.open_chat = "-"

    bot.chat(message)

    mock_press_key.assert_has_calls([call("-"), call("enter")])
    mock_hold_key.assert_called_with("ctrl", "v", duration=0.5)

    mock_pyperclip.paste.assert_called_once()
    mock_pyperclip.copy.assert_has_calls([call(message), call(original_clipboard)])


@pytest.mark.parametrize("slot", list(range(0, 10)))
def test_equip_slot(slot, mock_press_key):
    bot.equip_slot(slot)

    mock_press_key.assert_called_once_with(str(slot))


@pytest.mark.parametrize("slot", [-1, 10, "hi", None])
def test_equip_slot_invalid_slot(slot):
    with pytest.raises(bot.exceptions.InvalidSlotNumberException):
        bot.equip_slot(10)


def test_toggle_shift_lock(mock_press_key):
    bot.state._SHIFT_LOCK_ENABLED = False

    bot.toggle_shift_lock()
    mock_press_key.assert_called_once_with(bot.keybinds.toggle_shift_lock)

    assert bot.state.is_shift_lock_enabled()


def test_toggle_shift_lock_different_keybind(mock_press_key):
    bot.state._SHIFT_LOCK_ENABLED = False

    bot.keybinds.toggle_shift_lock = "ctrl"
    bot.toggle_shift_lock()
    mock_press_key.assert_called_once_with("ctrl")

    assert bot.state.is_shift_lock_enabled()


def test_toggle_inventory(mock_press_key):
    bot.state._INVENTORY_OPEN = False

    bot.toggle_inventory()
    mock_press_key.assert_called_once_with(bot.keybinds.toggle_inventory)

    assert bot.state.is_inventory_open()


def test_toggle_inventory_different_keybind(mock_press_key):
    bot.state._INVENTORY_OPEN = False

    bot.keybinds.toggle_inventory = "\\"
    bot.toggle_inventory()
    mock_press_key.assert_called_once_with("\\")

    assert bot.state.is_inventory_open()


def test_open_inventory_inventory_closed(mock_toggle_inventory):
    bot.state._INVENTORY_OPEN = False
    bot.open_inventory()
    mock_toggle_inventory.assert_called_once()


def test_open_inventory_inventory_open(mock_toggle_inventory):
    bot.state._INVENTORY_OPEN = True
    bot.open_inventory()
    mock_toggle_inventory.assert_not_called()


def test_close_inventory_inventory_closed(mock_toggle_inventory):
    bot.state._INVENTORY_OPEN = False
    bot.close_inventory()
    mock_toggle_inventory.assert_not_called()


def test_close_inventory_inventory_open(mock_toggle_inventory):
    bot.state._INVENTORY_OPEN = True
    bot.close_inventory()
    mock_toggle_inventory.assert_called_once()
