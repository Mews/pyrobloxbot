import pytest
from unittest.mock import patch
import pyrobloxbot as bot


class TestKeyboardAction:
    @pytest.fixture(autouse=True)
    def setup_mocks(self):
        with patch("pyrobloxbot.core.dinput") as self.mock_dinput:
            yield

    def test_keyboard_action(self):
        bot.keyboard_action("w")

        self.mock_dinput.press.assert_called_once_with("w")

    def test_keyboard_action_multiple_keys(self):
        keys = ["w", "a", "s", "d"]
        bot.keyboard_action(*keys)

        assert self.mock_dinput.press.call_count == len(keys)

        from unittest.mock import call

        expected_calls = [call(k) for k in keys]
        self.mock_dinput.press.assert_has_calls(expected_calls)


class TestHoldKeyboardAction:
    @pytest.fixture(autouse=True)
    def setup_mocks(self):
        with (
            patch("pyrobloxbot.core.dinput") as self.mock_dinput,
            patch("pyrobloxbot.core.wait") as self.mock_wait,
        ):
            yield

    def test_hold_keyboard_action(self):
        bot.hold_keyboard_action("w", duration=10)

        self.mock_dinput.keyDown.assert_called_once_with("w")
        self.mock_wait.assert_called_once_with(10)
        self.mock_dinput.keyUp.assert_called_once_with("w")

    def test_hold_keyboard_action_multiple_keys(self):
        keys = ["w", "a", "s", "d"]
        bot.hold_keyboard_action(*keys, duration=10)

        assert self.mock_dinput.keyUp.call_count == len(keys)
        assert self.mock_dinput.keyDown.call_count == len(keys)

        from unittest.mock import call

        expected_calls = [call(k) for k in keys]
        self.mock_dinput.keyUp.assert_has_calls(expected_calls)
        self.mock_wait.assert_called_once_with(10)
        self.mock_dinput.keyDown.assert_has_calls(expected_calls)


class TestPressKey:
    @pytest.fixture(autouse=True)
    def setup_mocks(self):
        with patch("pyrobloxbot.core.dinput") as self.mock_dinput:
            yield

    def test_press_key(self):
        bot.press_key("w")

        self.mock_dinput.press.assert_called_once_with("w")

    def test_press_key_multiple_keys(self):
        keys = ["w", "a", "s", "d"]
        bot.press_key(*keys)

        assert self.mock_dinput.press.call_count == len(keys)

        from unittest.mock import call

        expected_calls = [call(k) for k in keys]
        self.mock_dinput.press.assert_has_calls(expected_calls)


class TestHoldKey:
    @pytest.fixture(autouse=True)
    def setup_mocks(self):
        with (
            patch("pyrobloxbot.core.dinput") as self.mock_dinput,
            patch("pyrobloxbot.core.wait") as self.mock_wait,
        ):
            yield

    def test_hold_key(self):
        bot.hold_key("w", duration=10)

        self.mock_dinput.keyDown.assert_called_once_with("w")
        self.mock_wait.assert_called_once_with(10)
        self.mock_dinput.keyUp.assert_called_once_with("w")

    def test_hold_key_multiple_keys(self):
        keys = ["w", "a", "s", "d"]
        bot.hold_key(*keys, duration=10)

        assert self.mock_dinput.keyUp.call_count == len(keys)
        assert self.mock_dinput.keyDown.call_count == len(keys)

        from unittest.mock import call

        expected_calls = [call(k) for k in keys]
        self.mock_dinput.keyUp.assert_has_calls(expected_calls)
        self.mock_wait.assert_called_once_with(10)
        self.mock_dinput.keyDown.assert_has_calls(expected_calls)


class TestKeyDown:
    @pytest.fixture(autouse=True)
    def setup_mocks(self):
        with patch("pyrobloxbot.core.dinput") as self.mock_dinput:
            yield

    def test_key_down(self):
        bot.key_down("w")

        self.mock_dinput.keyDown.assert_called_once_with("w")
        self.mock_dinput.keyUp.assert_not_called()


class TestKeyUp:
    @pytest.fixture(autouse=True)
    def setup_mocks(self):
        with patch("pyrobloxbot.core.dinput") as self.mock_dinput:
            yield

    def test_key_up(self):
        bot.key_up("w")

        self.mock_dinput.keyUp.assert_called_once_with("w")
        self.mock_dinput.keyDown.assert_not_called()
