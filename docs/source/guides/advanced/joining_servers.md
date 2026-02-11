# Joining specific servers

As we've seen in the [Joining games guide](../usage/joining_games.md), pyrobloxbot has methods for:
- Joining a game on random server.
- Joining a specific private server.
- Joining a specific server.
- Joining a specific user's server.

Joining a random server or a user's server is easy. You just need to get the game id or the user id respectively, which is easy to do just by looking at a url:

- A game url will look like `https://www.roblox.com/games/155615604/Prison-Life`, and `155615604` is the game id. You can then just call {py:func}`pyrobloxbot.join_game` with that id as the argument.
- A user url will look like `https://www.roblox.com/users/694465738/profile`, and `694465738` is the user id. You can then just call {py:func}`pyrobloxbot.join_user` with that id as the argument.

However, getting the information needed to join a private server, or even a specific server, is a bit more complicated.

## Joining a private server

Joining a private server is done through {py:func}`pyrobloxbot.join_private_server`, and requires two pieces of information:
- The game id (we've seen how to get that already)
- The private server's link code.

Obtaining the latter is a bit let obvious, but still not difficult.

You're going to need to get your private server's invite link, which will look something like `https://www.roblox.com/share?code=864059867507234896ed98bd1b78a8dc&type=Server`.

You'll then paste that url in your browser, and wait a few seconds until you're redirected to a new url that looks like `https://www.roblox.com/games/90906407195271/Racket-Rivals?privateServerLinkCode=1020499390872690887970171`.
<br>There's your private server link code `1020499390872690887970171`!

```{note}
If the private server's invite link gets regenerated, then the private server link code will also change.
```

## Joining a specific server

This one is actually a bit more involved.

Joining a specific server is done through {py:func}`pyrobloxbot.join_server`, and also requires two pieces of information:
- The game id.
- The server's job id.

A job id will be a random looking string of numbers, letters and underscores, like:
<br>`D01F4F55_045B_4727_9A19_E694027D3F8A_69AA65738_2657`

This is what we'll now learn how to obtain, and there are a few ways to do it.

```{note}
Server job ids are volatile. Whenever a server shuts down, it's job id will cease to exist.
```

### Checking if the game makes it public

If you're lucky, the game you're trying to bot will actually show you the job id for the server you're in somewhere.

For example, if you look around you might find something like this:
```{figure} ../../_static/serverjobid.png
:height: 200px
:align: center

A server's job id shown in game (Racket Rivals)
```

Another common place to look is the developer console, which you can open with the `F9` key.

### Using the Roblox api

You usually can't find a server's full job id from the Roblox page, it will only show you an abbreviated version, like `11ee-46c6`. However, you can actually use the Roblox api to search for servers and get their job ids. (this is the same api used for the "Servers" tab in a game)

The url used for this is `https://games.roblox.com/v1/games/{game_id}/servers/Public`.

You can then use the `requests` library to query the Roblox api and get the information you need.

Here's an example script you can use:

```python
import requests

def get_server_ids(place_id):
    url = f"https://games.roblox.com/v1/games/{place_id}/servers/Public?limit=10"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return [server['id'] for server in data['data']]
    return []

servers = get_server_ids(73956553001240)
print(f"Available Job IDs: {servers}")
```

Some useful parameters to use in your call are:
- `limit` : How many servers to fetch.
- `sortOrder` : Either `Desc` or `Asc`, whether to sort the servers from fullest to emptiest or the other way around, respectively. Useful if you want to join almost empty servers.
- `excludeFullGames` : Whether or not to exclude full servers from the results.

### If you develop the game

This probably won't be the case, but if you're able to change the code of the game you want to join, you can print `game.JobId` to the console, and then check it by pressing `F9`.
