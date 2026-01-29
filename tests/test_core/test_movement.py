import pytest
from unittest.mock import patch, call

import pyrobloxbot as bot


@pytest.fixture
def mock_press_key():
    with patch("pyrobloxbot.core.movement.press_key") as m:
        yield m


@pytest.fixture
def mock_hold_key():
    with patch("pyrobloxbot.core.movement.hold_key") as m:
        yield m


@pytest.fixture
def mock_key_down():
    with patch("pyrobloxbot.core.movement.key_down") as m:
        yield m


@pytest.fixture
def mock_key_up():
    with patch("pyrobloxbot.core.movement.key_up") as m:
        yield m


@pytest.fixture
def mock_walk():
    with patch("pyrobloxbot.core.movement.walk") as m:
        yield m


@pytest.mark.parametrize("direction", ["f", "fw", "forward", "forwards"])
def test_walk_single_direction_forward(
    direction, mock_key_up, mock_key_down, mock_wait
):
    bot.walk(direction, duration=10)

    mock_key_down.assert_called_once_with(bot.keybinds.walk_forward)
    mock_wait.assert_called_once_with(10)
    mock_key_up.assert_called_once_with(bot.keybinds.walk_forward)


def test_walk_single_direction_forward_change_keybind(mock_key_up, mock_key_down):
    bot.keybinds.walk_forward = "esc"

    bot.walk("f", duration=1)

    mock_key_down.assert_called_once_with("esc")
    mock_key_up.assert_called_once_with("esc")


@pytest.mark.parametrize("direction", ["b", "back", "backward", "backwards"])
def test_walk_single_direction_backward(
    direction, mock_key_up, mock_key_down, mock_wait
):
    bot.walk(direction, duration=10)

    mock_key_down.assert_called_once_with(bot.keybinds.walk_back)
    mock_wait.assert_called_once_with(10)
    mock_key_up.assert_called_once_with(bot.keybinds.walk_back)


def test_walk_single_direction_backward_change_keybind(mock_key_up, mock_key_down):
    bot.keybinds.walk_back = "esc"

    bot.walk("b", duration=1)

    mock_key_down.assert_called_once_with("esc")
    mock_key_up.assert_called_once_with("esc")


@pytest.mark.parametrize("direction", ["l", "left"])
def test_walk_single_direction_left(direction, mock_key_up, mock_key_down, mock_wait):
    bot.walk(direction, duration=10)

    mock_key_down.assert_called_once_with(bot.keybinds.walk_left)
    mock_wait.assert_called_once_with(10)
    mock_key_up.assert_called_once_with(bot.keybinds.walk_left)


def test_walk_single_direction_left_change_keybind(mock_key_up, mock_key_down):
    bot.keybinds.walk_left = "esc"

    bot.walk("l", duration=1)

    mock_key_down.assert_called_once_with("esc")
    mock_key_up.assert_called_once_with("esc")


@pytest.mark.parametrize("direction", ["r", "right"])
def test_walk_single_direction_right(direction, mock_key_up, mock_key_down, mock_wait):
    bot.walk(direction, duration=10)

    mock_key_down.assert_called_once_with(bot.keybinds.walk_right)
    mock_wait.assert_called_once_with(10)
    mock_key_up.assert_called_once_with(bot.keybinds.walk_right)


def test_walk_single_direction_right_change_keybind(mock_key_up, mock_key_down):
    bot.keybinds.walk_right = "esc"

    bot.walk("r", duration=1)

    mock_key_down.assert_called_once_with("esc")
    mock_key_up.assert_called_once_with("esc")


def test_walk_multiple_directions(mock_key_up, mock_key_down, mock_wait):
    directions = ["f", "l", "r", "b"]

    bot.walk(*directions, duration=10)

    mock_key_down.assert_has_calls(
        [
            call(bot.keybinds.walk_forward),
            call(bot.keybinds.walk_left),
            call(bot.keybinds.walk_right),
            call(bot.keybinds.walk_back),
        ],
        any_order=True,
    )
    mock_wait.assert_called_once_with(10)
    mock_key_up.assert_has_calls(
        [
            call(bot.keybinds.walk_forward),
            call(bot.keybinds.walk_left),
            call(bot.keybinds.walk_right),
            call(bot.keybinds.walk_back),
        ],
        any_order=True,
    )


def test_walk_invalid_direction():
    with pytest.raises(bot.exceptions.InvalidWalkDirectionException):
        bot.walk("f", "l", "Hello world!", "b", "r", duration=2)


def test_walk_forward(mock_walk):
    bot.walk_forward(15)

    mock_walk.assert_called_once_with("f", duration=15)


def test_walk_left(mock_walk):
    bot.walk_left(15)

    mock_walk.assert_called_once_with("l", duration=15)


def test_walk_right(mock_walk):
    bot.walk_right(15)

    mock_walk.assert_called_once_with("r", duration=15)


def test_walk_back(mock_walk):
    bot.walk_back(15)

    mock_walk.assert_called_once_with("b", duration=15)


def test_jump(mock_press_key, mock_wait):
    bot.jump(10, 5)

    mock_press_key.assert_has_calls([call("space")] * 10)
    mock_wait.assert_has_calls([call(5)] * 10)


def test_jump_continous(mock_hold_key):
    bot.jump_continuous(15)

    mock_hold_key.assert_called_once_with("space", duration=15)
