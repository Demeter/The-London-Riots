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

    def fetch_article(self, article_store, entry):
        article = Article(entry)
        article_store[entry.link.encode("utf8")] = article
        return article

    def __call__(self, feed):
        with closing(shelve.open(self.article_store_path)) as article_store:
            for entry in feed.entries:
                if entry.link.encode("utf8") in article_store:
                    continue

                yield self.fetch_article(article_store, entry)

class FeedCache(object):
    def __init__(self, url, cache_store=CACHE_STORE):
        self.url = url
        self.cache_store_path = cache_store

    def __call__(self):
        with closing(shelve.open(self.cache_store_path)) as cache_store:
            return fcache(cache_store).fetch(self.url)
