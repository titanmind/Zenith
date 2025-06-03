import json
from pathlib import Path
from typing import Any


class SaveLoadMixin:
    """Mixin giving save()/load() helpers."""

    def save_json(self, path: Path) -> None:
        path.write_text(json.dumps(self.to_dict(), indent=2))

    @classmethod
    def load_json(cls, path: Path) -> Any:
        return cls.from_dict(json.loads(path.read_text()))
