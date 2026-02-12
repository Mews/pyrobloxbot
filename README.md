
# pyrobloxbot

[![Documentation badge](https://readthedocs.org/projects/pyrobloxbot/badge/?version=latest&style=flat-default)](https://pyrobloxbot.readthedocs.io/en/latest/pyrobloxbot.html)
[![PyPI Version](https://img.shields.io/pypi/v/pyrobloxbot?label=pypi%20package)](https://pypi.python.org/pypi/pyrobloxbot)
[![PyPI Downloads](https://img.shields.io/pypi/dm/pyrobloxbot)](https://pypi.python.org/pypi/pyrobloxbot)

**pyrobloxbot** is an open-source package for making Roblox bots that interact with the game strictly through the keyboard.

It simplifies this process by providing features like:
- Methods for most actions your character can make, like movement, chatting, resetting, etc
- Methods to navigate through game ui elements through the keyboard only, to avoid needing the mouse which is unreliable
- Methods to join games, join users and join private servers
- Highly customizable bots, by changing different options to fit your use case
- A global failsafe to avoid your bot going rogue

## Installation guide

pyrobloxbot can be installed using pip, by doing:

```shell
pip install pyrobloxbot
```

> [!NOTE]
> For now, pyrobloxbot is Windows only. See the [issue tracker](https://github.com/Mews/pyrobloxbot/issues/93) for updates.

## Documentation

Read the documentation at https://pyrobloxbot.readthedocs.io/en/latest/index.html

There you'll find:
- API references
- Basic and advanced usage guides
- Step by step, real life examples

## Have a question?

Don't hesitate to ask!

You can check the [FAQ](https://pyrobloxbot.readthedocs.io/en/latest/faq.html), [open an issue](https://github.com/Mews/pyrobloxbot/issues/new?labels=question), or contact me on discord (mews75)!

## Got an idea?

All feature requests are welcome!

You can submit them on github by [opening an issue](https://github.com/mews/pyrobloxbot/issues/new?template=feature.yml) and using the feature template.

---

Also, feel free to share anything you make with me through my discord (mews75)!

## Usage/Examples

```python
import pyrobloxbot as bot

#Send a message in chat
bot.chat("Hello world!")

#Walk forward for 5 seconds
bot.walk_forward(5)

#Reset player character
bot.reset_player()
```

## [Changelog](CHANGELOG.md)
