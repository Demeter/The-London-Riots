import itertools as it
from londonriots.tests import TestLR
from datetime import datetime as dt
import londonriots.feeds.tagged_words as tagged_words

import londonriots.feeds.currency as currency
from londonriots.models import root, NamedEntity, NamedEntityFrequency, Article, CurrencyPair
from pkg_resources import resource_string
page_body = resource_string(__name__, "sample_article.html").decode("utf-8")

class TestNamedEntities(TestLR):
    currency_pair_args = ("GBP", "USD")

    def setUp(self):
        TestLR.setUp(self)
        self.currency_pair = root[self.currency_pair_args]
        self.article = Article(self.currency_pair, "/".join((__name__, "sample_artcile.html")), dt.now(), page_body)
        tagged_words.tag_article(self.article)

    def test_word_tagging(self):
        self.assert_(len(self.article.entity_frequencies) > 0)
        for entity_frequency in self.article.entity_frequencies:
            self.assert_(int(entity_frequency.frequency) >= 0)
