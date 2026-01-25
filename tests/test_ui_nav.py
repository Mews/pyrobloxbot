import pytest
from unittest.mock import patch
import pyrobloxbot as bot


class TestUiNavigation:
    @pytest.fixture(autouse=True)
    def setup_mocks(self):
        with patch("pyrobloxbot.core.dinput") as self.mock_dinput:
            yield

    def test_toggle_ui_navigation(self):
        bot.state.UI_NAV_ENABLED = False

        bot.toggle_ui_navigation()

        self.mock_dinput.press.assert_called_once_with(bot.UI_NAV_KEY)
        assert bot.state.UI_NAV_ENABLED

    @pytest.mark.parametrize(
        "direction, expected_key",
        [
            ("up", "up"),
            ("u", "up"),
            ("down", "down"),
            ("d", "down"),
            ("left", "left"),
            ("l", "left"),
            ("right", "right"),
            ("r", "right"),
        ],
    )
    def test_ui_navigate(self, direction, expected_key):
        bot.ui_navigate(direction)

        self.mock_dinput.press.assert_called_with(expected_key)

    def test_ui_navigate_invalid_direction(self):
        with pytest.raises(bot.exceptions.InvalidUiDirectionException):
            bot.ui_navigate("hello world")

    @patch("pyrobloxbot.core.toggle_ui_navigation")
    def test_ui_navigate_up(self, mock_toggle_ui_nav):
        bot.state.UI_NAV_ENABLED = False

        bot.ui_navigate_up()

        mock_toggle_ui_nav.assert_called_once()
        self.mock_dinput.press.assert_called_with("up")

    @patch("pyrobloxbot.core.toggle_ui_navigation")
    def test_ui_navigate_down(self, mock_toggle_ui_nav):
        bot.state.UI_NAV_ENABLED = False

        bot.ui_navigate_down()

        mock_toggle_ui_nav.assert_called_once()
        self.mock_dinput.press.assert_called_with("down")

    @patch("pyrobloxbot.core.toggle_ui_navigation")
    def test_ui_navigate_left(self, mock_toggle_ui_nav):
        bot.state.UI_NAV_ENABLED = False

        bot.ui_navigate_left()

        mock_toggle_ui_nav.assert_called_once()
        self.mock_dinput.press.assert_called_with("left")

    @patch("pyrobloxbot.core.toggle_ui_navigation")
    def test_ui_navigate_right(self, mock_toggle_ui_nav):
        bot.state.UI_NAV_ENABLED = False

        bot.ui_navigate_right()

        mock_toggle_ui_nav.assert_called_once()
        self.mock_dinput.press.assert_called_with("right")

    @patch("pyrobloxbot.core.toggle_ui_navigation")
    def test_ui_click(self, mock_toggle_ui_nav):
        bot.state.UI_NAV_ENABLED = False

        bot.ui_click()

        mock_toggle_ui_nav.assert_called_once()
        self.mock_dinput.press.assert_called_with("enter")

    @patch("pyrobloxbot.core.Controller")
    @patch("pyrobloxbot.core.wait")
    @patch("pyrobloxbot.core.toggle_ui_navigation")
    def test_ui_scroll_up(self, mock_toggle_ui_nav, mock_wait, mock_controller_class):
        from pynput.keyboard import Key

        mock_kb = mock_controller_class.return_value
        bot.state.UI_NAV_ENABLED = False
        ticks = 3

        bot.ui_scroll_up(ticks=ticks, delay=0.05)

        mock_toggle_ui_nav.assert_called_once()

        assert mock_kb.press.call_count == ticks
        assert mock_kb.release.call_count == ticks
        mock_kb.press.assert_called_with(Key.page_up)

        # Assert 3: Delay logic
        assert mock_wait.call_count == ticks
        mock_wait.assert_called_with(0.05)

    @patch("pyrobloxbot.core.Controller")
    @patch("pyrobloxbot.core.wait")
    @patch("pyrobloxbot.core.toggle_ui_navigation")
    def test_ui_scroll_down(self, mock_toggle_ui_nav, mock_wait, mock_controller_class):
        from pynput.keyboard import Key

        mock_kb = mock_controller_class.return_value
        bot.state.UI_NAV_ENABLED = False
        ticks = 3

        bot.ui_scroll_down(ticks=ticks, delay=0.05)

        mock_toggle_ui_nav.assert_called_once()

        assert mock_kb.press.call_count == ticks
        assert mock_kb.release.call_count == ticks
        mock_kb.press.assert_called_with(Key.page_down)

        # Assert 3: Delay logic
        assert mock_wait.call_count == ticks
        mock_wait.assert_called_with(0.05)
