# Using Options

```{admonition} Note
See the [options api reference](../api_references/pyrobloxbot.options.md) for all available options.
```

pyrobloxbot comes pre-configured for a particular use case. This tends to be longer running bots, that you leave running uninterrupted and without intervention for a while.

However, you can leverage the various `options` provided to have your bot fit various different use cases.

## Waiting in background

You can have your bot run only when the Roblox window is in focus, and stop otherwise, using the {py:attr}`~pyrobloxbot.bot.options._BotOptions.force_focus` option.

Setting this option to `False` makes it so that actions get ignored if Roblox isn't is focus (read the {py:attr}`api reference<pyrobloxbot.bot.options._BotOptions.force_focus>` for more information).

Take this example, where the key `e` is repetedly pressed (maybe opening eggs in some game).
```python
import pyrobloxbot as bot

while True:
    bot.press_key('e')
    bot.wait(0.2)
```

This would require that the Roblox window always be in focus. If you instead did:
```python
import pyrobloxbot as bot

bot.options.force_focus = False

while True:
    bot.press_key('e')
    bot.wait(0.2)
```

Then it would still spam the `e` key, but you could open another window and it would stop until you focused Roblox again.

(options-guide-windowless)=
## "Windowless" / "Headless" bots

```{admonition} Note
pyrobloxbot doesn't enable you to make truly headless Roblox bots. Read the {ref}`FAQ<faq-windowless>` for more information.
```

You might want to keep using your computer while your bot is running.

If your bot will only be doing one or two actions every once in a while, then you can use the {py:attr}`~pyrobloxbot.bot.options._BotOptions.restore_focus_after_action` option. Setting this to `True` will make pyrobloxbot restore the focus to your window after executing each action (keep in mind the "previous window" can be the Roblox window).

For example, you might want a very simple anti afk bot.
If you did:
```python
import pyrobloxbot as bot

while True:
    bot.jump()
    bot.wait(60)
```

Then the Roblox window would be put in focus every time you jumped, and you'd need to go back to whatever window you were using before manually.

Instead, you can do:
```python
import pyrobloxbot as bot

bot.options.restore_focus_after_action = True

while True:
    bot.jump()
    bot.wait(60)
```

This will do the same, but it will put the previous window back in focus after jumping.

Do keep in mind that if, for example, you were doing something like this:

```python
import pyrobloxbot as bot

bot.options.restore_focus_after_action = True

bot.chat("hi")
bot.jump()
bot.walk_forward(10)
bot.jump()
bot.reset_player()
...
```

then the Roblox window would be put in and out of focus between each individual action.

To execute an entire code block and afterwards restore the focus to the previous window, you instead should use the {py:class}`pyrobloxbot.restore_focus` context manager.
