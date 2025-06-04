"""Simple conditional logger."""
from config import Settings


def log(msg: str, lvl: str = "INFO") -> None:
    """Print message when Settings.debug is True."""
    if Settings.debug:
        print(f"[{lvl}] {msg}")
