from .keybinds import _BotKeybinds
from .state import _BotState

state = _BotState()
keybinds = _BotKeybinds()

__all__ = ["state", "keybinds"]
