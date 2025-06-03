import pygame
from pygame.locals import KEYDOWN, KEYUP


class InputManager:
    """
    Tracks key/mouse state. Controllers can poll:
        if input_mgr.key_state.get(pygame.K_w): ...
    """

    def __init__(self) -> None:
        self.key_state: dict[int, bool] = {}

    # ────────────────────────────────────────────────────────────
    def process_event(self, event: pygame.event.Event) -> None:
        if event.type == KEYDOWN:
            self.key_state[event.key] = True
        elif event.type == KEYUP:
            self.key_state[event.key] = False
