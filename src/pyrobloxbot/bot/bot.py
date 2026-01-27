from .keybinds import BotKeybinds
from .state import BotState

state = BotState()
keybinds = BotKeybinds()

__all__ = ["state", "keybinds"]
