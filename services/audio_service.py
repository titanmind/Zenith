class AudioService:
    """Thin wrapper around pygame.mixer."""

    def __init__(self) -> None:
        ...

    def play_music(self, track: str) -> None:
        ...

    def play_sfx(self, name: str) -> None:
        ...
