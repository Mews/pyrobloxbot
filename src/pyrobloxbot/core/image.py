from .decorators import require_focus
import pyautogui


@require_focus
def image_is_visible(image_path: str, confidence: float = 0.9) -> bool:
    """Checks whether a given image is visible in the roblox window

    :param image_path: The path to the image file to check
    :type image_path: str
    :param confidence: How confident the function has to be to return True, must be between 0 and 0.999, defaults to 0.9\n
                       If this value is too low it may give false positives

    :type confidence: float, optional
    :return: Whether or not the image is visible
    :rtype: bool
    """

    try:
        pyautogui.locateOnScreen(image_path, confidence=confidence)
        return True
    except pyautogui.ImageNotFoundException:
        return False


__all__ = ["image_is_visible"]
