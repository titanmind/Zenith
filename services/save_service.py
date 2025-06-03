from pathlib import Path
from models.world import World


class SaveService:
    def save(self, world: World, target: Path) -> None:
        ...

    def load(self, source: Path) -> World:
        ...
