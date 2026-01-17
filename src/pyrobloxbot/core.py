from __future__ import annotations

import _thread
import os
from functools import wraps
from time import sleep as wait

import keyboard as kb
import pydirectinput as dinput
import pyautogui as pg
import pyperclip as pyclip
from pynput.keyboard import Controller, Key
from pygetwindow import getActiveWindow, getWindowsWithTitle
from win32gui import GetForegroundWindow, GetWindowText

from .exceptions import (
    InvalidSlotNumberException,
    InvalidUiDirectionException,
    InvalidWalkDirectionException,
    NoRobloxWindowException,
)
from .literals import KEYBOARD_KEYS, UI_NAVIGATE_DIRECTIONS, WALK_DIRECTIONS

UI_NAV_ENABLED = False
UI_NAV_KEY = "\\"
"""The key that is used by toggle_ui_navigation to turn on the ui navigation mode"""

FAILSAFE_HOTKEY = "ctrl+m"

kb.add_hotkey(FAILSAFE_HOTKEY, _thread.interrupt_main)


def set_failsafe_hotkey(*keys: KEYBOARD_KEYS.VALUES):
    """Changes hotkey required to trigger the failsafe

    The default hotkey is control + m

    :param keys: The key combination for triggering the failsafe
    :type keys: KEYBOARD_KEYS
    """
    global FAILSAFE_HOTKEY

    kb.clear_hotkey(FAILSAFE_HOTKEY)

    FAILSAFE_HOTKEY = ""
    for key in keys:
        key = kb._canonical_names.normalize_name(key)
        FAILSAFE_HOTKEY += key
        FAILSAFE_HOTKEY += "+"

    FAILSAFE_HOTKEY = FAILSAFE_HOTKEY[:-1]

    kb.add_hotkey(FAILSAFE_HOTKEY, _thread.interrupt_main)


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
def keyboard_action(*actions: KEYBOARD_KEYS.VALUES):
    """Presses one or more keyboard keys

    :param actions: The keys to be pressed
    :type actions: KEYBOARD_KEYS
    """
    for action in actions:
        dinput.press(action)


@require_focus
def hold_keyboard_action(*actions: KEYBOARD_KEYS.VALUES, duration: float):
    """Holds one or more keyboard keys for a given time

    If more than one key is provided, all keys will be held and released simultaneously

    :param actions: The keys to be held
    :type actions: KEYBOARD_KEYS
    :param duration: How long to hold for, in seconds
    :type duration: float
    """
    for action in actions:
        dinput.keyDown(action)
    wait(duration)
    for action in actions:
        dinput.keyUp(action)


press_key = keyboard_action
"""An alias for the keyboard_action function"""

hold_key = hold_keyboard_action
"""An alias for the hold_keyboard_action function"""


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


@require_focus
def walk(*directions: WALK_DIRECTIONS.VALUES, duration: float):
    """Walks in one or more directions for a given time

    If more than one direction is given it will walk diagonally

    :param directions: The directions to walk in
    :type directions: WALK_DIRECTIONS
    :param duration: How long to walk for, in seconds
    :type duration: float
    :raises InvalidWalkDirectionException: Raised when given directions aren't one of literals.WALK_DIRECTIONS.VALUES
    """

    forwardDirections = ["f", "fw", "forward", "forwards"]
    leftDirections = ["l", "left"]
    rightDirections = ["r", "right"]
    backDirections = ["b", "back", "backward", "backwards"]

    ## Check if all directions are valid
    for direction in directions:
        d = direction.lower().strip()

        if d in forwardDirections:
            pass
        elif d in leftDirections:
            pass
        elif d in rightDirections:
            pass
        elif d in backDirections:
            pass
        else:
            raise InvalidWalkDirectionException(
                "Direction must be one of " + str(WALK_DIRECTIONS.VALUES)
            )

    # Hold down keys
    for direction in directions:
        d = direction.lower().strip()

        if d in forwardDirections:
            dinput.keyDown("w")
        elif d in leftDirections:
            dinput.keyDown("a")
        elif d in rightDirections:
            dinput.keyDown("d")
        elif d in backDirections:
            dinput.keyDown("s")

    wait(duration)

    # Release keys
    for direction in directions:
        d = direction.lower().strip()

        if d in forwardDirections:
            dinput.keyUp("w")
        elif d in leftDirections:
            dinput.keyUp("a")
        elif d in rightDirections:
            dinput.keyUp("d")
        elif d in backDirections:
            dinput.keyUp("s")


@require_focus
def walk_forward(duration: float):
    """Walks forward for a given time

    :param duration: How long to walk for, in seconds
    :type duration: float
    """
    dinput.keyDown("w")
    wait(duration)
    dinput.keyUp("w")


@require_focus
def walk_left(duration: float):
    """Walks left for a given time

    :param duration: How long to walk for, in seconds
    :type duration: float
    """
    dinput.keyDown("a")
    wait(duration)
    dinput.keyUp("a")


@require_focus
def walk_right(duration: float):
    """Walks right for a given time

    :param duration: How long to walk for, in seconds
    :type duration: float
    """
    dinput.keyDown("d")
    wait(duration)
    dinput.keyUp("d")


@require_focus
def walk_back(duration: float):
    """Walks back for a given time

    :param duration: How long to walk for, in seconds
    :type duration: float
    """
    dinput.keyDown("s")
    wait(duration)
    dinput.keyUp("s")


@require_focus
def jump(number_of_jumps: int = 1, delay: float = 0):
    """Jumps for a given number of times

    :param number_of_jumps: How many times to jump, defaults to 1
    :type number_of_jumps: int
    :param delay: How much time between jumps, in seconds, defaults to 0
    :type delay: float
    """
    for i in range(number_of_jumps):
        dinput.press("space")
        wait(delay)


@require_focus
def jump_continuous(duration: float):
    """Holds jump for a given time

    :param duration: How long to hold jump for, in seconds
    :type duration: float
    """
    dinput.keyDown("space")
    wait(duration)
    dinput.keyUp("space")


@require_focus
def reset_player(interval: float = 0.5):
    """Resets player character

    :param interval: How long between each keyboard input, in seconds, defaults to 0.5
    :type interval: float
    """
    dinput.press(("esc", "r", "enter"), interval=interval)


@require_focus
def leave_game(interval: float = 0.5):
    """Leaves the current game

    :param interval: How long between each keyboard input, in seconds, defaults to 0.5
    :type interval: float
    """
    global UI_NAV_ENABLED
    dinput.press(("esc", "l", "enter"), interval=interval)
    UI_NAV_ENABLED = False


@require_focus
def toggle_shift_lock():
    """Toggles shift lock (Shift lock switch must be enabled in roblox settings)"""
    dinput.press("shift")


@require_focus
def chat(message: str):
    """Sends a message in chat

    :param message: The message to send
    :type message: str
    """
    # Open chat
    dinput.press("/")

    # Use clipboard to paste message quickly
    previousClipboard = pyclip.paste()

    pyclip.copy(message)
    dinput.keyDown("ctrl")
    dinput.keyDown("v")
    dinput.keyUp("ctrl")
    dinput.keyUp("v")

    dinput.press("enter")

    toggle_shift_lock()

    # Restore previous clipboard content
    pyclip.copy(previousClipboard)


@require_focus
def toggle_ui_navigation():
    """Toggles ui navigation mode.

    This is called by all ui navigation functions if ui navigation mode is disabled.

    You can change the key used to toggle this mode by changing the module's UI_NAV_KEY variable

    The "UI Navigation Toggle" setting must be enabled on Roblox
    """
    global UI_NAV_ENABLED
    UI_NAV_ENABLED = not UI_NAV_ENABLED
    dinput.press(UI_NAV_KEY)


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
        ui_navigate_up()

    elif d in left_directions:
        ui_navigate_left()

    elif d in right_directions:
        ui_navigate_right()

    elif d in down_directions:
        ui_navigate_left()

    else:
        raise InvalidUiDirectionException(
            "Direction must be one of " + str(UI_NAVIGATE_DIRECTIONS.VALUES)
        )


@require_focus
def ui_navigate_up():
    """Navigate up in ui elements"""
    if not UI_NAV_ENABLED:
        toggle_ui_navigation()

    dinput.press("up")


@require_focus
def ui_navigate_left():
    """Navigate left in ui elements"""
    if not UI_NAV_ENABLED:
        toggle_ui_navigation()

    dinput.press("left")


@require_focus
def ui_navigate_right():
    """Navigate right in ui elements"""
    if not UI_NAV_ENABLED:
        toggle_ui_navigation()

    dinput.press("right")


@require_focus
def ui_navigate_down():
    """Navigate down in ui elements"""
    if not UI_NAV_ENABLED:
        toggle_ui_navigation()

    dinput.press("down")


@require_focus
def ui_click():
    """Click on currently selected ui element"""
    if not UI_NAV_ENABLED:
        toggle_ui_navigation()

    dinput.press("enter")


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
    if not UI_NAV_ENABLED:
        toggle_ui_navigation()

    kb = Controller()
    for i in range(ticks):
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
    if not UI_NAV_ENABLED:
        toggle_ui_navigation()

    kb = Controller()
    for i in range(ticks):
        kb.press(Key.page_down)
        kb.release(Key.page_down)
        wait(delay)


@require_focus
def equip_slot(slot: int):
    """Equip a given item slot

    :param slot: The item slot to equip
    :type slot: int
    :raises InvalidSlotNumberException: Raised when slot isn't between 0 and 9
    """
    if slot < 0 or slot > 9:
        raise InvalidSlotNumberException("Slots should be between 0 and 9")

    dinput.press(str(slot))


def launch_game(game_id: int):
    """Launches a roblox game

    There can be a few seconds of delay between calling this function and the game opening

    :param game_id: The id of the roblox game to launch
    :type game_id: int
    """
    command = "start roblox://placeId=" + str(game_id)
    os.system(command=command)

    global UI_NAV_ENABLED
    UI_NAV_ENABLED = False


@require_focus
def image_is_visible(image_path: str, confidence: float = 0.9) -> bool:
    """Checks whether a given image is visible in the roblox window

    :param image_path: The path to the image file to check
    :type image_path: str
    :param confidence: How confident the function has to be to return True, must be between 0 and 0.999, defaults to 0.9\n
                       If this value is too low it may give false positives

    :type confidence: float, optional
    :return: Whether or not the image is visible
    :rtype: bool
    """

    try:
        pg.locateOnScreen(image_path, confidence=confidence)
        return True
    except pg.ImageNotFoundException:
        return False


__all__ = [
    "UI_NAV_ENABLED",
    "UI_NAV_KEY",
    "FAILSAFE_HOTKEY",
    "set_failsafe_hotkey",
    "require_focus",
    "keyboard_action",
    "hold_keyboard_action",
    "press_key",
    "hold_key",
    "key_down",
    "key_up",
    "walk",
    "walk_forward",
    "walk_left",
    "walk_right",
    "walk_back",
    "jump",
    "jump_continuous",
    "reset_player",
    "leave_game",
    "toggle_shift_lock",
    "chat",
    "toggle_ui_navigation",
    "ui_navigate",
    "ui_navigate_up",
    "ui_navigate_left",
    "ui_navigate_right",
    "ui_navigate_down",
    "ui_click",
    "ui_scroll_up",
    "ui_scroll_down",
    "equip_slot",
    "launch_game",
    "image_is_visible",
]
