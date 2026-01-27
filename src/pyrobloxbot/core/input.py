from functools import wraps
from pygetwindow import getActiveWindow, getWindowsWithTitle
from win32gui import GetForegroundWindow, GetWindowText

from ..constants import KEYBOARD_KEYS
from ..exceptions import NoRobloxWindowException

import pydirectinput as dinput
import pyautogui as pg

from ..utils import wait


def require_focus(fn):
    """A decorator that ensures the roblox window is in focus before running the decorated function

    This is already used by all pyrobloxbot functions that require it so you do not have to add it

    :raises NoRobloxWindowException: Raised when can't find a roblox window to focus
    """

    # Fast check to see if roblox window is already focused
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if GetWindowText(GetForegroundWindow()) == "Roblox":
            return fn(*args, **kwargs)

        else:
            rblxWindow = None

            # Find roblox window
            for window in getWindowsWithTitle("Roblox"):
                if window.title == "Roblox":
                    rblxWindow = window

            # Raise error if roblox isn't open
            if rblxWindow is None:
                raise NoRobloxWindowException("You must have roblox opened")

            # Set focus to roblox window
            else:
                pg.press("altleft")
                rblxWindow.maximize()
                rblxWindow.activate()

                # Wait for the roblox window to be active
                while getActiveWindow() is None:
                    pass

            return fn(*args, **kwargs)

    return wrapper


@require_focus
def press_key(*keys: KEYBOARD_KEYS.VALUES):
    """Presses one or more keyboard keys

    :param keys: The keys to be pressed
    :type keys: KEYBOARD_KEYS
    """
    for key in keys:
        dinput.press(key)


@require_focus
def hold_key(*keys: KEYBOARD_KEYS.VALUES, duration: float):
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
def key_down(key: KEYBOARD_KEYS.VALUES):
    """Holds down a key in a non blocking way

    The key will be held until key_up is called for the same key

    :param key: The key to be held down
    :type key: KEYBOARD_KEYS
    """
    dinput.keyDown(key)


@require_focus
def key_up(key: KEYBOARD_KEYS.VALUES):
    """Releases a key

    :param key: The key to be released
    :type key: KEYBOARD_KEYS
    """
    dinput.keyUp(key)


__all__ = [
    "require_focus",
    "press_key",
    "hold_key",
    "keyboard_action",
    "hold_keyboard_action",
    "key_down",
    "key_up",
]
