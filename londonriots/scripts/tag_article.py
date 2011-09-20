from londonriots.scripts import environment
import sys
import londonriots.models as models
import londonriots.feeds.currency as currency
import transaction
import time
from BeautifulSoup import BeautifulSoup
import nltk
import londonriots.feeds.tagged_words as tagged_words
import pprint as pp
import logging
import traceback as tb

log = logging.getLogger(__name__)

def main():
    with environment(sys.argv) as env:
        while True:
            log.info("Begin tagging")
            try:
                tag_articles()
                transaction.commit()
            except:
                log.error(tb.format_exc())
                transaction.abort()

            models.DBSession.close()
            log.info("End tagging")

            time.sleep(30)

def tag_articles():
    for article in models.DBSession.query(models.Article):
        if not len(article.entity_frequencies):
            log.info("Tagging article %s", article.url)
            tagged_words.tag_article(article)
            models.DBSession.flush()
        models.DBSession.expunge(article)
