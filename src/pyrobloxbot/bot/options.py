from dataclasses import dataclass
import typing


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
    If it's not, it will simply not execute the function.

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

    target_roblox_window: typing.Optional[int] = None
    """This option is used to set the handle of the window pyrobloxbot considers as the Roblox window.

    A window handle is a unique integer that identifies a window, and you can get it using :py:func:`pyrobloxbot.wait_for_focus`

    If the target handle is set to ``None``, pyrobloxbot will instead use any window with the exact title ``"Roblox"`` as the Roblox window.

    Note:
        Window handles are volatile. If you close an app and reopen it, it's handle will likely have changed.

    Defaults to ``None``.
    """

    auto_ui_navigation_mode: bool = False
    """This option is used so that actions that need the ui navigation mode to be enabled turn it on automatically, then reset it back to whatever state it was before.

    Warning:
        This option relies on pyrobloxbot's internal tracking of whether the ui navigation mode is enabled in game.

        This can sometimes get desynced from what's actually real in game,
        because clicking certain ui elements can turn off the ui navigation mode, and there's no way to track that automatically.

        Be careful of desyncs when using this option.

    Defaults to ``False``.
    """

    def _reset(self):
        self.__init__()


__all__ = ["_BotOptions"]
