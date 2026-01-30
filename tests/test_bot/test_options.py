import pytest

from pyrobloxbot.bot.options import _BotOptions


@pytest.fixture
def options():
    return _BotOptions()


def assert_options_are_default(options):
    pass


def test_default_values(options):
    assert_options_are_default(options)


def test__reset(options):
    options._reset()
    assert_options_are_default(options)
