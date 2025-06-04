from dataclasses import dataclass


@dataclass
class Star:
    """Simple stellar data container."""

    spectral_class: str
    luminosity: float
    radius_km: float
    color: tuple[int, int, int]
