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
from html2text import html2text

def main():
    with environment(sys.argv) as env:
        for article in models.DBSession.query(models.Article)[:10]:
            print article.url
            print html2text(article.source_text.encode("iso-8859-1"))
            #pp.pprint(tagged_words.extract_text(article))
            print "="*90
            #tagged_words.tag_article(article)
        #transaction.commit()
