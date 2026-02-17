import win32gui
import pydirectinput


def wait_for_focus(take_away_focus: bool = True) -> int:
    """Waits until any Roblox window is in focus, and returns it's window handle.

    Note:
        Window handles are volatile. If you close an app and reopen it, it's handle will likely have changed.

    Args:
        take_away_focus (bool): If set to ``True``, ``wait_for_focus`` will put the desktop window in focus after Roblox gets in focus. Defaults to ``True``.

    Returns:
        int: The window handle for the Roblox window that made the function exit. A window handle is a unique integer that is used to identify a specific window.
    """

    hwnd = win32gui.GetForegroundWindow()

    while win32gui.GetWindowText(hwnd) != "Roblox":
        hwnd = win32gui.GetForegroundWindow()

    if take_away_focus:
        pydirectinput.press("altleft")
        win32gui.SetForegroundWindow(win32gui.GetDesktopWindow())

    return hwnd


__all__ = ["wait_for_focus"]
