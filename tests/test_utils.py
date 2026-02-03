from pyrobloxbot import utils


def test_build_roblox_uri():
    assert (
        utils.build_roblox_uri(
            placeId="1", userId="2", linkCode="3", gameInstanceId="4", type="5"
        )
        == "roblox://experiences/start?placeId=1&userId=2&linkCode=3&gameInstanceId=4&type=5"
    )
