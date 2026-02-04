from ..constants import KEYBOARD_KEYS

import pydirectinput

from ..utils import wait
from .decorators import require_focus, apply_cooldown


@apply_cooldown()
@apply_cooldown(per_key=True)
@require_focus
def press_key(*keys: KEYBOARD_KEYS) -> None:
    """Presses the given keys in order

    Args:
        *keys (KEYBOARD_KEYS): The keys to be pressed
    """
    for key in keys:
        pydirectinput.press(key)


@apply_cooldown()
@require_focus
def hold_key(*keys: KEYBOARD_KEYS, duration: float) -> None:
    """Hold the given keys for a given duration

    Args:
        *keys (KEYBOARD_KEYS): The keys to hold
        duration (float): How long to hold the keys for
    """
    key_down(*keys)
    wait(duration)
    key_up(*keys)


keyboard_action = press_key
"""An alias for the press_key function"""

hold_keyboard_action = hold_key
"""An alias for the hold_key function"""


@apply_cooldown()
@require_focus
def key_down(*keys: KEYBOARD_KEYS) -> None:
    """Puts down the given keys, in a non blocking way.

    The keys will remain pressed until :func:`pyrobloxbot.key_up` is called for them.

    Args:
        *keys (KEYBOARD_KEYS): The keys to put down
    """
    for key in keys:
        pydirectinput.keyDown(key)


@apply_cooldown()
@apply_cooldown(per_key=True)
@require_focus
def key_up(*keys: KEYBOARD_KEYS) -> None:
    """Releases the given keys.

    Args:
        *keys (KEYBOARD_KEYS): The keys to release.
    """
    for key in keys:
        pydirectinput.keyUp(key)


__all__ = [
    "press_key",
    "hold_key",
    "keyboard_action",
    "hold_keyboard_action",
    "key_down",
    "key_up",
]
