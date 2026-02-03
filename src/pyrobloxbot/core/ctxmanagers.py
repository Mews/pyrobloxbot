from pygetwindow import getActiveWindow


class restore_focus:
    def __enter__(self):
        self.previous_window = getActiveWindow()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.previous_window.activate()


__all__ = ["restore_focus"]
