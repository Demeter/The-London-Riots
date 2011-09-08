import itertools as it
from londonriots.tests import TestLR
from datetime import datetime as dt

import londonriots.feeds.currency as currency
from londonriots.models import root, CurrencyPair
from pkg_resources import resource_string
page_body = resource_string(__name__, "GBPUSD.html")
TEST_FEED_URL = "http://news.google.com/news?hl=en&gl=us&q=usd+aud&um=1&ie=UTF-8&output=rss"

class TestCurrency(TestLR):
    currency_pair_args = ("GBP", "USD", TEST_FEED_URL)

    def setUp(self):
        TestLR.setUp(self)
        self.currency_pair = CurrencyPair(*self.currency_pair_args)
        self.tradeprice = currency.PriceFromYahooPage(self.currency_pair, page_body)

    def test_currency(self):
        self.assert_(self.tradeprice.effective_date < dt.now())

    def test_fetch_articles(self):
        for n, article in it.izip(it.count(), currency.FetchArticles(self.currency_pair)):
            if n > 1:
                break

            self.assertEqual(article.currency_pair, self.currency_pair)
            self.assert_(article.source_text)
