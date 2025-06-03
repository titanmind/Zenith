from dataclasses import dataclass
from pathlib import Path
from typing import Tuple


@dataclass
class Settings:
    fps: int = 60
    window_size: Tuple[int, int] = (1920, 1080)
    asset_dir: Path = Path(__file__).parent / "assets"
    save_dir: Path = Path.home() / ".zenith_saves"
    debug: bool = True
