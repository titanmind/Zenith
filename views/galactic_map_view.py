import pygame
from views.base_view import BaseView


class GalacticMapView(BaseView):
    """Pan/zoom galaxy map."""

    def render(self) -> None:
        self.screen.fill("midnightblue")
