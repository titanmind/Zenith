import pygame
from views.base_view import BaseView


class MenuView(BaseView):
    """ESC overlay menus."""

    def render(self) -> None:
        self.screen.fill("dimgray")
