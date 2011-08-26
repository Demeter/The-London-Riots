"""Manages the feed cache for a feed."""

from feedcache import Cache as fcache
import shelve
from contextlib import closing

CACHE_STORE = ".feedcache"
ARTICLE_STORE = ".articles"

class Article(object):
    """Represents a cached article."""

    def __init__(self, entry):
        self.entry = entry

    def __call__(self):
        self.content = requests.get(self.entry.link).content
        return self

class ArticleCache(object):
    """Downloads and caches articles from a feed."""

    def __init__(self, article_store=ARTICLE_STORE):
        self.article_store_path = article_store

    def __getitem__(self, link):
        item = link.encode("utf8")
        with closing(shelve.open(self.article_store_path)) as store:
            return store[item]

    def __setitem__(self, link, article):
        item = link.encode("utf8")
        with closing(shelve.open(self.article_store_path)) as store:
            store[item] = article

    def __contains__(self, link):
        item = link.encode("utf8")
        with closing(shelve.open(self.article_store_path)) as store:
            return item in store

    def fetch_article(self, entry):

        return article

    def __call__(self, feed):
        for entry in feed.entries:
            if entry.link in self:
                continue

            article = Article(entry)
            self[entry.link] = article

            yield article

class FeedCache(object):
    def __init__(self, url, cache_store=CACHE_STORE):
        self.url = url
        self.cache_store_path = cache_store

    def __call__(self):
        with closing(shelve.open(self.cache_store_path)) as cache_store:
            return fcache(cache_store).fetch(self.url)
