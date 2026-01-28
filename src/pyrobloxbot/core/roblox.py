from ..bot.bot import state
from .input import require_focus, press_key
from ..utils import wait

import os


@require_focus
def leave_game(interval: float = 0.5):
    """Leaves the current game

    :param interval: How long between each keyboard input, in seconds, defaults to 0.5
    :type interval: float
    """
    press_key("esc")
    wait(interval)
    press_key("l")
    wait(interval)
    press_key("enter")

    state._ui_nav_enabled = False


def launch_game(game_id: int):
    """Launches a roblox game

    There can be a few seconds of delay between calling this function and the game opening

    :param game_id: The id of the roblox game to launch
    :type game_id: int
    """
    command = "start roblox://placeId=" + str(game_id)
    os.system(command=command)

    state._ui_nav_enabled = False


__all__ = ["leave_game", "launch_game"]
