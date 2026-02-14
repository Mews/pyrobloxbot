# Multi Account bots

Making bots that involve two or more accounts opens the door to a world of new and powerful bot possibilities.

The challenge in making these comes from the fact that pyrobloxbot checks for the Roblox window by title. If you have two windows called `"Roblox"`, then which one gets selected by pyrobloxbot becomes arbitrary.

There are two ways of making multi account bots.

## Using an android emulator

You can use an android emulator, like BlueStacks, to have multiple Roblox accounts open at once.

**✅ Pros**

- Easier to setup.
- Requires no changes when using pyrobloxbot.
- More robust.

**❌ Cons**

- Only the account actually open on Roblox can be botted. The ones open on the emulator can be setup manually initially, but then can't be interacted with using pyrobloxbot.
- Lower limit for how many accounts you can open, emulators use a lot of ram.

## Using a multiple Roblox instances client

You can use a tool like [Avaluate/MultipleRobloxInstances](https://github.com/Avaluate/MultipleRobloxInstances) or [ic3w0lf22/Roblox-Account-Manager](https://github.com/ic3w0lf22/Roblox-Account-Manager) to have multiple Roblox accounts open at once.

If you then set {py:attr}`pyrobloxbot.options.force_focus<pyrobloxbot.bot.options._BotOptions.force_focus>` to `False`, you can use pyrobloxbot to alt tab around your open Roblox instances.

```{important}
It is important that you're aware that the order in which you cycle through windows in alt tab depends on when they were last accessed.

This means that if before you start your bot you open the Roblox instances in a different order, or interact with them, then the order that your bot expects might be different than the real one.

This issue is more apparent if you have more than two Roblox instances open.
```

**✅ Pros**

- Can control all the open Roblox accounts.
- Higher limit for how many instances you can have open.

**❌ Cons**

- More flaky, due to needing to alt tab around.
