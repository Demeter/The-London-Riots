from londonriots.scripts import environment
import sys
import londonriots.models as models
import londonriots.feeds.currency as currency
import transaction
import time
from BeautifulSoup import BeautifulSoup
import nltk

def main():
    with environment(sys.argv) as env:
        article = BeautifulSoup(models.DBSession.query(models.Article).first().source_text)
        text = u"".join(p.text for p in article.findAll("p"))
        print [(w,p) for w,p in nltk.pos_tag(nltk.word_tokenize(text)) if w[0].isalpha() and (p[0] in "NV") and (not any(c.isupper() for c in w[1:]))]
