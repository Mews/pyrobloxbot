from pyrobloxbot import utils
from unittest.mock import patch
import pytest


@pytest.fixture
def mock_sys():
    with patch("pyrobloxbot.utils.sys") as m:
        yield m


@pytest.fixture
def mock__thread():
    with patch("pyrobloxbot.utils._thread") as m:
        yield m


def test_build_roblox_uri():
    assert (
        utils.build_roblox_uri(
            placeId="1", userId="2", linkCode="3", gameInstanceId="4", type="5"
        )
        == "roblox://experiences/start?placeId=1&userId=2&linkCode=3&gameInstanceId=4&type=5"
    )


def test_failsafe_calls_interrupt_main(mock__thread, mock_sys):
    utils._failsafe()
    mock__thread.interrupt_main.assert_called_once()
