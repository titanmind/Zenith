import pygame
from views.base_view import BaseView


class SurfaceView(BaseView):
    """Cylindrical planet‑surface renderer."""

    def render(self) -> None:
        self.screen.fill("sienna")
