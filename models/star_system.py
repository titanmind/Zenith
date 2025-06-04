from typing import List, Optional

from models.planet import Planet
from models.star import Star


class StarSystem:
    """Procedurally generated system with a star and its planets."""

    def __init__(self, seed: int) -> None:
        self.seed = seed
        self.star: Optional[Star] = None          # now declared explicitly
        self.planets: List[Planet] = []

    # --------------------------------------------------------------------- #
    def update(self, dt: float) -> None:
        for planet in self.planets:
            planet.update(dt)
