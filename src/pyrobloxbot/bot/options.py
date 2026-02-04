from dataclasses import dataclass


@dataclass
class _BotOptions:
    maximize_roblox_window: bool = False
    """This option tells pyrobloxbot to maximize the Roblox window on top of putting it in focus
    when sending keyboard inputs.

    Default to ``False``.
    """

    restore_focus_after_action: bool = False
    """This option tells pyrobloxbot to restore the focus to the window that was previously in focus after every time it puts Roblox in focus.

    Note:
        Keep in mind the previous window can be the Roblox window.

    This option, along with :class:`pyrobloxbot.restore_focus`, is generally the closest you can get to a "headless" bot using pyrobloxbot.

    Defaults to ``False``.
    """

    action_cooldown: float = 0
    """This option defines a cooldown in seconds that is applied after every action is executed.

    Example:
        ::

            import pyrobloxbot as bot

            bot.options.action_cooldown = 1.5

            bot.jump()
            # waits 1.5 seconds

            bot.chat("Hello world!")
            # waits 1.5 seconds

            bot.leave_game()
            # waits 1.5 seconds

    Defaults to ``0``.
    """

    force_focus: bool = True
    """This option tells pyrobloxbot to put the Roblox window in focus before sending keyboard inputs.

    If set to ``False``, pyrobloxbot will still check if the Roblox window is in focus.
    If it's not, it will simply not send any keyboard inputs.

    Important:
        Be aware that if pyrobloxbot skips executing a function because Roblox isn't in focus, the function's return value will be ``None``.

        For example::

            import pyrobloxbot as bot

            bot.options.force_focus = False

            # Imagine the Roblox window isn't in focus here

            bot.image_is_visible("image.png") # returns None, instead of a boolean

        This might lead to a ``TypeError`` down the line.

    Defaults to ``True``.
    """

    key_press_cooldown: float = 0
    """This option defines a cooldown in seconds that is applied after every keyboard input.

    This differs from :data:`action_cooldown`, because it applies the cooldown to each keyboard input instead of every action.

    Example:
        ::

            import pyrobloxbot as bot

            bot.options.key_press_cooldown = 1.5

            bot.reset_player()
            # Waits 1.5 seconds after pressing esc, r and enter
            # In contrast, action_cooldown would only wait 1.5 seconds after reset_player is done

    You might find this option useful if for any reason quick keyboard inputs are getting skipped for you.

    Defaults to ``0``.
    """

    def _reset(self):
        self.__init__()


__all__ = ["_BotOptions"]
