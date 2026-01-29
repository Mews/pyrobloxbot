import pytest
from pyrobloxbot.bot.state import _BotState


@pytest.fixture
def state():
    return _BotState()


def test_default_values(state):
    assert not state._SHIFT_LOCK_ENABLED
    assert not state._UI_NAV_ENABLED


def test_is_ui_nav_enabled(state):
    assert not state.is_ui_nav_enabled()
    state._UI_NAV_ENABLED = True
    assert state.is_ui_nav_enabled()


def test_is_shift_lock_enabled(state):
    assert not state.is_shift_lock_enabled()
    state._SHIFT_LOCK_ENABLED = True
    assert state.is_shift_lock_enabled()
