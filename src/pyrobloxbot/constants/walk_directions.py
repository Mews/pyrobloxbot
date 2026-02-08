import typing

#: Strings that represent the forward direction in walk
WALK_FORWARD_DIRECTIONS = typing.Literal["f", "fw", "forward", "forwards"]

#: Strings that represent the back direction in walk
WALK_BACK_DIRECTIONS = typing.Literal["b", "bw", "back", "backward", "backwards"]

#: Strings that represent the left direction in walk
WALK_LEFT_DIRECTIONS = typing.Literal["l", "left"]

#: Strings that represent the right direction in walk
WALK_RIGHT_DIRECTIONS = typing.Literal["r", "right"]

#: Valid strings to pass to walk
WALK_DIRECTIONS: typing.TypeAlias = (
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
