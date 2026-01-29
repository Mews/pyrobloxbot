import pytest
from unittest.mock import patch

import pyrobloxbot as bot


@pytest.fixture
def mock_pyautogui():
    with patch("pyrobloxbot.core.image.pyautogui") as m:

        class MockException(Exception):
            pass

        m.ImageNotFoundException = MockException
        yield m


def test_image_is_visible_no_exception(mock_pyautogui):
    retv = bot.image_is_visible("some/image.png", 0.5)
    mock_pyautogui.locateOnScreen.assert_called_once_with(
        "some/image.png", confidence=0.5
    )
    assert retv


def test_image_is_visible_with_exception(mock_pyautogui):
    mock_pyautogui.locateOnScreen.side_effect = mock_pyautogui.ImageNotFoundException

    retv = bot.image_is_visible("some/image.png", 0.5)

    mock_pyautogui.locateOnScreen.assert_called_once_with(
        "some/image.png", confidence=0.5
    )
    assert not retv
