from ..constants import KEYBOARD_KEYS

import pydirectinput

from ..utils import wait
from .decorators import require_focus


@require_focus
def press_key(*keys: KEYBOARD_KEYS) -> None:
    """Presses one or more keyboard keys

    :param keys: The keys to be pressed
    :type keys: KEYBOARD_KEYS
    """
    for key in keys:
        pydirectinput.press(key)


@require_focus
def hold_key(*keys: KEYBOARD_KEYS, duration: float) -> None:
    """Holds one or more keyboard keys for a given time

    If more than one key is provided, all keys will be held and released simultaneously

    :param keys: The keys to be held
    :type keys: KEYBOARD_KEYS
    :param duration: How long to hold for, in seconds
    :type duration: float
    """
    for key in keys:
        key_down(key)
    wait(duration)
    for key in keys:
        key_up(key)


keyboard_action = press_key
"""An alias for the press_key function"""

hold_keyboard_action = hold_key
"""An alias for the hold_key function"""


@require_focus
def key_down(key: KEYBOARD_KEYS) -> None:
    """Holds down a key in a non blocking way

    The key will be held until key_up is called for the same key

    :param key: The key to be held down
    :type key: KEYBOARD_KEYS
    """
    pydirectinput.keyDown(key)


@require_focus
def key_up(key: KEYBOARD_KEYS) -> None:
    """Releases a key

    :param key: The key to be released
    :type key: KEYBOARD_KEYS
    """
    pydirectinput.keyUp(key)


__all__ = [
    "press_key",
    "hold_key",
    "keyboard_action",
    "hold_keyboard_action",
    "key_down",
    "key_up",
]
