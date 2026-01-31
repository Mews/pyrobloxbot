from ..exceptions import InvalidSlotNumberException
from .input import press_key, hold_key
from .decorators import require_focus, apply_cooldown
from ..utils import wait
from ..bot.bot import keybinds, state
import pyperclip


@apply_cooldown
@require_focus
def reset_player(interval: float = 0.5) -> None:
    """Resets player character

    :param interval: How long between each keyboard input, in seconds, defaults to 0.5
    :type interval: float
    """
    press_key("esc")
    wait(interval)
    press_key("r")
    wait(interval)
    press_key("enter")


@apply_cooldown
@require_focus
def chat(message: str) -> None:
    """Sends a message in chat

    :param message: The message to send
    :type message: str
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


@apply_cooldown
@require_focus
def equip_slot(slot: int) -> None:
    """Equip a given item slot

    :param slot: The item slot to equip
    :type slot: int
    :raises InvalidSlotNumberException: Raised when slot isn't between 0 and 9
    """
    if slot < 0 or slot > 9:
        raise InvalidSlotNumberException("Slots should be between 0 and 9")

    press_key(str(slot))


@apply_cooldown
@require_focus
def toggle_inventory() -> None:
    press_key(keybinds.toggle_inventory)
    state._INVENTORY_OPEN = not state._INVENTORY_OPEN


@apply_cooldown
@require_focus
def open_inventory() -> None:
    if not state.is_inventory_open():
        toggle_inventory()


@apply_cooldown
@require_focus
def close_inventory() -> None:
    if state.is_inventory_open():
        toggle_inventory()


@apply_cooldown
@require_focus
def toggle_shift_lock() -> None:
    """Toggles shift lock (Shift lock switch must be enabled in roblox settings)"""
    press_key(keybinds.toggle_shift_lock)
    state._SHIFT_LOCK_ENABLED = not state.is_shift_lock_enabled()


@apply_cooldown
@require_focus
def enable_shift_lock() -> None:
    if not state.is_shift_lock_enabled():
        toggle_shift_lock()


@apply_cooldown
@require_focus
def disable_shift_lock() -> None:
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
