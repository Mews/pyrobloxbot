import typing

UI_NAVIGATE_UP_ACTIONS = typing.Literal["up", "u"]
UI_NAVIGATE_LEFT_ACTIONS = typing.Literal["left", "l"]
UI_NAVIGATE_RIGHT_ACTIONS = typing.Literal["right", "r"]
UI_NAVIGATE_DOWN_ACTIONS = typing.Literal["down", "d"]
UI_CLICK_ACTIONS = typing.Literal["click", "c"]


"""Valid strings to pass to ui_navigate"""
UI_ACTIONS = (
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
