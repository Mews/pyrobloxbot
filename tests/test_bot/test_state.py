import pytest
from pyrobloxbot.bot.state import _BotState


@pytest.fixture
def state():
    return _BotState()


def assert_state_is_default(state):
    assert not state._SHIFT_LOCK_ENABLED
    assert not state._UI_NAV_ENABLED
    assert not state._INVENTORY_OPEN
    assert not state._COOLDOWN_SET


def test_default_values(state):
    assert_state_is_default(state)


def test_is_ui_nav_enabled(state):
    assert not state.is_ui_nav_enabled()
    state._UI_NAV_ENABLED = True
    assert state.is_ui_nav_enabled()


def test_is_shift_lock_enabled(state):
    assert not state.is_shift_lock_enabled()
    state._SHIFT_LOCK_ENABLED = True
    assert state.is_shift_lock_enabled()


def test_is_inventory_open(state):
    assert not state.is_inventory_open()
    state._INVENTORY_OPEN = True
    assert state.is_inventory_open()


def test__reset(state):
    state._SHIFT_LOCK_ENABLED = True
    state._UI_NAV_ENABLED = True
    state._INVENTORY_OPEN = True
    state._COOLDOWN_SET = True
    state._reset()

    assert_state_is_default(state)
