import pygame
from core.events import EventBus
from core.state import GameState
from models.world import World
from controllers.input_manager import InputManager

# mode‑specific controllers
from controllers.flight_controller import FlightController
from controllers.interior_controller import InteriorController
from controllers.surface_controller import SurfaceController
from controllers.galactic_controller import GalacticController
from controllers.menu_controller import MenuController


class GameController:
    """
    Owns the master input loop and delegates work to the controller that
    matches the current GameState.  Handles quitting and state‑switch logic.
    """

    def __init__(self, world: World, bus: EventBus) -> None:
        self.world = world
        self.bus = bus

        self.running = True
        self.input_mgr = InputManager()
        self.active_state: GameState = GameState.FLIGHT

        # ─────────────────────────────────── sub‑controllers ──
        # Ship / player objects may be None for now; supply once they exist.
        self.controllers = {
            GameState.FLIGHT:   FlightController(bus=bus),          # type: ignore[arg-type]
            GameState.INTERIOR: InteriorController(),
            GameState.SURFACE:  SurfaceController(),
            GameState.GALACTIC: GalacticController(),
            GameState.MENU:     MenuController(),
        }

    # ───────────────────────────────────────── event loop ──
    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            self.input_mgr.process_event(event)
            # forward raw pygame event to active mode controller
            self.controllers[self.active_state].handle_event(event)

            # simple demo: toggle ESC ↔ Flight/Menu
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if self.active_state is GameState.MENU:
                    self.change_state(GameState.FLIGHT)
                else:
                    self.change_state(GameState.MENU)

    def update(self, dt: float) -> None:
        self.world.update(dt)                              # world sim
        self.controllers[self.active_state].update(dt)     # mode‑logic

    # ───────────────────────────────────────── helpers ──
    def change_state(self, new_state: GameState) -> None:
        """Switch controller & emit event for ScreenManager."""
        if new_state is self.active_state:
            return
        self.active_state = new_state
        self.bus.emit("change_state", new_state)
