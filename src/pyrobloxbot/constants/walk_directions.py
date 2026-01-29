import typing

WALK_FORWARD_DIRECTIONS = typing.Literal["f", "fw", "forward", "forwards"]
WALK_BACK_DIRECTIONS = typing.Literal["b", "bw", "back", "backward", "backwards"]
WALK_LEFT_DIRECTIONS = typing.Literal["l", "left"]
WALK_RIGHT_DIRECTIONS = typing.Literal["r", "right"]

"""Valid strings to pass to walk"""
WALK_DIRECTIONS = (
    WALK_FORWARD_DIRECTIONS
    | WALK_BACK_DIRECTIONS
    | WALK_LEFT_DIRECTIONS
    | WALK_RIGHT_DIRECTIONS
)

__all__ = [
    "WALK_FORWARD_DIRECTIONS",
    "WALK_BACK_DIRECTIONS",
    "WALK_LEFT_DIRECTIONS",
    "WALK_RIGHT_DIRECTIONS",
    "WALK_DIRECTIONS",
]
