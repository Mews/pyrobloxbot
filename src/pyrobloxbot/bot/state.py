from dataclasses import dataclass


@dataclass
class _BotState:
    _UI_NAV_ENABLED: bool = False

    _SHIFT_LOCK_ENABLED: bool = False

    _INVENTORY_OPEN: bool = False

    _COOLDOWN_SET: bool = False

    def is_ui_nav_enabled(self) -> bool:
        """Returns whether or not the ui navigation mode is enabled.

        Important:
            There are cases where this can become disconnected from what's actually true in game.

            For more information, see :ref:`starting-ui-navigation`.

        Returns:
            bool: Whether or not the ui navigation mode is enabled.
        """
        return self._UI_NAV_ENABLED

    def is_shift_lock_enabled(self) -> bool:
        """Returns whether or not shift lock is enabled or not.

        Returns:
            bool: Whether or not shift lock is enabled.
        """
        return self._SHIFT_LOCK_ENABLED

    def is_inventory_open(self) -> bool:
        """Returns whether or not the player's inventory is open.

        Returns:
            bool: Whether or not the players inventory is open.
        """
        return self._INVENTORY_OPEN

    def _reset(self):
        self.__init__()


__all__ = ["_BotState"]
