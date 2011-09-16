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
            currency_pair_stats(currency_pair)
            print

def currency_pair_stats(currency_pair):
    count = 0
    total = 0
    s_dp = 0
    s_dp2 = 0
    for article in DBSession.query(Article).filter(
            Article.currency_pair == currency_pair):
        try:
            ne, dp = data_point_for_article(article, dt.timedelta(minutes=5))

            print dp, sorted(ne, key=lambda n: n.id)
        except KeyError:
            pass


def data_point_for_article(article, price_epsilon):
    article_start_time = article.effective_date
    currency_pair = article.currency_pair
    article_epsilon = dt.timedelta(hours=2)
    data_point = anal.data_point(currency_pair, article_start_time + article_epsilon, article_epsilon, price_epsilon)
    return data_point
