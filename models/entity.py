class Entity:
    """Base class for anything that can update & serialize."""

    def __init__(self) -> None:
        self.active: bool = True

    def update(self, dt: float) -> None:
        ...

    # ─────── persistence ───────
    def to_dict(self) -> dict:
        return {}

    @classmethod
    def from_dict(cls, data: dict) -> "Entity":
        return cls()
