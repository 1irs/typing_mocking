from math import sqrt
from typing import Tuple, Optional


def find_square_roots(a: float, b: float, c: float) -> Tuple[Optional[float], Optional[float]]:

    d = b * b - 4 * a * c

    if d < 0:
        return None, None

    x1 = (-b - sqrt(d))/ (2 * a)

    if d == 0:
        x2 = None
    else:
        x2 = (-b + sqrt(d))/ (2 * a)

    return x1, x2
