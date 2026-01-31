import pytest

from unittest.mock import patch, MagicMock, call
import pyrobloxbot as bot


@pytest.fixture
def mock_roblox_not_active_window_env():
    patches = [
        patch("pyrobloxbot.core.decorators.getActiveWindow", return_value="Not None"),
        patch("pyrobloxbot.core.decorators.pydirectinput"),
        patch("pyrobloxbot.core.decorators.getWindowsWithTitle"),
        patch("pyrobloxbot.core.decorators.GetWindowText", return_value="Not Roblox"),
        patch("pyrobloxbot.core.decorators.GetForegroundWindow"),
    ]

    mocks = [p.start() for p in patches]

    yield {
        "getActiveWindow": mocks[0],
        "pydirectinput": mocks[1],
        "getWindowsWithTitle": mocks[2],
        "GetWindowText": mocks[3],
        "GetForegroundWindow": mocks[4],
    }

    for p in patches:
        p.stop()


@pytest.fixture
def mock_roblox_active_window_env():
    patches = [
        patch("pyrobloxbot.core.decorators.getActiveWindow", return_value="Not None"),
        patch("pyrobloxbot.core.decorators.pydirectinput"),
        patch("pyrobloxbot.core.decorators.getWindowsWithTitle"),
        patch("pyrobloxbot.core.decorators.GetWindowText", return_value="Roblox"),
        patch("pyrobloxbot.core.decorators.GetForegroundWindow"),
    ]

    mocks = [p.start() for p in patches]

    yield {
        "getActiveWindow": mocks[0],
        "pydirectinput": mocks[1],
        "getWindowsWithTitle": mocks[2],
        "GetWindowText": mocks[3],
        "GetForegroundWindow": mocks[4],
    }

    for p in patches:
        p.stop()


@pytest.fixture
def mock_roblox_not_open_window_env():
    patches = [
        patch("pyrobloxbot.core.decorators.getActiveWindow", return_value="Not None"),
        patch("pyrobloxbot.core.decorators.pydirectinput"),
        patch("pyrobloxbot.core.decorators.getWindowsWithTitle", return_value=[]),
        patch("pyrobloxbot.core.decorators.GetWindowText", return_value="Not Roblox"),
        patch("pyrobloxbot.core.decorators.GetForegroundWindow"),
    ]

    mocks = [p.start() for p in patches]

    yield {
        "getActiveWindow": mocks[0],
        "pydirectinput": mocks[1],
        "getWindowsWithTitle": mocks[2],
        "GetWindowText": mocks[3],
        "GetForegroundWindow": mocks[4],
    }

    for p in patches:
        p.stop()


def test_require_focus_window_already_active(mock_roblox_active_window_env):
    @bot.decorators.require_focus
    def dummy_function():
        return "success"

    assert dummy_function() == "success"


def test_require_focus_no_roblox_window(mock_roblox_not_open_window_env):
    @bot.decorators.require_focus
    def dummy_function():
        return "success"

    with pytest.raises(bot.exceptions.NoRobloxWindowException):
        dummy_function()


def test_require_focus_window_not_already_active(mock_roblox_not_active_window_env):
    mock_window_env = mock_roblox_not_active_window_env
    mock_window = MagicMock()
    mock_window.title = "Roblox"

    mock_window_env["getWindowsWithTitle"].return_value = [mock_window]

    @bot.decorators.require_focus
    def dummy_function():
        return "success"

    assert dummy_function() == "success"

    mock_window_env["pydirectinput"].press.assert_called_once_with("altleft")
    mock_window.activate.assert_called_once()


def test_require_focus_window_not_already_active_with_maximize_option(
    mock_roblox_not_active_window_env,
):
    mock_window_env = mock_roblox_not_active_window_env

    mock_window = MagicMock()
    mock_window.title = "Roblox"

    mock_window_env["getWindowsWithTitle"].return_value = [mock_window]

    @bot.decorators.require_focus
    def dummy_function():
        return "success"

    bot.options.maximize_roblox_window = True
    assert dummy_function() == "success"

    mock_window_env["pydirectinput"].press.assert_called_once_with("altleft")
    mock_window.maximize.assert_called_once()
    mock_window.activate.assert_called_once()


def test_require_focus_window_not_already_active_with_restore_option(
    mock_roblox_not_active_window_env,
):
    mock_window_env = mock_roblox_not_active_window_env

    mock_window = MagicMock()
    mock_window.title = "Roblox"

    mock_window_env["getWindowsWithTitle"].return_value = [mock_window]

    mock_prev_window = MagicMock()
    mock_window_env["getActiveWindow"].return_value = mock_prev_window

    @bot.decorators.require_focus
    def dummy_function():
        return "success"

    bot.options.restore_focus_after_action = True
    assert dummy_function() == "success"

    mock_window_env["pydirectinput"].press.assert_has_calls([call("altleft")] * 2)
    mock_window.activate.assert_called_once()

    mock_prev_window.activate.assert_called_once()


def test_require_focus_roblox_is_active_with_force_focus_false(
    mock_roblox_active_window_env,
):
    bot.options.force_focus = False

    @bot.decorators.require_focus
    def dummy_function():
        return "success"

    assert dummy_function() == "success"


def test_require_focus_roblox_isnt_active_with_force_focus_false(
    mock_roblox_not_active_window_env,
):
    bot.options.force_focus = False

    dummy_func = MagicMock()

    @bot.decorators.require_focus
    def dummy_function():
        dummy_func()
        return "success"

    assert dummy_function() is None
    dummy_func.assert_not_called()


def test_require_focus_roblox_not_open_with_force_focus_false(
    mock_roblox_not_open_window_env,
):
    bot.options.force_focus = False

    dummy_func = MagicMock()

    @bot.decorators.require_focus
    def dummy_function():
        dummy_func()
        return "success"

    assert dummy_function() is None
    dummy_func.assert_not_called()


@patch("pyrobloxbot.decorators.state")
def test_resets_state(mock_state):
    @bot.decorators.resets_state
    def dummy_function():
        return "success"

    assert dummy_function() == "success"
    mock_state._reset.assert_called_once()


@patch("pyrobloxbot.decorators.state")
def test_resets_state_still_resets_if_fn_raises(mock_state):
    @bot.decorators.resets_state
    def dummy_function():
        raise Exception

    with pytest.raises(Exception):
        dummy_function()

    mock_state._reset.assert_called_once()


@pytest.fixture
def mock_toggle_ui_navigation():
    with patch("pyrobloxbot.core.ui.toggle_ui_navigation") as m:

        def toggle_value():
            bot.state._UI_NAV_ENABLED = not bot.state._UI_NAV_ENABLED

        m.side_effect = toggle_value

        yield m


@pytest.mark.parametrize("initial_nav_state", [True, False])
@pytest.mark.parametrize("function_behavior", ["success", "fail", "toggle"])
def test_requires_ui_navigation_mode_final_state_is_starting_state(
    mock_toggle_ui_navigation, initial_nav_state, function_behavior
):
    @bot.decorators.requires_ui_navigation_mode
    def dummy_function():
        if function_behavior == "fail":
            raise Exception
        if function_behavior == "success":
            return "success"
        if function_behavior == "toggle":
            mock_toggle_ui_navigation()

    bot.state._UI_NAV_ENABLED = initial_nav_state

    try:
        dummy_function()
    except Exception:
        assert function_behavior == "fail"

    assert bot.state.is_ui_nav_enabled() == initial_nav_state, (
        "Didn't restore state correctly"
    )


def test_requires_ui_navigation_mode(mock_toggle_ui_navigation):
    @bot.decorators.requires_ui_navigation_mode
    def dummy_function():
        return "success"

    bot.state._UI_NAV_ENABLED = False
    assert dummy_function() == "success"
    assert mock_toggle_ui_navigation.call_count == 2


def test_requires_ui_navigation_mode_already_enabled(mock_toggle_ui_navigation):
    @bot.decorators.requires_ui_navigation_mode
    def dummy_function():
        return "success"

    bot.state._UI_NAV_ENABLED = True
    assert dummy_function() == "success"
    assert mock_toggle_ui_navigation.call_count == 0


def test_apply_cooldown(mock_wait):
    @bot.decorators.apply_cooldown
    def dummy_function():
        return "success"

    bot.options.action_cooldown = 10

    assert dummy_function() == "success"

    mock_wait.assert_called_once_with(10)


def test_apply_cooldown_zero_cooldown(mock_wait):
    @bot.decorators.apply_cooldown
    def dummy_function():
        return "success"

    bot.options.action_cooldown = 0

    assert dummy_function() == "success"

    mock_wait.assert_not_called()


def test_apply_cooldown_negative_cooldown(mock_wait):
    @bot.decorators.apply_cooldown
    def dummy_function():
        return "success"

    bot.options.action_cooldown = -1

    assert dummy_function() == "success"

    mock_wait.assert_not_called()


def test_apply_cooldown_nested_only_waits_once(mock_wait):
    @bot.decorators.apply_cooldown
    def dummy_function():
        return "success"

    @bot.decorators.apply_cooldown
    def dummy_function2():
        return dummy_function()

    bot.options.action_cooldown = 10

    assert dummy_function2() == "success"

    mock_wait.assert_called_once_with(10)


def test_apply_cooldown_nested_thrice_only_waits_once(mock_wait):
    @bot.decorators.apply_cooldown
    def dummy_function():
        return "success"

    @bot.decorators.apply_cooldown
    def dummy_function2():
        return dummy_function()

    @bot.decorators.apply_cooldown
    def dummy_function3():
        return dummy_function2()

    bot.options.action_cooldown = 10

    assert dummy_function3() == "success"

    mock_wait.assert_called_once_with(10)


def test_apply_cooldown_nested_through_decorator_only_waits_once(mock_wait):
    def dummy_decorator(fn):
        def wrapper():
            dummy_function()
            return fn()

        return wrapper

    @bot.decorators.apply_cooldown
    def dummy_function():
        return "decorating"

    @bot.decorators.apply_cooldown
    @dummy_decorator
    def dummy_function2():
        return "success"

    bot.options.action_cooldown = 10

    assert dummy_function2() == "success"

    mock_wait.assert_called_once_with(10)


def test_apply_cooldown_fail_resets_COOLDOWN_SET():
    @bot.decorators.apply_cooldown
    def dummy_function():
        raise Exception

    with pytest.raises(Exception):
        dummy_function()

    assert not bot.state._COOLDOWN_SET


def test_apply_cooldown_nested_fail_resets_COOLDOWN_SET():
    @bot.decorators.apply_cooldown
    def dummy_function():
        raise Exception

    @bot.decorators.apply_cooldown
    def dummy_function2():
        return dummy_function()

    bot.options.action_cooldown = 10

    with pytest.raises(Exception):
        dummy_function2()

    assert not bot.state._COOLDOWN_SET
