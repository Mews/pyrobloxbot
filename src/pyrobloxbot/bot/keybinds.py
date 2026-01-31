from dataclasses import dataclass, field
from ..constants import KEYBOARD_KEYS
import keyboard
import _thread


@dataclass
class _BotKeybinds:
    walk_forward: str = "w"
    walk_back: str = "s"
    walk_left: str = "a"
    walk_right: str = "d"

    jump: str = "space"

    toggle_shift_lock: str = "shift"

    toggle_ui_navigation: str = "\\"

    toggle_inventory: str = "`"

    ui_navigate_up: str = "up"
    ui_navigate_down: str = "down"
    ui_navigate_left: str = "left"
    ui_navigate_right: str = "right"
    ui_click: str = "enter"

    open_chat: str = "/"

    _FAILSAFE_HOTKEY: str = field(init=False, default="")

    def __post_init__(self):
        self.set_failsafe_hotkey("ctrl", "m")

    def set_failsafe_hotkey(self, *keys: KEYBOARD_KEYS) -> None:
        """Changes hotkey required to trigger the failsafe

        The default hotkey is control + m

        :param keys: The key combination for triggering the failsafe
        :type keys: KEYBOARD_KEYS
        """

        if self._FAILSAFE_HOTKEY:
            keyboard.clear_hotkey(self._FAILSAFE_HOTKEY)

        self._FAILSAFE_HOTKEY = "+".join(keys)

        keyboard.add_hotkey(self._FAILSAFE_HOTKEY, _thread.interrupt_main)

    def _reset(self):
        self.__init__()


__all__ = ["_BotKeybinds"]
