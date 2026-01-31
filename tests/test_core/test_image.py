import pytest
from unittest.mock import patch, Mock

import pyrobloxbot as bot


@pytest.fixture
def mock_pyscreeze():
    with patch("pyrobloxbot.core.image.pyscreeze") as m:

        class MockException(Exception):
            pass

        m.ImageNotFoundException = MockException
        yield m


@pytest.fixture
def mock_ImageGrab():
    with patch("pyrobloxbot.core.image.ImageGrab") as m:
        yield m


def test_image_is_visible_no_exception(mock_pyscreeze, mock_ImageGrab):
    mock_screenshot = Mock()
    mock_ImageGrab.grab.return_value = mock_screenshot

    retv = bot.image_is_visible("some/image.png", 0.5)

    mock_ImageGrab.grab.assert_called_once_with(all_screens=True)

    mock_pyscreeze.locate.assert_called_once_with(
        needleImage="some/image.png", haystackImage=mock_screenshot, confidence=0.5
    )

    assert retv


def test_image_is_visible_with_exception(mock_pyscreeze, mock_ImageGrab):
    mock_pyscreeze.locate.side_effect = mock_pyscreeze.ImageNotFoundException

    mock_screenshot = Mock()
    mock_ImageGrab.grab.return_value = mock_screenshot

    retv = bot.image_is_visible("some/image.png", 0.5)

    mock_ImageGrab.grab.assert_called_once_with(all_screens=True)

    mock_pyscreeze.locate.assert_called_once_with(
        needleImage="some/image.png", haystackImage=mock_screenshot, confidence=0.5
    )

    assert not retv
