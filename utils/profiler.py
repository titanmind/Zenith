import time
from contextlib import contextmanager


@contextmanager
def profile(section: str):
    t0 = time.perf_counter()
    yield
    ms = (time.perf_counter() - t0) * 1000
    print(f"[PROFILE] {section}: {ms:.2f} ms")
