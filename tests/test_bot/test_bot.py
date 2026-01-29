from pyrobloxbot.bot import bot
from pyrobloxbot.bot.keybinds import _BotKeybinds
from pyrobloxbot.bot.state import _BotState


def test_fields():
    assert isinstance(bot.state, _BotState)
    assert isinstance(bot.keybinds, _BotKeybinds)
