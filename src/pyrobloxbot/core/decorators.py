from functools import wraps
from pygetwindow import getActiveWindow, getWindowsWithTitle
from win32gui import GetForegroundWindow, GetWindowText

import pyautogui
from ..exceptions import NoRobloxWindowException
from ..bot.bot import state


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
                pyautogui.press("altleft")
                rblxWindow.maximize()
                rblxWindow.activate()

                # Wait for the roblox window to be active
                while getActiveWindow() is None:
                    pass

            return fn(*args, **kwargs)

    return wrapper


def resets_state(fn):
    """This decorator marks functions that have the side effect of reseting the bot's state in game"""

    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        finally:
            state._reset()

    return wrapper


__all__ = [
    "require_focus",
    "resets_state",
]
