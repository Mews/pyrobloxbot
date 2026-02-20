# Image recognition

Image recognition enables your bot to react to certain events, by checking if a given image is visible on screen.

It is done using two main methods, {py:func}`pyrobloxbot.image_is_visible` and {py:func}`pyrobloxbot.wait_for_image`

For example, if whenever a boss spawns, a notification appears on screen, which looks the same every time, then you might do something like this:
```python
import pyrobloxbot as bot

def kill_boss():
    bot.reset_player() # Put the player in a predictable position
    ...

bot.wait_for_image("boss_notification.png")

kill_boss()
```

This code will wait until the image in `"boss_notification.png"` is visible anywhere on screen, then run the `kill_boss` function.

Image recognition is a powerful tool, and is basically the only way to make your bot react to stuff happening in game.

```{admonition} Important
:name: screenshots-dpi-aware

Be aware that the screenshots are dpi aware.

This means that a screenshot taken on one monitor might not be the same
physical size as taken if in another monitor, meaning pyrobloxbot might not find it.

Being in fullscreen has the same effect.

It is recommended to use screenshots taken on the monitor where Roblox will be running.
```

```{tip}
You might need to identify something that is partially transparent, like text, that will be different depending on what's behind it.

For this case, you can lower the `confidence` argument of {py:func}`pyrobloxbot.image_is_visible`. The default is `0.9`, and the lower it is, the less anything on screen has to match the actual image for it to return `True`.

Keep in mind low enough confidence values will begin giving false positives.
```
