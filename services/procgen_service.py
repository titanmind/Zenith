from random import Random
from models.star_system import StarSystem


class ProcGenService:
    """Procedural generation façade."""

    def __init__(self) -> None:
        self.rng = Random()

    def generate_star_system(self, seed: int | None = None) -> StarSystem:
        ...
