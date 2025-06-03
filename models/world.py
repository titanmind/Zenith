from typing import List
from core.events import EventBus
from models.star_system import StarSystem


class World:
    """Container for every star system plus meta‑state."""

    def __init__(self, bus: EventBus) -> None:
        self.bus = bus
        self.systems: List[StarSystem] = []
        self.active_system: StarSystem | None = None

    def update(self, dt: float) -> None:
        if self.active_system:
            self.active_system.update(dt)
