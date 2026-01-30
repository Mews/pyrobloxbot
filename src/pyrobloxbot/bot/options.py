from dataclasses import dataclass


@dataclass
class _BotOptions:
    maximize_roblox_window: bool = False

    restore_focus_after_action: bool = False

    action_cooldown: float = 0

    def _reset(self):
        self.__init__()


__all__ = ["_BotOptions"]
