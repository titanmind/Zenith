import pygame
from views.base_view import BaseView


class FlightView(BaseView):
    """Top‑down space‑flight renderer."""

    def render(self) -> None:
        self.screen.fill("black")
