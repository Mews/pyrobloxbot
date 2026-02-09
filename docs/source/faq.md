# FAQ

(faq-windowless)=
## "Windowless" / "Headless" bots

pyrobloxbot does not enable you to make truly headless Roblox bots in the traditional sense.

This is a consequence of the fundamental way pyrobloxbot sends inputs. Because the bot interacts through Roblox by "faking" keyboard inputs, the Roblox window must at some
point be in focus for the inputs to register.

Making truly headless Roblox bots is an incredibly complex task.

The closest you might be able to get is by [using the restore_focus_after_action option](options-guide-windowless) or the {py:class}`~pyrobloxbot.restore_focus` decorator. You might also pair these tools with minimizing the Roblox window, to make it never actually visible on screen, but it will still be active, and any keys you hit on your keyboard will be sent to Roblox.
