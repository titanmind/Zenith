import pygame
from core.state import GameState
from views.flight_view import FlightView
from views.interior_view import InteriorView
from views.surface_view import SurfaceView
from views.galactic_map_view import GalacticMapView
from views.menu_view import MenuView
from core.events import EventBus


class ScreenManager:
    """Switches active view based on GameState events."""

    def __init__(self, screen: pygame.Surface, bus: EventBus) -> None:
        self.screen = screen
        self.bus = bus
        self.views = {
            GameState.FLIGHT: FlightView(screen),
            GameState.INTERIOR: InteriorView(screen),
            GameState.SURFACE: SurfaceView(screen),
            GameState.GALACTIC: GalacticMapView(screen),
            GameState.MENU: MenuView(screen),
        }
        self.active_state = GameState.FLIGHT
        self.bus.subscribe("change_state", self._on_change_state)

    def _on_change_state(self, state: GameState) -> None:
        self.active_state = state

    def render(self) -> None:
        self.views[self.active_state].render()
