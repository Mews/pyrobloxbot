import win32gui


def wait_for_focus() -> int:
    """Waits until any Roblox window is in focus, and returns it's window handle.

    Note:
        Window handles are volatile. If you close an app and reopen it, it's handle will likely have changed.

    Returns:
        int: The window handle for the Roblox window that made the function exit. A window handle is a unique integer that is used to identify a specific window.
    """

    hwnd = win32gui.GetForegroundWindow()

    while win32gui.GetWindowText(hwnd) != "Roblox":
        hwnd = win32gui.GetForegroundWindow()

    return hwnd


__all__ = ["wait_for_focus"]
