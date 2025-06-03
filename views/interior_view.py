import pygame
from views.base_view import BaseView


class InteriorView(BaseView):
    """Side‑scroll interior renderer."""

    def render(self) -> None:
        self.screen.fill("darkslategray")
