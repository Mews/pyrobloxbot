from dataclasses import dataclass


@dataclass
class _BotOptions:
    pass

    def _reset(self):
        self.__init__()


__all__ = ["_BotOptions"]
