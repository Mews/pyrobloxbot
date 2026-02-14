# Macros

```{note}
This bot is made for the [*surf*](https://www.roblox.com/games/5315066937/surf) game, as of 11/02/2026.

The code for this bot is available in https://github.com/Mews/pyrobloxbot-examples/blob/main/surf-macros/main.py
```

You can use pyrobloxbot in conjunction with the keyboard package to make macros to use in game!

```{note}
You'll need to install the [keyboard](https://pypi.org/project/keyboard/) package.
```

For this example, we'll make macros for the [*surf*](https://www.roblox.com/games/5315066937/surf) game. In *surf*, you often need to type commands in chat to do stuff.
We'll make macros for common commands: `/spec`, `/serverlist` and `/style`.

Doing this is very simple. We just need to use `keyboard.add_hotkey` to register a global hotkey. Then we can use the hotkey to call any function.

In this example we'll use it to call a function that does a single action, using `lambda`, but you could just as easily define a function for a multi step action and bind that to the hotkey.

The code for the macros will look like:
```python
import pyrobloxbot as bot
import keyboard

bot.options.force_focus = False

keyboard.add_hotkey("u", lambda:bot.chat("/spec"))
keyboard.add_hotkey("i", lambda:bot.chat("/serverlist"))
keyboard.add_hotkey("o", lambda:bot.chat("/style"))

while True:
    bot.wait(0.1)
```

Then, when in game, pressing `U`, `I` and `O` will send `/spec`, `/serverlist` and `/style` in chat.

```{tip}
Use the {py:attr}`pyrobloxbot.options.force_focus<pyrobloxbot.bot.options._BotOptions.force_focus>` option to avoid triggering your macro outside Roblox.
```

````{tip}
When making an infinite loop to keep your macro running, use:
```python
while True:
    bot.wait(0.1)
```
Not
```python
while True:
    pass
```
Using `pass` will lead to pretty bad input lag on Roblox.
````
