import pygame
from core.events import EventBus
from controllers.game_controller import GameController
from views.screen_manager import ScreenManager
from models.world import World
from config import Settings


class Game:
    """Owns world, controller and view manager; runs the main loop."""

    def __init__(self, screen: pygame.Surface, settings: Settings) -> None:
        self.screen = screen
        self.settings = settings
        self.clock = pygame.time.Clock()
        self.bus = EventBus()

        self.world = World(self.bus)
        self.controller = GameController(self.world, self.bus)
        self.screen_manager = ScreenManager(self.screen, self.bus)

    # ───────────────────────────────────────── public ──
    def run(self) -> None:
        while self.controller.running:
            dt = self.clock.tick(self.settings.fps) / 1000.0
            self.controller.handle_events()
            self.controller.update(dt)
            self.screen_manager.render()
            pygame.display.flip()
