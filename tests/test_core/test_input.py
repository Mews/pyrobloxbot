import pytest
from unittest.mock import patch, call

import pyrobloxbot as bot


@pytest.fixture
def mock_pydirectinput():
    with patch("pyrobloxbot.core.input.pydirectinput") as m:
        yield m


@pytest.fixture
def mock_key_down():
    with patch("pyrobloxbot.core.input.key_down") as m:
        yield m


@pytest.fixture
def mock_key_up():
    with patch("pyrobloxbot.core.input.key_up") as m:
        yield m


def test_press_key_single(mock_pydirectinput):
    bot.press_key("esc")

    mock_pydirectinput.press.assert_called_once_with("esc")


def test_press_key_multiple(mock_pydirectinput):
    keys = ["w", "a", "s", "d"]

    bot.press_key(*keys)

    mock_pydirectinput.press.assert_has_calls([call(key) for key in keys])


def test_hold_key_single(mock_key_down, mock_key_up, mock_wait):
    bot.hold_key("esc", duration=10)

    mock_key_down.assert_called_once_with("esc")
    mock_wait.assert_called_once_with(10)
    mock_key_up.assert_called_once_with("esc")


def test_hold_key_multiple(mock_key_down, mock_key_up, mock_wait):
    keys = ["w", "a", "s", "d"]

    bot.hold_key(*keys, duration=10)

    mock_key_down.assert_has_calls([call(key) for key in keys])

    mock_wait.assert_called_once_with(10)

    mock_key_up.assert_has_calls([call(key) for key in keys])


def test_aliases():
    assert bot.keyboard_action == bot.press_key
    assert bot.hold_keyboard_action == bot.hold_key


def test_key_down(mock_pydirectinput):
    bot.key_down("esc")
    mock_pydirectinput.keyDown.assert_called_once_with("esc")


def test_key_up(mock_pydirectinput):
    bot.key_up("esc")
    mock_pydirectinput.keyUp.assert_called_once_with("esc")
