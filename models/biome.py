class Biome:
    """Surface patch with climate + resources."""

    def __init__(self, archetype: str) -> None:
        self.archetype = archetype

    def update(self, dt: float) -> None:
        ...
