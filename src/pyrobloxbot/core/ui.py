from ..exceptions import InvalidUiDirectionException
from ..constants import UI_NAVIGATE_DIRECTIONS
from .input import require_focus, press_key
from ..bot.bot import state
from pynput.keyboard import Controller, Key
from ..utils import wait


@require_focus
def toggle_ui_navigation():
    """Toggles ui navigation mode.

    This is called by all ui navigation functions if ui navigation mode is disabled.

    You can change the key used to toggle this mode by changing the module's UI_NAV_KEY variable

    The "UI Navigation Toggle" setting must be enabled on Roblox
    """
    state.ui_nav_enabled = not state.ui_nav_enabled
    press_key("\\")


def ui_navigate(direction: UI_NAVIGATE_DIRECTIONS.VALUES):
    """Navigates through roblox ui in specified direction

    :param direction: The direction to navigate in
    :type direction: UI_NAVIGATE_DIRECTIONS
    :raises InvalidUiDirectionException: Raised if direction isn't one of
    """
    d = direction.lower().strip()

    up_directions = ["up", "u"]
    left_directions = ["left", "l"]
    right_directions = ["right", "r"]
    down_directions = ["down", "d"]

    if d in up_directions:
        press_key("up")

    elif d in left_directions:
        press_key("left")

    elif d in right_directions:
        press_key("right")

    elif d in down_directions:
        press_key("down")

    else:
        raise InvalidUiDirectionException(
            "Direction must be one of " + str(UI_NAVIGATE_DIRECTIONS.VALUES)
        )


@require_focus
def ui_navigate_up():
    """Navigate up in ui elements"""
    if not state.ui_nav_enabled:
        toggle_ui_navigation()

    ui_navigate("u")


@require_focus
def ui_navigate_left():
    """Navigate left in ui elements"""
    if not state.ui_nav_enabled:
        toggle_ui_navigation()

    ui_navigate("l")


@require_focus
def ui_navigate_right():
    """Navigate right in ui elements"""
    if not state.ui_nav_enabled:
        toggle_ui_navigation()

    ui_navigate("r")


@require_focus
def ui_navigate_down():
    """Navigate down in ui elements"""
    if not state.ui_nav_enabled:
        toggle_ui_navigation()

    ui_navigate("d")


@require_focus
def ui_click():
    """Click on currently selected ui element"""
    if not state.ui_nav_enabled:
        toggle_ui_navigation()

    press_key("enter")


@require_focus
def ui_scroll_up(ticks: int, delay: float = 0.1):
    """Scrolls up through selected ui element

    The ui element itself has to be scrollable

    :param ticks: How many times to scroll
    :type ticks: int
    :param delay: The delay between each input, defaults to 0.1\n
                  A lower delay will scroll faster but at some point can lose precision
    :type delay: float, optional
    """
    if not state.ui_nav_enabled:
        toggle_ui_navigation()

    kb = Controller()
    for _ in range(ticks):
        kb.press(Key.page_up)
        kb.release(Key.page_up)
        wait(delay)


@require_focus
def ui_scroll_down(ticks: int, delay: float = 0.1):
    """Scrolls down in selected ui element

    :param ticks: How many times to scroll
    :type ticks: int
    :param delay: The delay between each input, defaults to 0.1\n
                  A lower delay will scroll faster but at some point can lose precision
    :type delay: float, optional
    """
    if not state.ui_nav_enabled:
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
