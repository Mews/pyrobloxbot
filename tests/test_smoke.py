import pytest

import pyrobloxbot as bot
from pyrobloxbot.bot.state import _BotState
from pyrobloxbot.bot.keybinds import _BotKeybinds


def test_state():
    assert isinstance(bot.state, _BotState)


def test_keybinds():
    assert isinstance(bot.keybinds, _BotKeybinds)


@pytest.mark.parametrize("export", bot.__all__)
def test__all__included_by_default(export):
    assert hasattr(bot, export), f"{export} not exported"


@pytest.mark.parametrize(
    "export",
    [
        "utils",
        "exceptions",
    ],
)
def test_other_exports_included_by_default(export):
    assert hasattr(bot, export), f"{export} not exported"


@pytest.mark.parametrize(
    "export",
    [
        "state",
        "keybinds",
        "options",
        "reset_player",
        "chat",
        "equip_slot",
        "toggle_shift_lock",
        "enable_shift_lock",
        "disable_shift_lock",
        "image_is_visible",
        "press_key",
        "hold_key",
        "keyboard_action",
        "hold_keyboard_action",
        "key_down",
        "key_up",
        "walk",
        "walk_forward",
        "walk_left",
        "walk_right",
        "walk_back",
        "jump",
        "jump_continuous",
        "leave_game",
        "join_game",
        "join_user",
        "join_private_server",
        "join_server",
        "toggle_ui_navigation",
        "enable_ui_navigation",
        "disable_ui_navigation",
        "ui_navigate",
        "ui_navigate_up",
        "ui_navigate_down",
        "ui_navigate_left",
        "ui_navigate_right",
        "ui_click",
        "ui_scroll_up",
        "ui_scroll_down",
        "toggle_inventory",
        "open_inventory",
        "close_inventory",
        "restore_focus",
        "wait",
    ],
)
def test__all__is_complete(export):
    assert export in bot.__all__, f"{export} not in __all__"


@pytest.mark.parametrize(
    "export",
    [
        "_BotState",
        "_BotKeybinds",
        "_BotOptions",
        "pyautogui",
        "pydirectinput",
        "keyboard",
        "pyperclip",
        "getActiveWindow",
        "getWindowsWithTitle",
        "GetForegroundWindow",
        "GetWindowText",
        "wraps",
        "os",
        "sleep",
        "NoRobloxWindowException",
        "InvalidSlotNumberException",
        "InvalidWalkDirectionException",
        "InvalidUiActionException",
        "KEYBOARD_KEYS",
        "WALK_DIRECTIONS",
        "UI_ACTIONS",
        "UI_NAVIGATE_UP_ACTIONS",
        "UI_NAVIGATE_LEFT_ACTIONS",
        "UI_NAVIGATE_RIGHT_ACTIONS",
        "UI_NAVIGATE_DOWN_ACTIONS",
        "UI_CLICK_ACTIONS",
        "pyscreeze",
        "ImageGrab",
    ],
)
def test_libraries_arent_exported(export):
    assert not hasattr(bot, export), f"{export} is being leaked"
