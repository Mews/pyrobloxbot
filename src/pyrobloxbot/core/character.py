from .input import press_key, hold_key
from .decorators import require_focus, apply_cooldown
from ..utils import wait
from ..bot.bot import keybinds, state
import pyperclip


@apply_cooldown()
@require_focus
def reset_player(interval: float = 0) -> None:
    """Resets the player character.

    Args:
        interval (float, optional): How long to wait in between each key press.
            Defaults to ``0``.

            Usually it should be fine, but change it to a higher value if you find it unreliable.
    """
    press_key("esc")
    wait(interval)
    press_key("r")
    wait(interval)
    press_key("enter")


@apply_cooldown()
@require_focus
def chat(message: str) -> None:
    """Sends a message in chat.

    Args:
        message (str): The message to send.
    """
    # Open chat
    press_key(keybinds.open_chat)

    # Use clipboard to paste message quickly
    previousClipboard = pyperclip.paste()

    pyperclip.copy(message)

    hold_key("ctrl", "v", duration=0.5)

    press_key("enter")

    # Restore previous clipboard content
    pyperclip.copy(previousClipboard)


@apply_cooldown()
@require_focus
def equip_slot(slot: int) -> None:
    """Equips a hotbar slot.

    Args:
        slot (int): The number of the slot to equip.
            Must be between ``0`` and ``9``.

    Raises:
        ValueError: Raised when the slot number isn't between ``0`` and ``9``.
    """
    if slot < 0 or slot > 9:
        raise ValueError("Slots should be between 0 and 9")

    press_key(str(slot))


@apply_cooldown()
@require_focus
def toggle_inventory() -> None:
    """Toggles the inventory."""
    press_key(keybinds.toggle_inventory)
    state._INVENTORY_OPEN = not state._INVENTORY_OPEN


@apply_cooldown()
@require_focus
def open_inventory() -> None:
    """Opens the inventory.
    If the inventory is already open, does nothing.
    """
    if not state.is_inventory_open():
        toggle_inventory()


@apply_cooldown()
@require_focus
def close_inventory() -> None:
    """Closes the inventory.
    If the inventory is already closed, does nothing.
    """
    if state.is_inventory_open():
        toggle_inventory()


@apply_cooldown()
@require_focus
def toggle_shift_lock() -> None:
    """Toggles shift lock.

    Note:
        Shift lock switch must be enabled in Roblox settings"""
    press_key(keybinds.toggle_shift_lock)
    state._SHIFT_LOCK_ENABLED = not state.is_shift_lock_enabled()


@apply_cooldown()
@require_focus
def enable_shift_lock() -> None:
    """Enables shift lock.
    If shift lock is already enabled, does nothing.

    Note:
        Shift lock switch must be enabled in Roblox settings.
    """
    if not state.is_shift_lock_enabled():
        toggle_shift_lock()


@apply_cooldown()
@require_focus
def disable_shift_lock() -> None:
    """Disables shift lock.
    If shift lock is already disabled, does nothing.

    Note:
        Shift lock switch must be enabled in Roblox settings.
    """
    if state.is_shift_lock_enabled():
        toggle_shift_lock()


__all__ = [
    "reset_player",
    "chat",
    "equip_slot",
    "toggle_shift_lock",
    "enable_shift_lock",
    "disable_shift_lock",
    "toggle_inventory",
    "open_inventory",
    "close_inventory",
]
