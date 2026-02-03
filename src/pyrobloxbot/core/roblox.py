from .input import press_key
from .decorators import require_focus, resets_state, apply_cooldown
from ..utils import wait, build_roblox_uri

import os


@apply_cooldown()
@require_focus
@resets_state
def leave_game(interval: float = 0) -> None:
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
def join_game(game_id: int) -> None:
    """Launches a roblox game

    There can be a few seconds of delay between calling this function and the game opening

    :param game_id: The id of the roblox game to launch
    :type game_id: int
    """
    uri = build_roblox_uri(placeId=game_id, type="InGame")
    command = f'start "" "{uri}"'
    os.system(command=command)


@apply_cooldown()
@resets_state
def join_user(user_id: int) -> None:
    uri = build_roblox_uri(userId=user_id, type="FollowUser")
    command = f'start "" "{uri}"'
    os.system(command=command)


@apply_cooldown()
@resets_state
def join_private_server(game_id: int, private_server_link_code: int) -> None:
    uri = build_roblox_uri(
        placeId=game_id, linkCode=private_server_link_code, type="InGame"
    )
    command = f'start "" "{uri}"'
    os.system(command=command)


@apply_cooldown()
@resets_state
def join_server(game_id: int, job_id: str) -> None:
    uri = build_roblox_uri(placeId=game_id, gameInstanceId=job_id, type="InGame")
    command = f'start "" "{uri}"'
    os.system(command=command)


__all__ = ["leave_game", "join_game", "join_user", "join_private_server", "join_server"]
