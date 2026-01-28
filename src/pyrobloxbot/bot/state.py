from dataclasses import dataclass


@dataclass
class BotState:
    _ui_nav_enabled: bool = False

    _shift_lock_enabled: bool = False

    def is_ui_nav_enabled(self):
        return self._ui_nav_enabled

    def is_shift_lock_enabled(self):
        return self._shift_lock_enabled


__all__ = ["BotState"]
