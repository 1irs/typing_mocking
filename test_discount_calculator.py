import unittest
import datetime
from freezegun import freeze_time

from discount_calculator import discount_calculator


class DiscountCalculatorTest(unittest.TestCase):

    @freeze_time("2020-04-26")
    def test_discount(self):
        self.assertEqual(
            80.0,
            discount_calculator(
                value=100,
                due_date=datetime.date(year=2020, month=4, day=28),
                days=3,
                discount=0.2
            )
        )

    @freeze_time("2020-04-28")
    def test_discount_yes(self):
        self.assertEqual(
            80.0,
            discount_calculator(
                value=100,
                due_date=datetime.date(year=2020, month=4, day=28),
                days=3,
                discount=0.2
            )
        )

    @freeze_time("2020-04-25")
    def test_no_discount_1(self):
        self.assertEqual(
            100.0,
            discount_calculator(
                value=100,
                due_date=datetime.date(year=2020, month=4, day=28),
                days=3,
                discount=0.2
            )
        )

    @freeze_time("2020-04-29")
    def test_no_discount_2(self):
        self.assertEqual(
            100.0,
            discount_calculator(
                value=100,
                due_date=datetime.date(year=2020, month=4, day=28),
                days=3,
                discount=0.2
            )
        )
