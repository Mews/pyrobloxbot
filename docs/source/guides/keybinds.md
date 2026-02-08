# Changing keybinds

On some games and for some keyboard languages, you might find that the default keybinds don't work.

Imagine a game where:
- Chat is opened with `-` instead of `/`
- Shift lock is toggled with `control` instead of `shift`
- And that, due to our keyboard language, the ui navigation mode is toggled with `~` instead of `\`

We could still make our bot work, by doing:
```python
import pyrobloxbot as bot

bot.keybinds.open_chat = "-"
bot.keybinds.toggle_shift_lock = "ctrl"
bot.keybinds.toggle_ui_navigation = "~"

...
```

`pyrobloxbot.keybinds` is also used for changing the failsafe hotkey, through {py:meth}`~pyrobloxbot.bot.keybinds._BotKeybinds.set_failsafe_hotkey`.

`pyrobloxbot.keybinds` is itself an instance of {py:class}`~pyrobloxbot.bot.keybinds._BotKeybinds` that gets used by the rest of package and can be accessed by the user.

Any changes to the keybinds should be done through `pyrobloxbot.keybinds`.

See the [keybinds api reference](../api_references/pyrobloxbot.keybinds.md) for all available keybinds.
