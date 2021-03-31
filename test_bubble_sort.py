import unittest

# Наш объект тестирования.
from bubble_sort import bubble_sort


class BubbleSortTest(unittest.TestCase):

    def test_integer(self):

        result = bubble_sort([7, 3, 5, 9])

        self.assertEqual(
            [3, 5, 7, 9],
            result
        )

    def test_float(self):

        result = bubble_sort([1.2, 7.7, 10.5, -3.2])

        self.assertEqual(
            [-3.2, 1.2, 7.7, 10.5],
            result
        )

    def test_str(self):

        result = bubble_sort([
            "banana",
            "apple",
            "orange",
            "картошечка",
            "111"
        ])

        self.assertEqual(
            [
                "111",
                "apple",
                "banana",
                "orange",
                "картошечка",
            ],
            result
        )

    def test_кидает_исключение_на_несовместимых_типах(self):
        with self.assertRaises(TypeError):
            bubble_sort([1, 'a', None])
