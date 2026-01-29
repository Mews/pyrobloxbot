from pyrobloxbot.bot import bot
from pyrobloxbot.bot.keybinds import BotKeybinds
from pyrobloxbot.bot.state import BotState


def test_fields():
    assert isinstance(bot.state, BotState)
    assert isinstance(bot.keybinds, BotKeybinds)
