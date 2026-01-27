from dataclasses import dataclass


@dataclass
class BotState:
    ui_nav_enabled: bool = False

    shift_lock_enabled: bool = False


__all__ = ["BotState"]
