# Changing keybinds

```{admonition} Note
See the [keybinds api reference](../api_references/pyrobloxbot.keybinds.md) for all available keybinds.
```

The `pyrobloxbot.keybinds` field serves two purposes:

1. Changing the keys used for each action
2. Changing the failsafe hotkey

## Changing keybinds

Often you'll find that some games change the default keys used for some actions.
Some common examples include opening the chat with `-` instead of `/`, and using the control key to toggle shift lock.

To make bots for these games, you might then need to change the key that the bot uses for these actions.

pyrobloxbot provides a way to do this through the `keybinds` field.

```python
import pyrobloxbot as bot

bot.keybinds.open_chat = '-'
bot.keybinds.toggle_shift_lock = 'ctrl'

...
```

In the above example, we change the bot's open chat and toggle shift lock keybinds.
This means that if we later do:
```python
bot.chat("Hello world!") # This will use '-' to open the chat instead of '/'
bot.enable_shift_lock() # This will press control instead of shift
```

A list of all the available keybinds can be found in the [api reference](../api_references/pyrobloxbot.keybinds.md).

## Changing the failsafe hotkey

pyrobloxbot comes with a global failsafe that can be triggered through a keyboard hotkey (`control+m` by default) to avoid your bot going rogue.
However, your bot might for whatever reason need to input the default hotkey, or you might be using another app while your bot is running that has you
pressing the default hotkey.

You can change the failsafe hotkey through the keybinds field.

```python
import pyrobloxbot as bot

bot.keybinds.set_failsafe_hotkey("ctrl", "shift", "y")

...
```

In the above code example, after the `set_failsafe_hotkey` method is executed, hitting `control+m` will no longer trigger the failsafe, only `control+shift+y` will.
