import time
from typing import Optional
from pynput import keyboard
import _thread
import sys


def sleep(seconds: float) -> None:
    start = time.perf_counter()

    while time.perf_counter() - start < seconds:
        time.sleep(0.05)


def wait(seconds: float) -> None:
    """Suspend execution for a given number of seconds.

    Important:
        You should use this method instead of ``time.sleep`` for manually adding delays in your bot.

        This is because the failsafe will only work reliably if you use this method. Otherwise, hitting the failsafe
        hotkey while ``time.sleep`` is running will cause the failsafe to not be triggered.

    Args:
        seconds (float): How long to wait for.
    """
    sleep(seconds)


def build_roblox_uri(
    placeId: Optional[int] = None,
    userId: Optional[int] = None,
    linkCode: Optional[int] = None,
    gameInstanceId: Optional[str] = None,
    type: Optional[str] = None,
) -> str:
    """Utility for generating Roblox uris with parameters

    Args:
        placeId (int, optional): The id of the game. This is required for everything except joining a user's game
        userId (int, optional): The id of a Roblox user. If you're allowed to join them,
            either because they added you as a friend or their joins are public, you'll join their game
        linkCode (int, optional): The code for a private server. This is not the code that appears
            in the invite link for a private server.
            Rather, one way to get this code is by pasting a private server invite link on the browser.
            The browser will eventually redirect to a link like
            "https://www.roblox.com/games/<place id>/<place name>?privateServerLinkCode=<linkCode>"
            The parameter to use is the one in privateServerLinkCode
        gameInstanceId (str, optional): The id of a particular server. There's no way to view them on the base site, and they are ephemeral.
        If you own the experience you may print game.JobId to the console
        type (str, optional): The type of join, either "InGame" or "FollowUser"

    Returns:
        str: A Roblox uri that can be passed to start

    """
    params = []

    if placeId:
        params.append(f"placeId={placeId}")
    if userId:
        params.append(f"userId={userId}")
    if linkCode:
        params.append(f"linkCode={linkCode}")
    if gameInstanceId:
        params.append(f"gameInstanceId={gameInstanceId}")
    if type:
        params.append(f"type={type}")

    return "roblox://experiences/start?" + "&".join(params)


def parse_special_key_for_pynput(key: str) -> str:
    if hasattr(keyboard.Key, key):
        return f"<{key}>"
    return key


def _failsafe():
    try:
        old_hook = sys.excepthook

        def failsafe_excepthook(exc_type, exc, tb):
            old_hook(exc_type, exc, tb)

            from .bot.bot import keybinds

            if exc_type is KeyboardInterrupt:
                failsafe_hotkey = keybinds._FAILSAFE_HOTKEY
                print(f"""Failsafe triggered ({failsafe_hotkey})
If you didn't mean for this to happen, you might have pressed {failsafe_hotkey} on accident, or made your bot press it
You can change the failsafe hotkey through set_failsafe_hotkey
For more info see the documentation for pyrobloxbot.keybinds.set_failsafe_hotkey
""")

        sys.excepthook = failsafe_excepthook
    finally:
        _thread.interrupt_main()


__all__ = ["wait"]
