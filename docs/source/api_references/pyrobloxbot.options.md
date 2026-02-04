# pyrobloxbot.options


The bot's options can be changed like so
```python
import pyrobloxbot as bot

bot.options.action_cooldown = 1.5
bot.options.force_focus = False

...
```

`pyrobloxbot.options` is itself an instance of `_BotOptions` that gets used by the rest of package and can be accessed by the user.

```{eval-rst}
..  autoclass:: pyrobloxbot.bot.options._BotOptions
    :members:
```
