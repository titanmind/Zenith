from utils.vector import Vec2


class Ship:
    """Player vessel; owns systems & interior layout."""

    def __init__(self) -> None:
        self.hull: float = 1.0
        self.systems: dict[str, float] = {}
        self.position = Vec2()
        self.velocity = Vec2()
        self.orientation_deg = 0.0

    def update(self, dt: float) -> None:
        """Advance position using simple Euler integration."""
        self.position = self.position + self.velocity * dt
