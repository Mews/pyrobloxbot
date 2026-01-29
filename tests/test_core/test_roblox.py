import pytest
from unittest.mock import patch, call

import pyrobloxbot as bot


@pytest.fixture
def mock_press_key():
    with patch("pyrobloxbot.core.roblox.press_key") as m:
        yield m


@pytest.fixture
def mock_os():
    with patch("pyrobloxbot.core.roblox.os") as m:
        yield m


def test_leave_game(mock_press_key, mock_wait):
    bot.leave_game(3)

    mock_press_key.assert_has_calls([call("esc"), call("l"), call("enter")])

    mock_wait.assert_has_calls([call(3)] * 2)


def test_leave_game_resets_ui_nav_enabled(mock_press_key):
    bot.state._UI_NAV_ENABLED = True

    bot.leave_game()

    assert not bot.state.is_ui_nav_enabled()


def test_launch_game(mock_os):
    game_id = 12345
    expected_command = f"start roblox://placeId={game_id}"

    bot.launch_game(12345)

    mock_os.system.assert_called_once_with(command=expected_command)


def test_launch_game_resets_ui_nav_enabled(mock_os):
    bot.state._UI_NAV_ENABLED = True

    bot.launch_game(12345)

    assert not bot.state.is_ui_nav_enabled()
