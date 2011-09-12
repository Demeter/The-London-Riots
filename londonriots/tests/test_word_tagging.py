import itertools as it
from londonriots.tests import TestLR
from datetime import datetime as dt
import londonriots.feeds.tagged_words as tagged_words

import londonriots.feeds.currency as currency
from londonriots.models import root, TaggedWord, WordFrequency, Article, CurrencyPair
from pkg_resources import resource_string
page_body = resource_string(__name__, "sample_article.html").decode("utf-8")
TEST_FEED_URL = "http://news.google.com/news?hl=en&gl=us&q=usd+aud&um=1&ie=UTF-8&output=rss"

class TestWordTagging(TestLR):
    currency_pair_args = ("GBP", "USD", TEST_FEED_URL)

    def setUp(self):
        TestLR.setUp(self)
        self.currency_pair = CurrencyPair(*self.currency_pair_args)
        self.article = Article(self.currency_pair, "/".join((__name__, "sample_artcile.html")), dt.now(), page_body)
        tagged_words.tag_article(self.article)

    def test_word_tagging(self):
        self.assert_(len(self.article.word_frequencies) > 0)
