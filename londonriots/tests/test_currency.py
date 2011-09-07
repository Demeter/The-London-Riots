from londonriots.tests import TestLR
from datetime import datetime as dt

import londonriots.feeds.currency as currency
from londonriots.models import root, CurrencyPair

class TestCurrency(TestLR):
    currency_pair = ("GBP", "USD")

    def setUp(self):
        TestLR.setUp(self)
        currency_pair = root.get(self.currency_pair, CurrencyPair(*self.currency_pair))
        self.tradeprice = currency.CurrencyPriceYahoo(currency_pair)

    def test_currency(self):
        self.assert_(self.tradeprice.effective_date < dt.now())
