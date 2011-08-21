"""Manages the feed cache for a feed."""

from feedcache import Cache as fcache
import shelve

CACHE_STORE = ".feedcache"
ARTICLE_STORE = ".articles"

class ArticleCache(object):
    """Downloads and caches articles from a feed."""

    def __init__(self, article_store=ARTICLE_STORE):
        self.article_store_path = article_store

    def fetch_article(self, article_store, link):
        content = requests.get(link).content
        article_store[link] = content
        return content

    def __iter__(self, feed_entries):
        with shelve.open(self.article_store_path) as article_store:

            for entry in feed_entries:
                if entry.link in article_store:
                    continue

                yield self.fetch_article(article_store, entry.link)
