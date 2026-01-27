import pytest
import pyrobloxbot as bot


class TestPackageExports:
    @pytest.mark.parametrize(
        "api_member",
        [
            "state",
            "exceptions",
            "keybinds",
            "require_focus",
            "keyboard_action",
            "hold_keyboard_action",
            "press_key",
            "hold_key",
            "key_down",
            "key_up",
            "walk",
            "walk_forward",
            "walk_left",
            "walk_right",
            "walk_back",
            "jump",
            "jump_continuous",
            "reset_player",
            "leave_game",
            "toggle_shift_lock",
            "chat",
            "toggle_ui_navigation",
            "ui_navigate",
            "ui_navigate_up",
            "ui_navigate_left",
            "ui_navigate_right",
            "ui_navigate_down",
            "ui_click",
            "ui_scroll_up",
            "ui_scroll_down",
            "equip_slot",
            "launch_game",
            "image_is_visible",
        ],
    )
    def test_public_api_completeness(self, api_member):
        assert hasattr(bot, api_member), (
            f"'{api_member}' is missing from the public API!"
        )
        assert api_member in bot.__all__, (
            f"'{api_member}' is missing from __all__ exports!"
        )

    @pytest.mark.parametrize(
        "internal",
        [
            "annotations",
            "_thread",
            "os",
            "wraps",
            "sleep",
            "kb",
            "dinput",
            "pg",
            "pyperclip",
            "Controller",
            "Key",
            "getActiveWindow",
            "getWindowsWithTitle",
            "GetForegroundWindow",
            "GetWindowText",
        ],
    )
    def test_no_internal_leakage(self, internal):
        assert not hasattr(bot, internal), (
            f"Internal dependency '{internal}' leaked into public namespace!"
        )
