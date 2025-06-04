from dataclasses import dataclass
from typing import Tuple


@dataclass
class Star:
    spectral_class: str            # e.g. "G"
    luminosity: float              # relative to Sun
    radius_km: float               # physical radius
    color: Tuple[int, int, int]    # RGB for rendering
