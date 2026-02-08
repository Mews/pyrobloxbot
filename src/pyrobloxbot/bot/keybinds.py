from dataclasses import dataclass, field
from ..constants import KEYBOARD_KEYS
from ..utils import parse_special_key_for_pynput, _failsafe
from pynput import keyboard


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
        """Changes the hotkey required to trigger the failsafe

        The default hotkey is ``control + m``

        Args:
            *keys (KEYBOARD_KEYS): The new keys whose combination triggers the failsafe.
        """
        if self._FAILSAFE_LISTENER is not None:
            self._FAILSAFE_LISTENER.stop()

        parsed_keys = [parse_special_key_for_pynput(key) for key in keys]

        self._FAILSAFE_HOTKEY = "+".join(parsed_keys)

        self._FAILSAFE_LISTENER = keyboard.GlobalHotKeys(
            {self._FAILSAFE_HOTKEY: _failsafe}
        )
        self._FAILSAFE_LISTENER.daemon = True
        self._FAILSAFE_LISTENER.start()

    def _reset(self):
        self.__init__()


__all__ = ["_BotKeybinds"]
