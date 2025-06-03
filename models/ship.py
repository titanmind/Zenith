class Ship:
    """Player vessel; owns systems & interior layout."""

    def __init__(self) -> None:
        self.hull: float = 1.0
        self.systems: dict[str, float] = {}

    def update(self, dt: float) -> None:
        ...
