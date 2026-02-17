import win32gui


def wait_for_focus() -> int:
    """Waits until the Roblox window is in focus, and returns it's window handle.

    Returns:
        int: The window handle for the Roblox window that made the function exit. A window handle is a unique integer and is used by Windows to identify windows.
    """

    hwnd = win32gui.GetForegroundWindow()

    while win32gui.GetWindowText(hwnd) != "Roblox":
        hwnd = win32gui.GetForegroundWindow()

    return hwnd


__all__ = ["wait_for_focus"]
