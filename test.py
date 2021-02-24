from unittest import TestCase

from quick_sort import quickSort


class Test(TestCase):

    def test(self) -> None:

        self.assertEqual(
            [1,2,3,4,5],
            quickSort([1,4,3,2,5])
        )
