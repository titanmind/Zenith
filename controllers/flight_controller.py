import pygame
from core.events import EventBus


class FlightController:
    """
    Handles player input and updates while in FLIGHT mode.
    Ship/game‑play logic will be added later.
    """

    def __init__(self, bus: EventBus, ship=None) -> None:
        self.bus = bus
        self.ship = ship  # will point to the real Ship object eventually

    # ───────────────────────────────────────── input ──
    def handle_event(self, event: pygame.event.Event) -> None:
        # e.g., mouse movement, key presses
        ...

    # ───────────────────────────────────────── tick ──
    def update(self, dt: float) -> None:
        # integrate velocities, move ship, etc.
        ...
