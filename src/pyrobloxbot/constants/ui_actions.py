import typing

#: Strings that represent navigating up in ui elements
UI_NAVIGATE_UP_ACTIONS = typing.Literal["up", "u"]

#: Strings that represent navigating left in ui elements
UI_NAVIGATE_LEFT_ACTIONS = typing.Literal["left", "l"]

#: Strings that represent navigating right in ui elements
UI_NAVIGATE_RIGHT_ACTIONS = typing.Literal["right", "r"]

#: Strings that represent navigating down in ui elements
UI_NAVIGATE_DOWN_ACTIONS = typing.Literal["down", "d"]

#: Strings that represent clicking ui elements
UI_CLICK_ACTIONS = typing.Literal["click", "c"]


#: Valid strings to pass to ui_navigate
UI_ACTIONS: typing.TypeAlias = (
    UI_NAVIGATE_UP_ACTIONS
    | UI_NAVIGATE_LEFT_ACTIONS
    | UI_NAVIGATE_RIGHT_ACTIONS
    | UI_NAVIGATE_DOWN_ACTIONS
    | UI_CLICK_ACTIONS
)

__all__ = [
    "UI_NAVIGATE_UP_ACTIONS",
    "UI_NAVIGATE_LEFT_ACTIONS",
    "UI_NAVIGATE_RIGHT_ACTIONS",
    "UI_NAVIGATE_DOWN_ACTIONS",
    "UI_CLICK_ACTIONS",
    "UI_ACTIONS",
]
