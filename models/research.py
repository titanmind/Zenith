class ResearchTree:
    """Handles unlock progression."""

    def __init__(self) -> None:
        self.completed: set[str] = set()

    def queue_item(self, item: str) -> None:
        ...

    def update(self, dt: float) -> None:
        ...
