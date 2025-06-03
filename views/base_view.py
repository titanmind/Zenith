# views/base_view.py (implicit – imported by concrete views if desired)
import pygame


class BaseView:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen

    def render(self) -> None:
        ...
