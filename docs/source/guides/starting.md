# Starting guide

```{admonition} Note
The goal of this guide is to get you started using the library and teach some core ideas of bot building.

For more advanced and specific examples, see the usage guides and examples.
```
pyrobloxbot is, at its core, just a library to mimic keyboard inputs for Roblox, to control the game automatically. This simple interaction method, along with a few extra features, allows you to make a huge variety of complex bots.


## Making your first bot

To get started, you need to [install the package](./installation.md).

Then, making a bot is as simple as making a normal python script. For example, to make a bot that, when ran, jumps and says `"Hello world!"` in chat, you can do:
```python
import pyrobloxbot as bot

bot.jump()
bot.chat("Hello world!")
```

You can also use any other python flow control structures, like:

```python
for i in range(5):
    bot.jump()
    bot.wait(0.5)
# You can also just do bot.jump(5, interval=0.5)

while True:
    bot.chat("annoying")

def awesome_movement_sequence():
    bot.walk_forward(5)
    bot.jump()
    bot.walk_left(2)

awesome_movement_sequence()
```

```{admonition} Tip
Use the [api reference](../api_references/api_references.md) to see all the methods `pyrobloxbot` provides.
```

## Identifying what can be botted

Making a bot with pyrobloxbot is easy, but it is also important to manage your expectations, and identify which parts of a game can be botted, and which ones cannot.

First of all, pyrobloxbot will never be like cheats. This is because anything you could do with pyrobloxbot, you would also be able to do manually (and probably faster).

It also cannot (or at least is very difficult to) automate very complex tasks. If the thing you're looking to bot requires reacting to stuff that isn't consistent, chances are
it is really hard or even impossible to automate. The most common example of this is interacting with other players. Making a bot that does PvP, for example, is essentially impossible.

pyrobloxbot excels at automating repetitive tasks or tasks that don't require much reaction to the environment. It's biggest strength is in the time you can then have the bot run. Once you have made your bot, and have made it robust enough, you can just run it for hours upon hours without intervention, potentially giving you a huge advantage over other players.

This might sound discouraging, but this still lets you automate a ton of different stuff. You can find some bot examples in the usage and advances guides to inspire you.

## Bot building basics

Roblox games are incredibly heterogeneous, but there are some reoccurring patterns and guidelines to follow when making bots.

First, you should use {py:func}`pyrobloxbot.wait` to add delays in your bot instead of `time.sleep`, to ensure that the failsafe works consistently.

You also need to be aware of every tool your bot has at its disposal, and then do your best to stretch the limits set by those tools. Learn everything your bot can do in the api references and the usage guides.

Making a botting strategy often goes way beyond actually coding. A lot of the power you can give to your bot comes from taking advantage of (often small or seemingly irrelevant) in game features. Mold the game itself to make your bot's life as easy as possible.

This can be something as simple as using a private server instead of a public one, or figuring out a specific item loadout or base layout that makes botting easier.

**Creativity is the most important skill in bot building.**

You also need to be know what your main focus should be. For example, if your bot will be running for long periods of time unattended, then reliability and robustness shouldn't be neglected.
