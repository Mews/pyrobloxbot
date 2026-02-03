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


def test_join_game(mock_os):
    game_id = 12345
    expected_command = (
        f'start "" "roblox://experiences/start?placeId={game_id}&type=InGame"'
    )

    bot.join_game(12345)

    mock_os.system.assert_called_once_with(command=expected_command)


def test_join_game_resets_ui_nav_enabled(mock_os):
    bot.state._UI_NAV_ENABLED = True

    bot.join_game(12345)

    assert not bot.state.is_ui_nav_enabled()


def test_join_user(mock_os):
    user_id = 12345
    expected_command = (
        f'start "" "roblox://experiences/start?userId={user_id}&type=FollowUser"'
    )

    bot.join_user(user_id)

    mock_os.system.assert_called_once_with(command=expected_command)


def test_join_private_server(mock_os):
    game_id = 12345
    private_server_link_code = 67890

    expected_command = f'start "" "roblox://experiences/start?placeId={game_id}&linkCode={private_server_link_code}&type=InGame"'

    bot.join_private_server(game_id, private_server_link_code)

    mock_os.system.assert_called_once_with(command=expected_command)


def test_join_server(mock_os):
    game_id = 12345
    job_id = "ea556-1235-ashgv-1234"

    expected_command = f'start "" "roblox://experiences/start?placeId={game_id}&gameInstanceId={job_id}&type=InGame"'

    bot.join_server(game_id, job_id)

    mock_os.system.assert_called_once_with(command=expected_command)
