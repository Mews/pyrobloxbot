import pytest
from unittest.mock import patch
import pyrobloxbot as bot


class TestWalk:
    @pytest.fixture(autouse=True)
    def setup_mocks(self):
        with (
            patch("pyrobloxbot.core.input.dinput") as self.mock_dinput,
            patch("pyrobloxbot.utils.sleep") as self.mock_wait,
        ):
            yield

    def test_walk_forward(self):
        bot.walk_forward(10)

        self.mock_dinput.keyDown.assert_called_once_with("w")
        self.mock_wait.assert_called_once_with(10)
        self.mock_dinput.keyUp.assert_called_once_with("w")

    def test_walk_left(self):
        bot.walk_left(10)

        self.mock_dinput.keyDown.assert_called_once_with("a")
        self.mock_wait.assert_called_once_with(10)
        self.mock_dinput.keyUp.assert_called_once_with("a")

    def test_walk_right(self):
        bot.walk_right(10)

        self.mock_dinput.keyDown.assert_called_once_with("d")
        self.mock_wait.assert_called_once_with(10)
        self.mock_dinput.keyUp.assert_called_once_with("d")

    def test_walk_back(self):
        bot.walk_back(10)

        self.mock_dinput.keyDown.assert_called_once_with("s")
        self.mock_wait.assert_called_once_with(10)
        self.mock_dinput.keyUp.assert_called_once_with("s")

    def test_walk(self):
        bot.walk("forward", duration=5)

        self.mock_dinput.keyDown.assert_called_once_with("w")
        self.mock_wait.assert_called_once_with(5)
        self.mock_dinput.keyUp.assert_called_once_with("w")

    def test_walk_multiple_directions(self):
        bot.walk("forward", "left", "backwards", "right", duration=5)

        assert self.mock_dinput.keyUp.call_count == 4
        assert self.mock_dinput.keyDown.call_count == 4

        from unittest.mock import call

        expected_calls = [call(k) for k in ("w", "a", "s", "d")]

        self.mock_dinput.keyUp.assert_has_calls(expected_calls)
        self.mock_wait.assert_called_once_with(5)
        self.mock_dinput.keyDown.assert_has_calls(expected_calls)

    def test_walk_invalid_direction(self):
        with pytest.raises(bot.exceptions.InvalidWalkDirectionException):
            bot.walk("Hello world!", duration=15)
