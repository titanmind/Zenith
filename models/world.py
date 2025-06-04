from typing import List

from config import Settings                     # NEW
from core.events import EventBus
from models.star_system import StarSystem
from services.procgen_service import ProcGenService


class World:
    """Container for every star system plus meta‑state."""

    def __init__(self, bus: EventBus) -> None:
        self.bus = bus
        self.systems: List[StarSystem] = []
        self.active_system: StarSystem | None = None

        # deterministic first system based on global seed
        procgen = ProcGenService()
        system = procgen.generate_star_system(Settings().seed)   # UPDATED
        self.systems.append(system)
        self.active_system = system

    # --------------------------------------------------------------------- #
    def update(self, dt: float) -> None:
        if self.active_system:
            self.active_system.update(dt)
