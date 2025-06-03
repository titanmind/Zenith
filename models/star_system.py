from typing import List
from models.planet import Planet


class StarSystem:
    """Procedurally generated system with star + planets."""

    def __init__(self, seed: int) -> None:
        self.seed = seed
        self.planets: List[Planet] = []

    def update(self, dt: float) -> None:
        for planet in self.planets:
            planet.update(dt)
