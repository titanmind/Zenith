from collections import defaultdict
from typing import Callable, Any, Dict, List


class EventBus:
    """Tiny pub/sub hub so systems stay decoupled."""

    def __init__(self) -> None:
        self._subs: Dict[str, List[Callable[[Any], None]]] = defaultdict(list)

    def subscribe(self, event: str, cb: Callable[[Any], None]) -> None:
        self._subs[event].append(cb)

    def emit(self, event: str, payload: Any | None = None) -> None:
        for cb in self._subs.get(event, []):
            cb(payload)
