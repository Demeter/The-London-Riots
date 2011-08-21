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

    def test_feed_cache(self):
        feed_cache = fcache.FeedCache(TEST_FEED_URL)
        entries = list(feed_cache())
        self.assert_(len(entries) > 0)
