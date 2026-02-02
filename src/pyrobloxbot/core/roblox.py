from .input import press_key
from .decorators import require_focus, resets_state, apply_cooldown
from ..utils import wait

import os


@apply_cooldown()
@require_focus
@resets_state
def leave_game(interval: float = 0.5) -> None:
    """Leaves the current game

    :param interval: How long between each keyboard input, in seconds, defaults to 0.5
    :type interval: float
    """
    press_key("esc")
    wait(interval)
    press_key("l")
    wait(interval)
    press_key("enter")


@apply_cooldown()
@resets_state
def launch_game(game_id: int) -> None:
    """Launches a roblox game

    There can be a few seconds of delay between calling this function and the game opening

    :param game_id: The id of the roblox game to launch
    :type game_id: int
    """
    command = "start roblox://placeId=" + str(game_id)
    os.system(command=command)


__all__ = ["leave_game", "launch_game"]
