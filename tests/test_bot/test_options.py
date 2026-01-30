import pytest

from pyrobloxbot.bot.options import _BotOptions


@pytest.fixture
def options():
    return _BotOptions()


def assert_options_are_default(options):
    assert options.maximize_roblox_window == False  #  noqa: E712
    assert options.restore_focus_after_action == False  #  noqa: E712


def test_default_values(options):
    assert_options_are_default(options)


def test__reset(options):
    options.maximize_roblox_window = True
    options.restore_focus_after_action = True
    options._reset()
    assert_options_are_default(options)
