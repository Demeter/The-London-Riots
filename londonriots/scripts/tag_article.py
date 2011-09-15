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

def main():
    with environment(sys.argv) as env:
        for article in models.DBSession.query(models.Article):
            article = models.DBSession.merge(article)
            
            if len(article.entity_frequencies) > 0: continue

            tagged_words.tag_article(article)
            transaction.commit()

