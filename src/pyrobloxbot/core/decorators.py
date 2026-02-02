from functools import wraps
from pygetwindow import getActiveWindow, getWindowsWithTitle
from win32gui import GetForegroundWindow, GetWindowText

import pydirectinput
from ..exceptions import NoRobloxWindowException
from ..bot.bot import state, options
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

        elif not options.force_focus:
            return None

        else:
            rblx_window = None
            previous_window = getActiveWindow()

            # Find roblox window
            for window in getWindowsWithTitle("Roblox"):
                if window.title == "Roblox":
                    rblx_window = window

            # Raise error if roblox isn't open
            if rblx_window is None:
                raise NoRobloxWindowException("You must have roblox opened")

            # Set focus to roblox window
            else:
                pydirectinput.press("altleft")
                if options.maximize_roblox_window:
                    rblx_window.maximize()
                rblx_window.activate()

                # Wait for the roblox window to be active
                while getActiveWindow() is None:
                    pass

            retv = fn(*args, **kwargs)

            if options.restore_focus_after_action:
                pydirectinput.press("altleft")
                previous_window.activate()

            return retv

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


def requires_ui_navigation_mode(fn):
    """This decorator ensures ui navigation mode is enabled on roblox before running the decorated function
    After the function is done, it returns to the original state, meaning if ui navigation was disabled before the function was called it'll go back to being disabled, if it was already enabled it'll stay enabled
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        from . import ui

        original_is_ui_nav_enabled = state.is_ui_nav_enabled()

        if not original_is_ui_nav_enabled:
            ui.toggle_ui_navigation()

        try:
            return fn(*args, **kwargs)
        finally:
            if state.is_ui_nav_enabled() != original_is_ui_nav_enabled:
                ui.toggle_ui_navigation()

    return wrapper


def apply_cooldown(per_key: bool = False):  # type: ignore[no-untyped-def]
    """This decorator applies the cooldown defined in bot.options.action_cooldown at the end of the decorated function"""

    def decorator(fn):
        if not per_key:

            @wraps(fn)
            def wrapper(*args, **kwargs):
                if state._COOLDOWN_SET:
                    return fn(*args, **kwargs)

                state._COOLDOWN_SET = True

                try:
                    retv = fn(*args, **kwargs)

                    if options.action_cooldown > 0:
                        wait(options.action_cooldown)

                    return retv

                finally:
                    state._COOLDOWN_SET = False

            return wrapper

        if per_key:

            @wraps(fn)
            def wrapper(*args, **kwargs):
                retv = fn(*args, **kwargs)

                if options.key_press_cooldown > 0:
                    wait(options.key_press_cooldown)

                return retv

            return wrapper

    return decorator


__all__ = [
    "require_focus",
    "resets_state",
    "requires_ui_navigation_mode",
    "apply_cooldown",
]
