from .keybinds import _BotKeybinds
from .state import _BotState
from .options import _BotOptions

state = _BotState()
keybinds = _BotKeybinds()
options = _BotOptions()

__all__ = ["state", "keybinds", "options"]
