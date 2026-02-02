from ..exceptions import InvalidUiActionException
from ..constants.ui_actions import (
    UI_ACTIONS,
    UI_NAVIGATE_DOWN_ACTIONS,
    UI_NAVIGATE_LEFT_ACTIONS,
    UI_NAVIGATE_RIGHT_ACTIONS,
    UI_NAVIGATE_UP_ACTIONS,
    UI_CLICK_ACTIONS,
)
from .input import press_key
from .decorators import require_focus, requires_ui_navigation_mode, apply_cooldown
from ..bot.bot import state, keybinds
from pynput.keyboard import Controller, Key
from ..utils import wait
from typing import get_args


@apply_cooldown()
@require_focus
def toggle_ui_navigation() -> None:
    """Toggles ui navigation mode.

    This is called by all ui navigation functions if ui navigation mode is disabled.

    You can change the key used to toggle this mode by changing the module's UI_NAV_KEY variable

    The "UI Navigation Toggle" setting must be enabled on Roblox
    """
    state._UI_NAV_ENABLED = not state.is_ui_nav_enabled()
    press_key(keybinds.toggle_ui_navigation)


@apply_cooldown()
@require_focus
def enable_ui_navigation() -> None:
    if not state.is_ui_nav_enabled():
        toggle_ui_navigation()


@apply_cooldown()
@require_focus
def disable_ui_navigation() -> None:
    if state.is_ui_nav_enabled():
        toggle_ui_navigation()


@apply_cooldown()
@require_focus
@requires_ui_navigation_mode
def ui_navigate(*actions: UI_ACTIONS) -> None:
    """Navigates through roblox ui in specified direction

    :param direction: The direction to navigate in
    :type direction: UI_ACTIONS
    :raises InvalidUiDirectionException: Raised if direction isn't one of
    """
    for action in actions:
        a = action.lower().strip()

        if a in get_args(UI_NAVIGATE_UP_ACTIONS):
            press_key(keybinds.ui_navigate_up)

        elif a in get_args(UI_NAVIGATE_LEFT_ACTIONS):
            press_key(keybinds.ui_navigate_left)

        elif a in get_args(UI_NAVIGATE_RIGHT_ACTIONS):
            press_key(keybinds.ui_navigate_right)

        elif a in get_args(UI_NAVIGATE_DOWN_ACTIONS):
            press_key(keybinds.ui_navigate_down)

        elif a in get_args(UI_CLICK_ACTIONS):
            press_key(keybinds.ui_click)

        else:
            raise InvalidUiActionException("Action must be one of " + str(UI_ACTIONS))


@apply_cooldown()
@require_focus
@requires_ui_navigation_mode
def ui_navigate_up(times: int = 1) -> None:
    """Navigate up in ui elements"""
    for _ in range(times):
        ui_navigate("u")


@apply_cooldown()
@require_focus
@requires_ui_navigation_mode
def ui_navigate_left(times: int = 1) -> None:
    """Navigate left in ui elements"""
    for _ in range(times):
        ui_navigate("l")


@apply_cooldown()
@require_focus
@requires_ui_navigation_mode
def ui_navigate_right(times: int = 1) -> None:
    """Navigate right in ui elements"""
    for _ in range(times):
        ui_navigate("r")


@apply_cooldown()
@require_focus
@requires_ui_navigation_mode
def ui_navigate_down(times: int = 1) -> None:
    """Navigate down in ui elements"""
    for _ in range(times):
        ui_navigate("d")


@apply_cooldown()
@require_focus
@requires_ui_navigation_mode
def ui_click() -> None:
    """Click on currently selected ui element"""
    ui_navigate("c")


@apply_cooldown()
@require_focus
@requires_ui_navigation_mode
def ui_scroll_up(ticks: int, interval: float = 0.1) -> None:
    """Scrolls up through selected ui element

    The ui element itself has to be scrollable

    :param ticks: How many times to scroll
    :type ticks: int
    :param interval: The delay between each input, defaults to 0.1\n
                  A lower delay will scroll faster but at some point can lose precision
    :type interval: float, optional
    """
    kb = Controller()
    for _ in range(ticks):
        kb.press(Key.page_up)
        kb.release(Key.page_up)
        wait(interval)


@apply_cooldown()
@require_focus
@requires_ui_navigation_mode
def ui_scroll_down(ticks: int, interval: float = 0.1) -> None:
    """Scrolls down in selected ui element

    :param ticks: How many times to scroll
    :type ticks: int
    :param interval: The delay between each input, defaults to 0.1\n
                  A lower delay will scroll faster but at some point can lose precision
    :type interval: float, optional
    """
    kb = Controller()
    for _ in range(ticks):
        kb.press(Key.page_down)
        kb.release(Key.page_down)
        wait(interval)


__all__ = [
    "toggle_ui_navigation",
    "enable_ui_navigation",
    "disable_ui_navigation",
    "ui_navigate",
    "ui_navigate_up",
    "ui_navigate_down",
    "ui_navigate_left",
    "ui_navigate_right",
    "ui_click",
    "ui_scroll_up",
    "ui_scroll_down",
]
