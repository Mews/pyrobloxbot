# FAQ

(faq-windowless)=
## "Windowless" / "Headless" bots

pyrobloxbot does not enable you to make truly headless Roblox bots in the traditional sense.

This is a consequence of the fundamental way pyrobloxbot sends inputs. Because the bot interacts through Roblox by "faking" keyboard inputs, the Roblox window must at some
point be in focus for the inputs to register.

Making truly headless Roblox bots is an incredibly complex task.

The closest you might be able to get is by [using the restore_focus_after_action option](options-guide-windowless) or the {py:class}`~pyrobloxbot.restore_focus` decorator. You might also pair these tools with minimizing the Roblox window, to make it never actually visible on screen, but it will still be active, and any keys you hit on your keyboard will be sent to Roblox.

(faq-keyboard-only)=
## Why only use the keyboard?

Often when making an automation script, using the mouse is the most finicky part. This is because it usually involves a lot of "magic numbers", and tends to be more unreliable that using the keyboard in general.

It also can lead to worse consequences if for whatever reason there's a mistake on your bot, because pyrobloxbot can ensure that it's keyboard inputs only ever get sent to Roblox, but not mouse inputs.

As such, I made the decision to only use the keyboard when making my bots, and that later transferred over to pyrobloxbot.

This doesn't mean that you can't use the mouse in **your** bots, or even that its a bad idea. Sometimes it really is the only way to bot something, and I myself have resorted to using the mouse for some bots.
<br> It just means that pyrobloxbot doesn't support it.
