from cpi_inflation import add_inflation_single
from cpi_inflation.za import CPI_INFLATION
from unittest import TestCase
from datetime import date, datetime, timedelta


class TestCalculations(TestCase):

    def setUp(self) -> None:
        self.simple_map = {
            '2020-01-01': 2,
            '2019-12-01': 1
        }

    def test_add_inflation_for_one_year(self):
        amount = 100
        dt = date(year=2019, month=12, day=1)
        expected = 200
        to = date(year=2020, month=1, day=1)
        adjusted = add_inflation_single(self.simple_map, amount, dt, to)
        self.assertEqual(adjusted, expected)

    def test_discount_for_one_year(self):
        discount_rate = 1.1
        amount = 100
        dt = date(year=2019, month=12, day=1)
        expected = amount / discount_rate
        to = date(year=2018, month=1, day=1)
        adjusted = add_inflation_single(self.simple_map, amount, dt, to, discount_rate)
        self.assertEqual(adjusted, expected)


class TestZAInflation(TestCase):

    def test_simple_inflation_calculation(self):
        a = 100_000
        d = date(year=1990, month=1, day=1)
        val = add_inflation_single(CPI_INFLATION, a, d)
        self.assertEqual(int(val), 711320)

    def test_discounting(self):
        a = 100_000

        # one year
        d = datetime.now().date() + timedelta(weeks=70)  # more than one full year in future
        v = add_inflation_single(CPI_INFLATION, a, d)
        self.assertEqual(int(v), 94_339)

        # two years
        d = datetime.now().date() + timedelta(weeks=130)  # more than one full year in future
        v = add_inflation_single(CPI_INFLATION, a, d)
        self.assertEqual(int(v), 88_999)