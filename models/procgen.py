from __future__ import annotations
from random import Random


class ProcGenRules:
    """Static tables & helper maths for procedural generation."""

    # Weighted or uniform tables for various procedural values -----------------
    SPECTRAL_CLASSES: list[str] = [
        "O", "B", "A", "F", "G", "K", "M", "White Dwarf", "Red Giant"
    ]

    PLANET_TYPES: list[str] = [
        "terrestrial",
        "oceanic",
        "desert",
        "ice",
        "lava",
        "gas-giant",
        "dwarf-rock",
        "barren",
    ]

    @staticmethod
    def random_spectral_class(rng: Random | None = None) -> str:
        """Pick a stellar spectral class at random."""
        rng = rng or Random()
        return rng.choice(ProcGenRules.SPECTRAL_CLASSES)

    @staticmethod
    def random_planet_type(rng: Random | None = None) -> str:
        """Return a random planet type."""
        rng = rng or Random()
        return rng.choice(ProcGenRules.PLANET_TYPES)

    @staticmethod
    def random_orbit_radius(rng: Random | None = None) -> float:
        """Generate a random orbital radius in kilometers."""
        rng = rng or Random()
        # Roughly span from Mercury-like to far Neptune-like distances
        # 50 million km – 6 billion km
        return rng.uniform(5.0e7, 6.0e9)
