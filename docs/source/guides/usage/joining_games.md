# Joining games

pyrobloxbot also has methods to join Roblox games, just like you would on the regular Roblox app.

This is useful to make certain kinds of bots where you need to server hop (see the usage examples), but also can just be used to make your bot more robust.

Depending on the game and whether or not you have a private server, you might not be able to account for 100% of things that could happen to you while you're afk.

So, if you plan on having your bot run for really long periods of time unattended, a good practice would be to rejoin whatever game you are every once in a while, to undo anything unpredictable that might have happened to your character.

Mostly though, these methods are used for server hopping.

```{tip}
You can join a Roblox game (even if its the same game) while already being inside a game.
```

```python
import pyrobloxbot as bot

game_id = 12345 # Example game id

def collect_lobby_chest():
    # Example routine to do on each server hop
    bot.ui_click()
    bot.walk("fw", duration=3)
    bot.hold_key("e", duration=1)

while True:
    bot.join_game(game_id) # Rejoin another random server

    while not bot.image_is_visible("play_button.png"):
        bot.wait(1) # Wait until the game launches

    collect_lobby_chest()
```
In the above example, the bot joins a random server on the game with id `12345`, then waits for it to finish loading (imagine in the example `"play_button.png"` is a screenshot of something that only appears when the game loads, and always looks the same, like a play button) and then do some routine, before server hopping to do it again.

More fleshed out versions of similar bots are available in the [usage examples].

pyrobloxbot allows you to:
- Join a game on random server.
- Join a specific private server.
- Join a specific server.
- Join a specific user's server.

Joining a random server or a user's server is easy. You just need to get the game id or the user id respectively, which is easy to do just by looking at a url:

- A game url will look like `https://www.roblox.com/games/155615604/Prison-Life`, and `155615604` is the game id. You can then just call {py:func}`pyrobloxbot.join_game` with that id as the argument.
- A user url will look like `https://www.roblox.com/users/694465738/profile`, and `694465738` is the user id. You can then just call {py:func}`pyrobloxbot.join_user` with that id as the argument.

Joining a private server and a specific server in particular are a bit more difficult. See [the advanced guide](../advanced/joining_servers.md) for more info on how to do so.

Check the {py:func}`api reference <pyrobloxbot.join_game>` to see how to use all the game joining methods.

```{note}
Keep in mind you're only able to do any of these things if you'd normally be able to do them from the Roblox app.
```
