from .decorators import require_focus
import pyscreeze
from PIL import ImageGrab


@require_focus
def image_is_visible(image_path: str, confidence: float = 0.9) -> bool:
    """Checks whether a given image is visible on screen.

    Important:
        Be aware that the screenshots are dpi aware.

        This means that a screenshot taken on one monitor might not be the same
        physical size as taken in another monitor, meaning the method might not find it.

        Being in fullscreen has the same effect.

        It is recommended to use screenshots taken on the monitor where Roblox will be running.

    Args:
        image_path (str): The path of the image to check
        confidence (float, optional): How confident the method must be to return ``True``.
            Be aware that low confidence values (<0.5) might start giving you false positives.

            Defaults to ``0.9``.

    Returns:
        bool: Whether or not the image is visible.
    """
    try:
        screen = ImageGrab.grab(all_screens=True)
        pyscreeze.locate(
            needleImage=image_path, haystackImage=screen, confidence=confidence
        )
        return True
    except pyscreeze.ImageNotFoundException:
        return False


__all__ = ["image_is_visible"]
