import pytest
from unittest.mock import patch, call

import pyrobloxbot as bot
import pyrobloxbot.exceptions


@pytest.fixture
def mock_press_key():
    with patch("pyrobloxbot.core.roblox.press_key") as m:
        yield m


@pytest.fixture
def mock_os():
    with patch("pyrobloxbot.core.roblox.os") as m:
        yield m


@pytest.fixture
def mock_requests_get():
    with patch("requests.get") as m:
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


def test_find_servers(mock_requests_get):
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = {
        "data": [
            {
                "id": "1e2bbbeb-0013-4b65-b9aa-59b20188cc72",
                "maxPlayers": 16,
                "playing": 15,
                "playerTokens": [
                    "6AF7DC66B74887E0A69406D8EDF6FB02",
                    "52314C46653DDEAF25EE4B0338683914",
                    "57AE283C8409EE457A7C43FC42D8C868",
                    "638EB82FA026CFD7D9A6E88B23297950",
                    "C939314F88DBCF77E7F9243AE36846A7",
                ],
                "players": [],
                "fps": 59.993824,
                "ping": 56,
            },
            {
                "id": "a3d94ee4-bccb-4481-ad35-da14a79cde04",
                "maxPlayers": 16,
                "playing": 13,
                "playerTokens": [
                    "34B4BDB20F8B8BC6E08D13D583288381",
                    "2B67984D7C08EA58A3E66D5D07FC7FA2",
                    "B4869C315193ED289BB67322D4DA0259",
                    "9EAC9971D9A76732C6B0311B774DC29D",
                    "A5761CE362C1493E74FA855EA76C2B14",
                ],
                "players": [],
                "fps": 59.993122,
                "ping": 146,
            },
            {
                "id": "14b4b25a-f889-4ee4-82f3-3a747d14c288",
                "maxPlayers": 16,
                "playing": 13,
                "playerTokens": [
                    "2440412BE20AFE1B92191F34A0F2DDCD",
                    "E270C75F0289DB383B9EECFFF37B64BF",
                    "E5A9FB18BA7474D2DF6382C65F3EDEE3",
                    "81E0890FCB918BFD2941AFD6C4E5512A",
                    "1F3AF85AA70D992B979A68F0AC9760D7",
                ],
                "players": [],
                "fps": 59.990795,
                "ping": 76,
            },
        ]
    }

    assert bot.find_servers(12345) == [
        "1e2bbbeb-0013-4b65-b9aa-59b20188cc72",
        "a3d94ee4-bccb-4481-ad35-da14a79cde04",
        "14b4b25a-f889-4ee4-82f3-3a747d14c288",
    ]
    mock_requests_get.assert_called_once_with(
        "https://games.roblox.com/v1/games/12345/servers/Public?sortOrder=Desc&excludeFullGames=true&limit=10"
    )


def test_find_servers_different_parameters(mock_requests_get):
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = {
        "data": [
            {
                "id": "1e2bbbeb-0013-4b65-b9aa-59b20188cc72",
                "maxPlayers": 16,
                "playing": 15,
                "playerTokens": [
                    "6AF7DC66B74887E0A69406D8EDF6FB02",
                    "52314C46653DDEAF25EE4B0338683914",
                    "57AE283C8409EE457A7C43FC42D8C868",
                    "638EB82FA026CFD7D9A6E88B23297950",
                    "C939314F88DBCF77E7F9243AE36846A7",
                ],
                "players": [],
                "fps": 59.993824,
                "ping": 56,
            },
        ]
    }

    bot.find_servers(12345, limit=50, descending=False, ignore_full_servers=False)

    mock_requests_get.assert_called_once_with(
        "https://games.roblox.com/v1/games/12345/servers/Public?sortOrder=Asc&excludeFullGames=false&limit=50"
    )


def test_find_servers_api_error(mock_requests_get):
    mock_requests_get.return_value.status_code = 400
    mock_requests_get.return_value.json.return_value = {
        "errors": [
            {"code": 0, "message": "Allowed values: 10, 25, 50, 100", "field": "limit"}
        ]
    }

    with pytest.raises(pyrobloxbot.exceptions.RobloxApiException):
        bot.find_servers(12345)


def test_find_servers_http_error(mock_requests_get):
    mock_requests_get.return_value.status_code = 400
    mock_requests_get.return_value.json.return_value = {"data": {}}

    bot.find_servers(12345)

    mock_requests_get.return_value.raise_for_status.assert_called_once()


def test_find_servers_no_data(mock_requests_get):
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = {}

    with pytest.raises(pyrobloxbot.exceptions.RobloxApiException):
        bot.find_servers(12345)
