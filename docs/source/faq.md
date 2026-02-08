# FAQ

(faq-windowless)=
## "Windowless" / "Headless" bots

`pyrobloxbot` does not enable you to make truly headless Roblox bots in the tradicional sense.

This is a consequence of the fundamental way `pyrobloxbot` sends inputs. Because the bot interacts through Roblox by "faking" keyboard inputs, the Roblox window must at some
point be in focus for the inputs to register.

Making truly headless Roblox bots is an incredibly complex task, and working methods tend to get patched within a few weeks.

The closest you might be able to get is by [using the restore_focus_after_action option](options-guide-windowless) or the {py:class}`~pyrobloxbot.restore_focus` decorator.
