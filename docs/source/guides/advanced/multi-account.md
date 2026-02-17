# Multi Account bots

Making bots that involve two or more accounts opens the door to a world of new and powerful bot possibilities.

The challenge in making these comes from the fact that pyrobloxbot checks for the Roblox window by title. If you have two windows called `"Roblox"`, then which one gets selected by pyrobloxbot becomes arbitrary.

There are two ways of making multi account bots.

## Using a multiple Roblox instances client

pyrobloxbot provides built-in support for multi account bots using this method.

You can use a tool like [Avaluate/MultipleRobloxInstances](https://github.com/Avaluate/MultipleRobloxInstances) or [ic3w0lf22/Roblox-Account-Manager](https://github.com/ic3w0lf22/Roblox-Account-Manager) to have multiple Roblox accounts open at once.

Then, we'll need to get the *handle* of every Roblox window we'll use. A handle is just an integer that identifies an open window. To get the handles, we use {py:func}`pyrobloxbot.wait_for_focus`.

We can have a script like so:
```python
import pyrobloxbot as bot

print("Select the main window")
main_window = bot.wait_for_focus()

print("Select the alt window")
alt_window = bot.wait_for_focus()
```

Where the program will print `"Select the main window"` and wait for you to select any Roblox window. It will then store the handle of the Roblox window you selected in `main_window`. Same thing for the `alt_window`. You can repeat this for as many windows as you have.

```{note}
You only need to get the handles for the windows you'll need to control.
```

Then, you use the {py:attr}`pyrobloxbot.options.target_roblox_window<pyrobloxbot.bot.options._BotOptions.target_roblox_window>` option to change which window pyrobloxbot uses.

For example, you could then do:
```python
bot.options.target_roblox_window = main_window

bot.jump()

bot.options.target_roblox_window = alt_window

bot.jump()
```

Which will make the character in the main window jump, then the character in the alt window.

```{video} ../../_static/multi_account/example.mp4
:autoplay:
:loop:
:muted:
:width: 100%

The above example being ran.
```

**✅ Pros**

- Can control all the open Roblox accounts.
- Higher limit for how many instances you can have open.

**❌ Cons**

- Requires manually registering all the Roblox windows every time the bot is ran.

## Using an android emulator

You can use an android emulator, like BlueStacks, to have multiple Roblox accounts open at once.

**✅ Pros**

- Easier to setup.
- Requires no changes when using pyrobloxbot.

**❌ Cons**

- Only the account actually open on Roblox can be botted. The ones open on the emulator can be setup manually initially, but then can't be interacted with using pyrobloxbot.
- Lower limit for how many accounts you can open, emulators use a lot of ram.
