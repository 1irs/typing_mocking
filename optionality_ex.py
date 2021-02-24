from typing import Optional


def f1() -> Optional[int]:
    return 42


def f2() -> int:
    v = f1()
    if v:
        return v * 2
    else:
        return 0
