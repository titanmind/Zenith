from random import Random
from math import pi, sqrt

from config import STAR_COLORS
from models.star_system import StarSystem
from models.star import Star
from models.planet import Planet
from models.procgen import ProcGenRules


class ProcGenService:
    """Procedural generation façade."""

    def __init__(self) -> None:
        self.rng = Random()

    def generate_star_system(self, seed: int | None = None) -> StarSystem:
        """Create a basic star system using deterministic random values."""

        # Resolve seed and create a dedicated RNG
        if seed is None:
            seed = self.rng.randrange(2**32)
        rng = Random(seed)

        # Build the star system container
        system = StarSystem(seed)

        # ── Generate star -------------------------------------------------
        spectral = ProcGenRules.random_spectral_class(rng)
        luminosity = rng.uniform(0.2, 50.0)
        radius_km = rng.uniform(2.0e5, 1.5e6)
        color = rng.choice(STAR_COLORS)
        system.star = Star(spectral, luminosity, radius_km, color)

        # ── Helper for orbital period using Kepler's third law ------------
        def kepler_period(radius: float) -> float:
            mu = 1.327e11  # Sun's gravitational parameter (km^3/s^2)
            return 2 * pi * sqrt(radius**3 / mu) / 3600.0

        # ── Generate planets ---------------------------------------------
        system.planets = []
        for i in range(3):
            name = f"Planet {i + 1}"
            pradius = rng.uniform(800.0, 70000.0)
            orbit_radius = ProcGenRules.random_orbit_radius(rng)
            orbital_period = kepler_period(orbit_radius)

            planet = Planet(name, pradius, orbit_radius, orbital_period)
            system.planets.append(planet)

        return system
