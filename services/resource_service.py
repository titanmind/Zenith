import pygame
from pathlib import Path
from config import Settings


class ResourceService:
    """Loads, caches, and returns image (and later sound) assets."""

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.cache: dict[str, pygame.Surface] = {}

    # ────────────────────────────────────────────────────────────
    def get_image(self, name: str) -> pygame.Surface:
        """
        Return a Pygame Surface, loading & caching the image on first call.
        `name` can include sub‑folders, e.g. 'ui/reticle.png'.
        """
        if name in self.cache:
            return self.cache[name]

        path: Path = self.settings.asset_dir / name
        if not path.exists():
            raise FileNotFoundError(f"Asset not found: {path}")

        surface = pygame.image.load(path.as_posix()).convert_alpha()
        self.cache[name] = surface
        return surface
