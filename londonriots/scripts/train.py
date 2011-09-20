import math
from londonriots.analengine.epsilon import *
from londonriots.models import CurrencyPair, root, DBSession

from londonriots.tests import TestLR
import datetime as dt
from pprint import pprint as pp
import londonriots.analengine.epsilon as anal
from londonriots.models import DBSession, Article, CurrencyPair
from londonriots.scripts import environment
import sys

def main():
    with environment(sys.argv) as env:
        for currency_pair in DBSession.query(CurrencyPair):
            print currency_pair.source, currency_pair.target
            with open("%s-%s.txt" % (currency_pair.source, currency_pair.target), "w") as outfile:
                currency_pair_stats(outfile, currency_pair)

def currency_pair_stats(outfile, currency_pair):
    old_nes = set()
    for article in DBSession.query(Article).filter(Article.currency_pair == currency_pair):
        try:
            ne, dp = data_point_for_article(article, dt.timedelta(minutes=5))

            ne = tuple(sorted(id for id, name in ne))
            if ne in old_nes:
                continue
            old_nes.add(ne) 
            outfile.write("%s %s\n" % (dp, " ".join(("%d:1" % id for id in ne))))

        except KeyError:
            pass


def data_point_for_article(article, price_epsilon):
    article_start_time = article.effective_date
    currency_pair = article.currency_pair
    article_epsilon = dt.timedelta(hours=1)
    data_point = anal.data_point(currency_pair, article_start_time + article_epsilon, article_epsilon, price_epsilon)
    return data_point
