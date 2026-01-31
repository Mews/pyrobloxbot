from dataclasses import dataclass


@dataclass
class _BotState:
    _UI_NAV_ENABLED: bool = False

    _SHIFT_LOCK_ENABLED: bool = False

    _INVENTORY_OPEN: bool = False

    _COOLDOWN_SET: bool = False

    def is_ui_nav_enabled(self) -> bool:
        return self._UI_NAV_ENABLED

    def is_shift_lock_enabled(self) -> bool:
        return self._SHIFT_LOCK_ENABLED

    def is_inventory_open(self) -> bool:
        return self._INVENTORY_OPEN

    def _reset(self):
        self.__init__()


__all__ = ["_BotState"]
