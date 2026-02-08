# Using Options

The bot's options can be changed like so
```python
import pyrobloxbot as bot

bot.options.action_cooldown = 1.5
bot.options.force_focus = False

...
```

`pyrobloxbot.options` is itself an instance of {py:class}`~pyrobloxbot.bot.options._BotOptions` that gets used by the rest of package and can be accessed by the user.

Any changes to the bot's options should be made through `pyrobloxbot.options`.

See the [options api reference](../api_references/pyrobloxbot.options.md) for all available options.
