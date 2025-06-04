"""Convenience launcher that prints FPS every second."""
import time
import pygame

# Import main module to access the same setup
import main
from core.game import Game
from config import Settings


def main_dev() -> None:
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.window_size)
    pygame.display.set_caption("Zenith (Dev)")

    game = Game(screen, settings)

    last = time.time()
    frames = 0
    while game.controller.running:
        dt = game.clock.tick(settings.fps) / 1000.0
        game.controller.handle_events()
        game.controller.update(dt)
        game.screen_manager.render()
        pygame.display.flip()
        frames += 1

        if time.time() - last >= 1.0:
            print(f"FPS: {frames}")
            frames = 0
            last = time.time()

    pygame.quit()


if __name__ == "__main__":
    main_dev()
