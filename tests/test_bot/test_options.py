import pytest

from pyrobloxbot.bot.options import _BotOptions


@pytest.fixture
def options():
    return _BotOptions()


def assert_options_are_default(options):
    assert not options.maximize_roblox_window
    assert not options.restore_focus_after_action
    assert options.action_cooldown == 0
    assert options.force_focus


def test_default_values(options):
    assert_options_are_default(options)


def test__reset(options):
    options.maximize_roblox_window = True
    options.restore_focus_after_action = True
    options.action_cooldown = 10.5
    options.force_focus = False
    options._reset()
    assert_options_are_default(options)
