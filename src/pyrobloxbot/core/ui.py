from ..exceptions import InvalidUiDirectionException
from ..constants.ui_navigate_directions import (
    UI_NAVIGATE_DIRECTIONS,
    UI_NAVIGATE_DOWN_DIRECTIONS,
    UI_NAVIGATE_LEFT_DIRECTIONS,
    UI_NAVIGATE_RIGHT_DIRECTIONS,
    UI_NAVIGATE_UP_DIRECTIONS,
)
from .input import require_focus, press_key
from ..bot.bot import state, keybinds
from pynput.keyboard import Controller, Key
from ..utils import wait
from typing import get_args


@require_focus
def toggle_ui_navigation() -> None:
    """Toggles ui navigation mode.

    This is called by all ui navigation functions if ui navigation mode is disabled.

    You can change the key used to toggle this mode by changing the module's UI_NAV_KEY variable

    The "UI Navigation Toggle" setting must be enabled on Roblox
    """
    state._UI_NAV_ENABLED = not state.is_ui_nav_enabled()
    press_key(keybinds.toggle_ui_navigation)


def ui_navigate(direction: UI_NAVIGATE_DIRECTIONS) -> None:
    """Navigates through roblox ui in specified direction

    :param direction: The direction to navigate in
    :type direction: UI_NAVIGATE_DIRECTIONS
    :raises InvalidUiDirectionException: Raised if direction isn't one of
    """
    if not state.is_ui_nav_enabled():
        toggle_ui_navigation()

    d = direction.lower().strip()

    if d in get_args(UI_NAVIGATE_UP_DIRECTIONS):
        press_key(keybinds.ui_navigate_up)

    elif d in get_args(UI_NAVIGATE_LEFT_DIRECTIONS):
        press_key(keybinds.ui_navigate_left)

    elif d in get_args(UI_NAVIGATE_RIGHT_DIRECTIONS):
        press_key(keybinds.ui_navigate_right)

    elif d in get_args(UI_NAVIGATE_DOWN_DIRECTIONS):
        press_key(keybinds.ui_navigate_down)

    else:
        raise InvalidUiDirectionException(
            "Direction must be one of " + str(UI_NAVIGATE_DIRECTIONS)
        )


@require_focus
def ui_navigate_up() -> None:
    """Navigate up in ui elements"""
    ui_navigate("u")


@require_focus
def ui_navigate_left() -> None:
    """Navigate left in ui elements"""
    ui_navigate("l")


@require_focus
def ui_navigate_right() -> None:
    """Navigate right in ui elements"""
    ui_navigate("r")


@require_focus
def ui_navigate_down() -> None:
    """Navigate down in ui elements"""
    ui_navigate("d")


@require_focus
def ui_click() -> None:
    """Click on currently selected ui element"""
    if not state.is_ui_nav_enabled():
        toggle_ui_navigation()

    press_key(keybinds.ui_click)


@require_focus
def ui_scroll_up(ticks: int, delay: float = 0.1) -> None:
    """Scrolls up through selected ui element

    The ui element itself has to be scrollable

    :param ticks: How many times to scroll
    :type ticks: int
    :param delay: The delay between each input, defaults to 0.1\n
                  A lower delay will scroll faster but at some point can lose precision
    :type delay: float, optional
    """
    if not state.is_ui_nav_enabled():
        toggle_ui_navigation()

    kb = Controller()
    for _ in range(ticks):
        kb.press(Key.page_up)
        kb.release(Key.page_up)
        wait(delay)


@require_focus
def ui_scroll_down(ticks: int, delay: float = 0.1) -> None:
    """Scrolls down in selected ui element

    :param ticks: How many times to scroll
    :type ticks: int
    :param delay: The delay between each input, defaults to 0.1\n
                  A lower delay will scroll faster but at some point can lose precision
    :type delay: float, optional
    """
    if not state.is_ui_nav_enabled():
        toggle_ui_navigation()

    kb = Controller()
    for _ in range(ticks):
        kb.press(Key.page_down)
        kb.release(Key.page_down)
        wait(delay)


__all__ = [
    "toggle_ui_navigation",
    "ui_navigate",
    "ui_navigate_up",
    "ui_navigate_down",
    "ui_navigate_left",
    "ui_navigate_right",
    "ui_click",
    "ui_scroll_up",
    "ui_scroll_down",
]
