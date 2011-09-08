from londonriots.tests import TestLR
from datetime import datetime as dt

import londonriots.feeds.currency as currency
from londonriots.models import root, CurrencyPair
from pkg_resources import resource_string
page_body = resource_string(__name__, "GBPUSD.html")
TEST_FEED_URL = "http://news.google.com/news?hl=en&gl=us&q=usd+aud&um=1&ie=UTF-8&output=rss"

class TestCurrency(TestLR):
    currency_pair = ("GBP", "USD")

    def setUp(self):
        TestLR.setUp(self)
        source, target = self.currency_pair
        currency_pair = CurrencyPair(source, target, TEST_FEED_URL)
        self.tradeprice = currency.PriceFromYahooPage(currency_pair, page_body)

    def test_currency(self):
        self.assert_(self.tradeprice.effective_date < dt.now())
