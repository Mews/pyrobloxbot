from ..constants.walk_directions import (
    WALK_DIRECTIONS,
    WALK_BACK_DIRECTIONS,
    WALK_FORWARD_DIRECTIONS,
    WALK_LEFT_DIRECTIONS,
    WALK_RIGHT_DIRECTIONS,
)
from .input import key_down, key_up, press_key, hold_key
from .decorators import require_focus, apply_cooldown
from ..utils import wait
from ..bot.bot import keybinds
from typing import get_args


@apply_cooldown()
@require_focus
def walk(*directions: WALK_DIRECTIONS, duration: float) -> None:
    """Makes the character walk in the given directions for a certain time.

    Args:
        *directions (WALK_DIRECTIONS): The directions to walk in.
            If two perpendicular directions are given, the bot won't move in either.

        duration (float): How long to walk for.

    Raises:
        ValueError: Raised when the directions aren't one of :data:`pyrobloxbot.constants.WALK_DIRECTIONS`
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
            raise ValueError("Direction must be one of " + str(WALK_DIRECTIONS))

    for key in keys:
        key_down(key)

    wait(duration)

    for key in keys:
        key_up(key)


@apply_cooldown()
@require_focus
def walk_forward(duration: float) -> None:
    """Walks forward for a given time.

    Args:
        duration (float): How long to walk for.
    """
    walk("f", duration=duration)


@apply_cooldown()
@require_focus
def walk_left(duration: float) -> None:
    """Walks left for a given time.

    Args:
        duration (float): How long to walk for.
    """
    walk("l", duration=duration)


@apply_cooldown()
@require_focus
def walk_right(duration: float) -> None:
    """Walks right for a given time.

    Args:
        duration (float): How long to walk for.
    """
    walk("r", duration=duration)


@apply_cooldown()
@require_focus
def walk_back(duration: float) -> None:
    """Walks backwards for a given time.

    Args:
        duration (float): How long to walk for.
    """
    walk("b", duration=duration)


@apply_cooldown()
@require_focus
def jump(number_of_jumps: int = 1, interval: float = 0) -> None:
    """Jumps a given number of times.

    Args:
        number_of_jumps (int, optional): How many times to jump. Defaults to ``1``.
        interval (float, optional): How long between each jump. Defaults to ``0``.
    """
    for i in range(number_of_jumps):
        press_key(keybinds.jump)

        if i != number_of_jumps - 1:
            wait(interval)


@apply_cooldown()
@require_focus
def jump_continuous(duration: float) -> None:
    """Holds jump for a given time.

    Args:
        duration (float): How long to hold jump for.
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
