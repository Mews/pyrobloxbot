# Anti-AFK bot

```{note}
The code for this example is available at https://github.com/Mews/pyrobloxbot-examples/blob/main/anti-afk/main.py
```

We've learned how to use the features pyrobloxbot has to offer.

Now we need to learn how to actually put them together into a working script.

The first thing is we need to define the goal for our bot, and how it will accomplish it.

Our objective for this bot is just to move randomly every 5 minutes or so, to avoid getting kicked for inactivity.

After that, we can start coding.

I usually import pyrobloxbot like this:
```python
import pyrobloxbot as bot
```

When making a bot, separation of concerns is pretty important. It might seem overkill for a simple bot like this, but when you're making a huge bot with multiple steps, you definitely don't want all your code to just be unlabeled inside a `while True` loop.

So, we'll first define a function that will actually do the action we want to do.

```python
import random

def move_randomly(n_times):
    directions = ["f", "b", "l", "r"]
    for _ in range(n_times):
        d = random.choice(directions)
        bot.walk(d, duration=1)
```

Now, we just need to run this function every 5 minutes.

```python
while True:
    bot.move_randomly(5)
    bot.wait(5*60)
```

In this case, we'll use the failsafe to stop the bot.

At this point, we already have a working anti-afk bot! But we can still improve it's functionality.

For example, say we want the bot to be running while we're doing something else on our computer. We want the bot to do what it needs to do every 5 minutes, and then let us keep doing what we were doing.

For this, we'll use the {py:class}`pyrobloxbot.restore_focus` context manager.

```python
while True:
    with bot.restore_focus():
        move_randomly(5)
    bot.wait(5*60)
```

And we're done!

You can see below the bot moving randomly 5 times, then restoring the focus back to the terminal automatically, and then we terminate the program with the failsafe.

```{video} ../../_static/antiafkbot/antiafkbot.mp4
:autoplay:
:loop:
:muted:
:width: 100%
```
