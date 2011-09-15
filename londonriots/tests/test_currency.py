import itertools as it
from londonriots.tests import TestLR
from datetime import datetime as dt

import londonriots.feeds.currency as currency
from londonriots.models import root, CurrencyPair
from pkg_resources import resource_string
page_body = resource_string(__name__, "GBPUSD.html")

class TestCurrency(TestLR):
    currency_pair_args = ("GBP", "USD")

    def setUp(self):
        TestLR.setUp(self)
        self.currency_pair = root[self.currency_pair_args]
        self.tradeprice = currency.PriceFromYahooPage(self.currency_pair, page_body)

    def test_currency(self):
        self.assert_(self.tradeprice.effective_date < dt.now())
