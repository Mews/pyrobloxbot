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
    """Toggles the ui navigation mode.

    Note:
        The "UI Navigation Toggle" setting must be enabled on Roblox.
    """
    state._UI_NAV_ENABLED = not state.is_ui_nav_enabled()
    press_key(keybinds.toggle_ui_navigation)


@apply_cooldown()
@require_focus
def enable_ui_navigation() -> None:
    """Enables the ui navigation mode.
    Does nothing if it's already enabled.

    Warning:
        This function relies on pyrobloxbot's internal tracking of whether the ui navigation mode is enabled in game.

        This can sometimes get desynced from what's actually real in game,
        because clicking certain ui elements can turn off the ui navigation mode, and there's no way to track that automatically.

        Be careful of desyncs when using this function.

    Note:
        The "UI Navigation Toggle" setting must be enabled on Roblox.
    """

    if not state.is_ui_nav_enabled():
        toggle_ui_navigation()


@apply_cooldown()
@require_focus
def disable_ui_navigation() -> None:
    """Disables the ui navigation mode.
    Does nothing if it's already disabled.

    Warning:
        This function relies on pyrobloxbot's internal tracking of whether the ui navigation mode is enabled in game.

        This can sometimes get desynced from what's actually real in game,
        because clicking certain ui elements can turn off the ui navigation mode, and there's no way to track that automatically.

        Be careful of desyncs when using this function.

    Note:
        The "UI Navigation Toggle" setting must be enabled on Roblox.
    """
    if state.is_ui_nav_enabled():
        toggle_ui_navigation()


@apply_cooldown()
@require_focus
@requires_ui_navigation_mode
def ui_navigate(*actions: UI_ACTIONS) -> None:
    """Executes the given ui actions in order.

    This function is used for doing entire ui navigation sequences in a single function.

    The actions can include navigating in any of the cardinal directions and clicking on the selected ui element.

    Note:
        The ui navigation mode must be enabled.

    Raises:
        ValueError: Raised when any of the actions provided isn't in :data:`pyrobloxbot.constants.UI_ACTIONS`
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
            raise ValueError("Action must be one of " + str(UI_ACTIONS))


@apply_cooldown()
@require_focus
@requires_ui_navigation_mode
def ui_navigate_up(times: int = 1) -> None:
    """Navigates up in ui elements.

    Note:
        The ui navigation mode must be enabled.

    Args:
        times (int, optional): How many times to navigate up. Defaults to ``1``.
    """
    for _ in range(times):
        ui_navigate("u")


@apply_cooldown()
@require_focus
@requires_ui_navigation_mode
def ui_navigate_left(times: int = 1) -> None:
    """Navigates left in ui elements.

    Note:
        The ui navigation mode must be enabled.

    Args:
        times (int, optional): How many times to navigate left. Defaults to ``1``.
    """
    for _ in range(times):
        ui_navigate("l")


@apply_cooldown()
@require_focus
@requires_ui_navigation_mode
def ui_navigate_right(times: int = 1) -> None:
    """Navigates right in ui elements.

    Note:
        The ui navigation mode must be enabled.

    Args:
        times (int, optional): How many times to navigate right. Defaults to ``1``.
    """
    for _ in range(times):
        ui_navigate("r")


@apply_cooldown()
@require_focus
@requires_ui_navigation_mode
def ui_navigate_down(times: int = 1) -> None:
    """Navigates down in ui elements.

    Note:
        The ui navigation mode must be enabled.

    Args:
        times (int, optional): How many times to navigate down. Defaults to ``1``.
    """
    for _ in range(times):
        ui_navigate("d")


@apply_cooldown()
@require_focus
@requires_ui_navigation_mode
def ui_click() -> None:
    """Click on the currently selected ui element.

    Note:
        The ui navigation mode must be enabled.
    """
    ui_navigate("c")


@apply_cooldown()
@require_focus
@requires_ui_navigation_mode
def ui_scroll_up(ticks: int, interval: float = 0.1) -> None:
    """Scrolls up through selected ui element.

    The ui element itself has to be scrollable. This means you have to have selected the scrollable frame, not one of the
    elements inside it.

    Note:
        The ui navigation mode must be enabled.

    Args:
        ticks (int): How many times to scroll
        interval (float, optional): The delay between each input. Defaults to ``0.1``.

            A lower delay will scroll faster but at some point can lose precision.
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
    """Scrolls down through selected ui element.

    The ui element itself has to be scrollable. This means you have to have selected the scrollable frame, not one of the
    elements inside it.

    Note:
        The ui navigation mode must be enabled.

    Args:
        ticks (int): How many times to scroll
        interval (float, optional): The delay between each input. Defaults to ``0.1``.

            A lower delay will scroll faster but at some point can lose precision.
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
