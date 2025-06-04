from models.biome import Biome
import math


class Planet:
    """Single planet or moon."""

    def __init__(
        self,
        name: str,
        radius_km: float,
        orbit_radius_km: float,
        orbital_period_h: float,
        theta: float = 0.0,
    ) -> None:
        self.name = name
        self.radius_km = radius_km
        self.orbit_radius_km = orbit_radius_km
        self.orbital_period_h = orbital_period_h
        self.theta = theta
        self.biomes: list[Biome] = []

    def update(self, dt: float) -> None:
        """Advance orbital position."""
        if self.orbital_period_h > 0:
            self.theta += dt / (self.orbital_period_h * 3600) * 2 * math.pi
            self.theta %= 2 * math.pi
