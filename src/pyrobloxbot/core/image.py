from .decorators import require_focus
import pyscreeze
from PIL import ImageGrab
import typing
import time
from ..utils import wait
from ..exceptions import ImageTimeoutExpired


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


@require_focus
def wait_for_image(
    image_path: str,
    confidence: float = 0.9,
    timeout: typing.Optional[int] = None,
    continue_after_timeout: bool = False,
) -> bool:
    """Sleep until a given image is visible on screen.

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
        timeout (typing.Optional[int], optional): A timeout in seconds,
            after which the function stops waiting for the image.
            If set to ``None``, it will wait indefinitely.

            Defaults to ``None``.
        continue_after_timeout (bool, optional): If set to ``False``,
            the function will raise :py:class:`pyrobloxbot.exceptions.ImageTimeoutExpired` when the timeout expires.

            If set to ``True``, it will just stop sleeping without raising anything.

            Defaults to ``False``.

    Raises:
        ImageTimeoutExpired: Raised when the timeout expires and ``continue_after_timeout`` is ``False``

    Returns:
        bool: ``True`` if the image was found, or ``False`` if the timeout expired.
    """

    start = time.perf_counter()
    while not image_is_visible(image_path, confidence):
        if timeout is not None and time.perf_counter() - start >= timeout:
            if continue_after_timeout:
                return False
            else:
                raise ImageTimeoutExpired(
                    f'Didn\'t find "{image_path}" after {timeout} seconds.'
                )
        wait(0.1)

    return True


__all__ = ["image_is_visible", "wait_for_image"]
