from ..constants import WALK_DIRECTIONS
from .input import require_focus, key_down, key_up, press_key, hold_key
from ..exceptions import InvalidWalkDirectionException
from ..utils import wait


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
            key_down("w")
        elif d in leftDirections:
            key_down("a")
        elif d in rightDirections:
            key_down("d")
        elif d in backDirections:
            key_down("s")

    wait(duration)

    # Release keys
    for direction in directions:
        d = direction.lower().strip()

        if d in forwardDirections:
            key_up("w")
        elif d in leftDirections:
            key_up("a")
        elif d in rightDirections:
            key_up("d")
        elif d in backDirections:
            key_up("s")


@require_focus
def walk_forward(duration: float):
    """Walks forward for a given time

    :param duration: How long to walk for, in seconds
    :type duration: float
    """
    walk("f", duration=duration)


@require_focus
def walk_left(duration: float):
    """Walks left for a given time

    :param duration: How long to walk for, in seconds
    :type duration: float
    """
    walk("l", duration=duration)


@require_focus
def walk_right(duration: float):
    """Walks right for a given time

    :param duration: How long to walk for, in seconds
    :type duration: float
    """
    walk("r", duration=duration)


@require_focus
def walk_back(duration: float):
    """Walks back for a given time

    :param duration: How long to walk for, in seconds
    :type duration: float
    """
    walk("b", duration=duration)


@require_focus
def jump(number_of_jumps: int = 1, delay: float = 0):
    """Jumps for a given number of times

    :param number_of_jumps: How many times to jump, defaults to 1
    :type number_of_jumps: int
    :param delay: How much time between jumps, in seconds, defaults to 0
    :type delay: float
    """
    for _ in range(number_of_jumps):
        press_key("space")
        wait(delay)


@require_focus
def jump_continuous(duration: float):
    """Holds jump for a given time

    :param duration: How long to hold jump for, in seconds
    :type duration: float
    """
    hold_key("space", duration=duration)


__all__ = [
    "walk",
    "walk_forward",
    "walk_left",
    "walk_right",
    "walk_back",
    "jump",
    "jump_continuous",
]
