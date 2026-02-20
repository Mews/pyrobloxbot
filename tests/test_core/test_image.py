import pytest
from unittest.mock import patch, Mock

import pyrobloxbot as bot
import pyrobloxbot.exceptions


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


@pytest.fixture
def mock_image_is_visible():
    with patch("pyrobloxbot.core.image.image_is_visible") as m:
        yield m


@pytest.fixture
def mock_perf_counter():
    with patch("pyrobloxbot.core.image.time.perf_counter") as m:
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


def test_wait_for_image(mock_image_is_visible, mock_perf_counter):
    mock_image_is_visible.side_effect = [False, False, True]
    mock_perf_counter.side_effect = [0, 0.1, 0.2]

    assert bot.wait_for_image("img.png", timeout=1)


def test_wait_for_image_timeout_expires(mock_image_is_visible, mock_perf_counter):
    mock_image_is_visible.side_effect = [False, False, False]
    mock_perf_counter.side_effect = [0, 1, 2]

    with pytest.raises(pyrobloxbot.exceptions.ImageTimeoutExpired):
        bot.wait_for_image("img.png", timeout=2, continue_after_timeout=False)


def test_wait_for_image_timeout_expires_continue(
    mock_image_is_visible, mock_perf_counter
):
    mock_image_is_visible.side_effect = [False, False, False]
    mock_perf_counter.side_effect = [0, 1, 2]

    assert not bot.wait_for_image("img.png", timeout=2, continue_after_timeout=True)
