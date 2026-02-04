
# pyrobloxbot

[![Documentation badge](https://readthedocs.org/projects/pyrobloxbot/badge/?version=latest&style=flat-default)](https://pyrobloxbot.readthedocs.io/en/latest/pyrobloxbot.html)
[![PyPI Version](https://img.shields.io/pypi/v/pyrobloxbot?label=pypi%20package)](https://pypi.python.org/pypi/pyrobloxbot)
[![PyPI Downloads](https://img.shields.io/pypi/dm/pyrobloxbot)](https://pypi.python.org/pypi/pyrobloxbot)

A Python library to control the Roblox character and interact with game UI strictly through keyboard inputs

It aims to streamline the process of creating a Roblox bot, by providing useful features such as:
- Methods for most actions your character can make, including movement, chatting, resetting, etc
- Methods for navigating a game's UI through the keyboard exclusively, making it robust
- Methods for joining games, joining users and joining private servers
- Highly customizable, can make all kinds of bots for different use cases

For more information, read the [documentation](https://pyrobloxbot.readthedocs.io/en/latest/index.html)!

If you have any issues while using the library, please [ask a question!](CONTRIBUTING.md#i-have-a-question)

All feature suggestions are welcome! Find out [how to request a feature](CONTRIBUTING.md#suggesting-enhancements).


## Installation

Install pyrobloxbot using ```pip install pyrobloxbot```

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
