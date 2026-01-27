import pytest
from unittest.mock import patch
import pyrobloxbot as bot


class TestJump:
    @pytest.fixture(autouse=True)
    def setup_mocks(self):
        with (
            patch("pyrobloxbot.core.input.dinput") as self.mock_dinput,
            patch("pyrobloxbot.utils.sleep") as self.mock_wait,
        ):
            yield

    def test_jump(self):
        bot.jump()

        self.mock_dinput.press.assert_called_once_with("space")

    def test_jump_multiple_times(self):
        bot.jump(10)

        from unittest.mock import call

        expected_calls = [call("space")] * 10
        self.mock_dinput.press.assert_has_calls(expected_calls)

    def test_jump_multiple_times_with_delay(self):
        bot.jump(5, 5)

        from unittest.mock import call

        expected_calls = [call("space")] * 5
        self.mock_dinput.press.assert_has_calls(expected_calls)

        expected_calls = [call(5)] * 5
        self.mock_wait.assert_has_calls(expected_calls)

    def test_jump_continuous(self):
        bot.jump_continuous(10)

        self.mock_dinput.keyDown.assert_called_once_with("space")
        self.mock_wait.assert_called_once_with(10)
        self.mock_dinput.keyUp.assert_called_once_with("space")
