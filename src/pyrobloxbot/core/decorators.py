from functools import wraps
from pygetwindow import getActiveWindow, getWindowsWithTitle
from win32gui import GetForegroundWindow, GetWindowText

import pydirectinput
from ..exceptions import NoRobloxWindowException
from ..bot.bot import state, options
from ..utils import wait


def require_focus(fn):
    """Decorator that ensures the roblox window is in focus before running the decorated function.

    It is affected by the options ``force_focus`` and ``maximize_roblox_window``.

    If ``maximize_roblox_window`` is set to ``True``, the decorator will maximize the roblox window on top of activating it before
    running the decorated function.

    If ``force_focus`` is set to ``False``, instead of activating the Roblox window, the decorator will only check if
    it is already in focus. If it is, it runs the decorated function. If it isn't it doesn't run anything.

    Important:
        Be aware that if `force_focus` is ``False`` and the decorator skips the function because Roblox isn't in focus,
        the function's return value will be ``None``.

    Raises:
        NoRobloxWindowException: Raised if the decorator can't find the Roblox window to activate.
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
    """Decorator that resets the bot's internal state after running the decorated function.

    Used for methods like :func:`pyrobloxbot.leave_game` and
    :func:`pyrobloxbot.join_game`, that cause the characters state to be reset ingame.
    This needs to be replicated in the bot's internal state.
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        finally:
            state._reset()

    return wrapper


def requires_ui_navigation_mode(fn):
    """This decorator ensures ui navigation mode is enabled on roblox before running the decorated function.

    After the function is done, it returns to the original state, meaning if ui navigation was disabled before
    the function was called it'll go back to being disabled, if it was already enabled it'll stay enabled.

    All functions in :mod:`pyrobloxbot.core.ui` use this decorator.
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
    """Decorator that applies a cooldown after the decorated function is executed

    Args:
        per_key (bool, optional): Defaults to ``False``.

            If set to ``False``, the applied delay will be the one set in :data:`pyrobloxbot.options.action_cooldown`.
            In this case, there is also a failsafe to ensure that nested calls to functions using this decorator don't
            cause multiple cooldowns to be applied. The cooldown is only applied to the first decorated function that's called.

            If set to ``True``, the applied delay will be the one set in :data:`pyrobloxbot.options.key_press_cooldown`.
    """

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
