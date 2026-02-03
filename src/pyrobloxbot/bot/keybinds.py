from dataclasses import dataclass, field
from ..constants import KEYBOARD_KEYS
from ..utils import parse_special_key_for_pynput
from pynput import keyboard
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
    _FAILSAFE_LISTENER: keyboard.GlobalHotKeys = field(init=False, default=None)

    def __post_init__(self):
        self.set_failsafe_hotkey("ctrl", "m")

    def set_failsafe_hotkey(self, *keys: KEYBOARD_KEYS) -> None:
        """Changes hotkey required to trigger the failsafe

        The default hotkey is control + m

        :param keys: The key combination for triggering the failsafe
        :type keys: KEYBOARD_KEYS
        """
        if self._FAILSAFE_LISTENER is not None:
            self._FAILSAFE_LISTENER.stop()

        parsed_keys = [parse_special_key_for_pynput(key) for key in keys]

        self._FAILSAFE_HOTKEY = "+".join(parsed_keys)

        self._FAILSAFE_LISTENER = keyboard.GlobalHotKeys(
            {self._FAILSAFE_HOTKEY: _thread.interrupt_main}
        )
        self._FAILSAFE_LISTENER.daemon = True
        self._FAILSAFE_LISTENER.start()

    def _reset(self):
        self.__init__()


__all__ = ["_BotKeybinds"]
