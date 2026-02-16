import win32gui


class restore_focus:
    """This is a context manager that allows you to execute bot actions inside it,
    and at the end restore the focus to the window that was previously active.

    Example:
        Ran from the terminal, jump and say ``"Hello world!"`` in chat before returning to the terminal

        >>> import pyrobloxbot as bot
        >>> with bot.restore_focus():
        ...     bot.jump()
        ...     bot.chat("Hello world!")

    """

    def __enter__(self):
        self.previous_window = win32gui.GetForegroundWindow()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        win32gui.SetForegroundWindow(self.previous_window)


__all__ = ["restore_focus"]
