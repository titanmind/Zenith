# services/resource_service.py
import pygame
from pathlib import Path

from config import Settings


class ResourceService:
    """Loads, caches, and returns image (and later sound) assets.

    During early prototyping, if a requested image is missing on disk
    we auto‑fabricate a 32×32 coloured square so the game never crashes.
    """

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.cache: dict[str, pygame.Surface] = {}

    # ------------------------------------------------------------------ #
    def get_image(self, name: str) -> pygame.Surface:
        """
        Return a pygame.Surface, loading & caching it on first access.

        `name` can include sub‑folders, e.g. `"ui/reticle.png"`.
        If the image file is absent, a coloured placeholder surface is
        generated so that rendering code always receives something valid.
        """
        if name in self.cache:
            return self.cache[name]

        path: Path = self.settings.asset_dir / name

        if path.exists():
            surface = pygame.image.load(path.as_posix()).convert_alpha()
        else:
            # ── Procedurally build a simple placeholder ──
            placeholder = pygame.Surface((32, 32), pygame.SRCALPHA)

            # Choose a colour based on the requested basename
            colour_map: dict[str, tuple[int, int, int]] = {
                "star":   (255, 240, 200),   # warm yellow‑white
                "planet": (120, 160, 255),   # cool blue
                "ship":   (200, 200, 200),   # light grey
            }
            colour = colour_map.get(Path(name).stem, (255, 0, 255))  # magenta fallback
            placeholder.fill(colour)

            # Minimal visual cue: draw a black border
            pygame.draw.rect(placeholder, (0, 0, 0), placeholder.get_rect(), 1)
            surface = placeholder

        self.cache[name] = surface
        return surface
