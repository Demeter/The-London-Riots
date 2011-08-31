"""Tests for the cache.py module."""

import unittest
import os
import os.path as opath
import londonriots.feeds.cache as fcache

TEST_FEED_URL = "http://news.google.com/news?hl=en&gl=us&q=usd+aud&um=1&ie=UTF-8&output=rss"

class TestCache(unittest.TestCase):
    def setUp(self):
        if opath.exists(fcache.ARTICLE_STORE):
            os.unlink(fcache.ARTICLE_STORE)

        if opath.exists(fcache.CACHE_STORE):
            os.unlink(fcache.CACHE_STORE)

        self.feed_cache = fcache.FeedCache(TEST_FEED_URL)
        self.article_cache = fcache.ArticleCache()

    def test_feed_cache(self):
        entries = list(self.feed_cache())
        self.assert_(len(entries) > 0)

    def test_article_cache(self):
        first_batch = list(self.article_cache(self.feed_cache()))
        second_batch = list(self.article_cache(self.feed_cache()))

        self.assertNotEqual(first_batch, second_batch)
