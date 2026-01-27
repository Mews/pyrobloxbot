import pytest
from unittest.mock import patch, call
import pyrobloxbot as bot


class TestPlayer:
    @pytest.fixture(autouse=True)
    def setup_mocks(self):
        with patch("pyrobloxbot.core.input.dinput") as self.mock_dinput:
            yield

    def test_reset_player(self):
        bot.reset_player(interval=1)

        self.mock_dinput.press.assert_has_calls([call("esc"), call("r"), call("enter")])

    def test_leave_game(self):
        bot.leave_game(interval=1)

        self.mock_dinput.press.assert_has_calls([call("esc"), call("l"), call("enter")])

    def test_toggle_shift_lock(self):
        bot.toggle_shift_lock()

        self.mock_dinput.press.assert_called_once_with("shift")

    def test_equip_slot(self):
        bot.equip_slot(5)

        self.mock_dinput.press.assert_called_once_with("5")

    def test_equip_slot_invalid_slot(self):
        with pytest.raises(bot.exceptions.InvalidSlotNumberException):
            bot.equip_slot(11)

    @patch("pyrobloxbot.core.character.pyperclip")
    def test_chat(self, mock_pyclip):
        original_clipboard_content = "original clipboard"

        mock_pyclip.paste.return_value = original_clipboard_content
        test_message = "hello everyone"

        bot.chat(test_message)

        from unittest.mock import call

        mock_pyclip.copy.assert_has_calls(
            [call(test_message), call(original_clipboard_content)]
        )

        self.mock_dinput.press.assert_has_calls([call("/"), call("enter")])

        self.mock_dinput.keyDown.assert_has_calls([call("ctrl"), call("v")])
        self.mock_dinput.keyUp.assert_has_calls([call("ctrl"), call("v")])

    @patch("pyrobloxbot.core.roblox.os.system")
    def test_launch_game(self, mock_os_system):
        game_id = 123456
        bot.state.ui_nav_enabled = True

        bot.launch_game(game_id)

        expected_command = f"start roblox://placeId={game_id}"
        mock_os_system.assert_called_once_with(command=expected_command)

        assert bot.state.ui_nav_enabled is False
