from __future__ import annotations
import math


class Vec2:
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.x, self.y = x, y

    # basic ops
    def __add__(self, other: "Vec2") -> "Vec2":
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vec2") -> "Vec2":
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, k: float) -> "Vec2":
        return Vec2(self.x * k, self.y * k)

    # helpers
    def length(self) -> float:
        return math.hypot(self.x, self.y)

    def normalized(self) -> "Vec2":
        l = self.length() or 1.0
        return Vec2(self.x / l, self.y / l)
