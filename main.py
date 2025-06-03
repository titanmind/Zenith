#test 2

"""
Zenith – entry point.
"""
import pygame
from core.game import Game
from config import Settings


def main() -> None:
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.window_size)
    pygame.display.set_caption("Zenith")

    game = Game(screen, settings)
    game.run()

    pygame.quit()


if __name__ == "__main__":
    main()
