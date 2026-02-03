import pytest
from unittest.mock import MagicMock, patch

import pyrobloxbot as bot


@pytest.fixture
def mock_getActiveWindow():
    with patch("pyrobloxbot.core.ctxmanagers.getActiveWindow") as m:
        yield m


def test_restore_focus(mock_getActiveWindow):
    mock_window = MagicMock()
    mock_getActiveWindow.return_value = mock_window

    def dummy_function():
        return "success"

    with bot.restore_focus():
        assert dummy_function() == "success"

    mock_window.activate.assert_called_once()
