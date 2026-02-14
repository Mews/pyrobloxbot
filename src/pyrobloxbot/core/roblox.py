from .input import press_key
from .decorators import require_focus, resets_state, apply_cooldown
from ..utils import wait, build_roblox_uri

import os


@apply_cooldown()
@require_focus
@resets_state
def leave_game(interval: float = 0) -> None:
    """Leaves the current game.

    Args:
        interval (float, optional): How long to wait in between each key press.
            Defaults to ``0``.

            Usually it should be fine, but change it to a higher value if you find it unreliable.
    """
    press_key("esc")
    wait(interval)
    press_key("l")
    wait(interval)
    press_key("enter")


@apply_cooldown()
@resets_state
def join_game(game_id: int) -> None:
    """Launches a Roblox game.

    Note:
        The time it takes for the game to launch is entirely variable.

        It is usually recomended to use :func:`pyrobloxbot.image_is_visible` to detect when the game has finished launching.

    Args:
        game_id (int): The id of the game to join.

            This can be found in the url for the game, which has the format ``https://www.roblox.com/games/<Game Id>/<Game Name>``.
            The game id will be a random looking number.
    """
    uri = build_roblox_uri(placeId=game_id, type="InGame")
    command = f'start "" "{uri}"'
    os.system(command=command)


@apply_cooldown()
@resets_state
def join_user(user_id: int) -> None:
    """Joins a user's game. This is only possible if you'd normally be able to do so from the app.

    Note:
        The time it takes for the game to launch is entirely variable.

        It is usually recomended to use :func:`pyrobloxbot.image_is_visible` to detect when the game has finished launching.

    Args:
        user_id (int): The id of the user to join.

            This can be found in the user's profile link, which has the format ``https://www.roblox.com/users/<User Id>/profile``.
            The user id will be a random looking number.
    """

    uri = build_roblox_uri(userId=user_id, type="FollowUser")
    command = f'start "" "{uri}"'
    os.system(command=command)


@apply_cooldown()
@resets_state
def join_private_server(game_id: int, private_server_link_code: int) -> None:
    """Joins a private server given it's private link code.

    Note:
        The time it takes for the game to launch is entirely variable.

        It is usually recomended to use :func:`pyrobloxbot.image_is_visible` to detect when the game has finished launching.

    Args:
        game_id (int): The id of the private server's game.
        private_server_link_code (int): The private server's link code.
    """
    uri = build_roblox_uri(
        placeId=game_id, linkCode=private_server_link_code, type="InGame"
    )
    command = f'start "" "{uri}"'
    os.system(command=command)


@apply_cooldown()
@resets_state
def join_server(game_id: int, job_id: str) -> None:
    """Joins a particular server given it's job id.

    Note:
        The time it takes for the game to launch is entirely variable.

        It is usually recomended to use :func:`pyrobloxbot.image_is_visible` to detect when the game has finished launching.

    Args:
        game_id (int): The server's game id.
        job_id (str): The server's job id.
    """
    uri = build_roblox_uri(placeId=game_id, gameInstanceId=job_id, type="InGame")
    command = f'start "" "{uri}"'
    os.system(command=command)


__all__ = ["leave_game", "join_game", "join_user", "join_private_server", "join_server"]
