import unittest
from datetime import datetime as dt

import londonriots.extraction.currency as currency

class TestCurrency(unittest.TestCase):
    currency_pair = ("GBP", "USD")

    def setUp(self):
        self.currency = currency.CurrencyPrice(self.currency_pair)

    def test_currency(self):
        self.assert_(self.currency.date < dt.now())
