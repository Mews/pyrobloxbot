from ..constants.walk_directions import (
    WALK_DIRECTIONS,
    WALK_BACK_DIRECTIONS,
    WALK_FORWARD_DIRECTIONS,
    WALK_LEFT_DIRECTIONS,
    WALK_RIGHT_DIRECTIONS,
)
from .input import require_focus, key_down, key_up, press_key, hold_key
from ..exceptions import InvalidWalkDirectionException
from ..utils import wait
from ..bot.bot import keybinds
from typing import get_args


@require_focus
def walk(*directions: WALK_DIRECTIONS, duration: float) -> None:
    """Walks in one or more directions for a given time

    If more than one direction is given it will walk diagonally

    :param directions: The directions to walk in
    :type directions: WALK_DIRECTIONS
    :param duration: How long to walk for, in seconds
    :type duration: float
    :raises InvalidWalkDirectionException: Raised when given directions aren't one of literals.WALK_DIRECTIONS
    """

    keys = set()

    for direction in directions:
        d = direction.lower().strip()

        if d in get_args(WALK_FORWARD_DIRECTIONS):
            keys.add(keybinds.walk_forward)
        elif d in get_args(WALK_LEFT_DIRECTIONS):
            keys.add(keybinds.walk_left)
        elif d in get_args(WALK_RIGHT_DIRECTIONS):
            keys.add(keybinds.walk_right)
        elif d in get_args(WALK_BACK_DIRECTIONS):
            keys.add(keybinds.walk_back)
        else:
            raise InvalidWalkDirectionException(
                "Direction must be one of " + str(WALK_DIRECTIONS)
            )

    for key in keys:
        key_down(key)

    wait(duration)

    for key in keys:
        key_up(key)


@require_focus
def walk_forward(duration: float) -> None:
    """Walks forward for a given time

    :param duration: How long to walk for, in seconds
    :type duration: float
    """
    walk("f", duration=duration)


@require_focus
def walk_left(duration: float) -> None:
    """Walks left for a given time

    :param duration: How long to walk for, in seconds
    :type duration: float
    """
    walk("l", duration=duration)


@require_focus
def walk_right(duration: float) -> None:
    """Walks right for a given time

    :param duration: How long to walk for, in seconds
    :type duration: float
    """
    walk("r", duration=duration)


@require_focus
def walk_back(duration: float) -> None:
    """Walks back for a given time

    :param duration: How long to walk for, in seconds
    :type duration: float
    """
    walk("b", duration=duration)


@require_focus
def jump(number_of_jumps: int = 1, interval: float = 0) -> None:
    """Jumps for a given number of times

    :param number_of_jumps: How many times to jump, defaults to 1
    :type number_of_jumps: int
    :param interval: How much time between jumps, in seconds, defaults to 0
    :type interval: float
    """
    for _ in range(number_of_jumps):
        press_key(keybinds.jump)
        wait(interval)


@require_focus
def jump_continuous(duration: float) -> None:
    """Holds jump for a given time

    :param duration: How long to hold jump for, in seconds
    :type duration: float
    """
    hold_key(keybinds.jump, duration=duration)


__all__ = [
    "walk",
    "walk_forward",
    "walk_left",
    "walk_right",
    "walk_back",
    "jump",
    "jump_continuous",
]
