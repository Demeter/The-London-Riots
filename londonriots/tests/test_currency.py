from londonriots.tests import TestLR
from datetime import datetime as dt

import londonriots.feeds.currency as currency
from londonriots.models import root, CurrencyPair
from pkg_resources import resource_string
page_body = resource_string(__name__, "GBPUSD.html")

class TestCurrency(TestLR):
    currency_pair = ("GBP", "USD")

    def setUp(self):
        TestLR.setUp(self)
        currency_pair = root.get(self.currency_pair, CurrencyPair(*self.currency_pair))
        self.tradeprice = currency.PriceFromYahooPage(currency_pair, page_body)

    def test_currency(self):
        self.assert_(self.tradeprice.effective_date < dt.now())
