from models.inventory import Inventory


class Player:
    """Avatar data independent of rendering."""

    def __init__(self) -> None:
        self.inventory = Inventory()
        self.position = (0.0, 0.0)

    def update(self, dt: float) -> None:
        ...
