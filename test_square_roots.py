import unittest
from unittest import skip

from find_square_roots import find_square_roots


class SquareRootsTest(unittest.TestCase):

    """
        ax2 + bx + c = 0
        Три коэф: a, b, c
        Решения:
            x1 <> x2
            x1 == x2
            корней нет.

        def find_square_roots(a: float, b: float, c:float) -> Tuple[Optional[float], Optional[float]]:
            pass

    """

    def test_1(self):
        """
            x2 - 4 = 0
            x1 == -2
            x2 == 2
        :return:
        """
        result = find_square_roots(1.0, 0.0, -4)

        self.assertEqual(
            (-2, 2),
            result
        )

    def test_2(self):
        """
                    x2 - 9 = 0
                    x1 == -3
                    x2 == 3
                :return:
                """
        result = find_square_roots(1.0, 0.0, -9)

        self.assertEqual(
            (-3, 3),
            result
        )

    def test_no_roots(self):
        result = find_square_roots(1.0, 1.0, 1.0)
        self.assertEqual(
            (None, None),
            result
        )

    def test_two_roots(self):
        result = find_square_roots(2.0, -4.0, -10.0)
        self.assertEqual(
            (-1.4494897427831779, 3.449489742783178),
            result
        )

    @skip('Код еще не написан')
    def test_one_root(self):
        result = find_square_roots(1.0, -6.0, 9.0)
        self.assertEqual(
            (3, None),
            result
        )

