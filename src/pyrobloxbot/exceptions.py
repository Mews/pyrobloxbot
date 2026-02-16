class NoRobloxWindowException(Exception):
    """Raised when a function can't find a Roblox window to focus"""

    pass


class RobloxApiException(Exception):
    """Raised when an error occurs in a call to the Roblox api"""

    pass


__all__ = [
    "NoRobloxWindowException",
    "RobloxApiException",
]
