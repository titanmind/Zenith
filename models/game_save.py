from dataclasses import dataclass


@dataclass
class GameSave:
    """Metadata stored with a save file."""

    seed: int
    player_version: str
    ship_version: str
    world_version: str
