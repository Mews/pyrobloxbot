from ..exceptions import InvalidSlotNumberException
from .input import require_focus, press_key, hold_key
from ..utils import wait
from ..bot.bot import keybinds
import pyperclip


@require_focus
def reset_player(interval: float = 0.5):
    """Resets player character

    :param interval: How long between each keyboard input, in seconds, defaults to 0.5
    :type interval: float
    """
    press_key("esc")
    wait(interval)
    press_key("r")
    wait(interval)
    press_key("enter")


@require_focus
def chat(message: str):
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


@require_focus
def equip_slot(slot: int):
    """Equip a given item slot

    :param slot: The item slot to equip
    :type slot: int
    :raises InvalidSlotNumberException: Raised when slot isn't between 0 and 9
    """
    if slot < 0 or slot > 9:
        raise InvalidSlotNumberException("Slots should be between 0 and 9")

    press_key(str(slot))


@require_focus
def toggle_shift_lock():
    """Toggles shift lock (Shift lock switch must be enabled in roblox settings)"""
    press_key(keybinds.toggle_shift_lock)


__all__ = [
    "reset_player",
    "chat",
    "equip_slot",
    "toggle_shift_lock",
]
