import pygame


class HUD:
    """Draws common overlays (health bars, reticle, etc.)."""

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen

    def render(self) -> None:
        ...
