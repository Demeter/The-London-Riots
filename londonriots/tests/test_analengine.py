from londonriots.tests import TestLR
import datetime as dt
import londonriots.analengine.epsilon as anal
from londonriots.models import root

class TestAnalEngine(TestLR):
    def setUp(self):
        TestLR.setUp(self)
        self.currency_pair = root[("GBP", "USD")]
        self.article_start_time = dt.datetime(2011, 9, 9, 11)
        self.article_epsilon = dt.timedelta(hours=5)
        self.named_entities = anal.named_entities_in_time_range(self.currency_pair, self.article_start_time, self.article_epsilon)

        self.currency_price_at_time = self.article_start_time + self.article_epsilon + dt.timedelta(minutes=5)
        self.currency_price = anal.currency_price_at_time(self.currency_pair, self.currency_price_at_time)

        self.data_point = anal.data_point(self.currency_pair, self.article_start_time + self.article_epsilon, self.article_epsilon, dt.timedelta(minutes=5))

    def test_analengine_named_entities(self):
        self.assert_(self.named_entities.count() > 0)

    def test_analengine_currency_price_after_time(self):
        self.assert_(self.currency_price > 0)

    def test_analengine_has_no_prices(self):
        self.assertRaises(KeyError, lambda: anal.currency_price_at_time(self.currency_pair, dt.datetime(2001, 9, 9)))

    def test_analengine_data_point(self):
        ne,p = self.data_point
        self.assert_(len(ne) != 0)
