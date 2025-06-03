from models.biome import Biome


class Planet:
    """Single planet or moon."""

    def __init__(self, name: str, radius_km: float) -> None:
        self.name = name
        self.radius_km = radius_km
        self.biomes: list[Biome] = []

    def update(self, dt: float) -> None:
        ...
