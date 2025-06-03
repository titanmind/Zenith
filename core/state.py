from enum import Enum, auto


class GameState(Enum):
    FLIGHT = auto()
    INTERIOR = auto()
    SURFACE = auto()
    GALACTIC = auto()
    MENU = auto()
