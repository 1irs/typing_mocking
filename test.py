from unittest import TestCase, expectedFailure

from quick_sort import quickSort


class Test(TestCase):

    def test(self) -> None:

        self.assertEqual(
            [1,2,3,4,5],
            quickSort([1,4,3,2,5])
        )

    @expectedFailure
    def test_almost_equal_expected(self):
        self.assertAlmostEqual(3.14, 3.145, places=4)

    def test_almost_equal_unexpected(self):
        self.assertAlmostEqual(3.14, 3.145, places=2)
