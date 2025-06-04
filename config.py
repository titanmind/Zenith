from dataclasses import dataclass
from pathlib import Path
from typing import Tuple


# color palette -------------------------------------------------------------
# Basic grayscale for UI elements
UI_DARK: tuple[int, int, int] = (30, 30, 30)
UI_GREY: tuple[int, int, int] = (60, 60, 60)
UI_LIGHT: tuple[int, int, int] = (200, 200, 200)

# Possible stellar colors (placeholder values for now)
STAR_COLORS: list[tuple[int, int, int]] = [
    (255, 255, 255),  # white
    (255, 240, 200),  # yellowish
    (255, 180, 180),  # redish
    (180, 200, 255),  # blueish
]


@dataclass
class Settings:
    fps: int = 60
    window_size: Tuple[int, int] = (1920, 1080)
    asset_dir: Path = Path(__file__).parent / "assets"
    save_dir: Path = Path.home() / ".zenith_saves"
    debug: bool = True
    seed: int = 42
