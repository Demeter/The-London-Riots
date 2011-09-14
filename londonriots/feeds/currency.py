"""Extracts the current currency rate from a Yahoo Finance page."""

import requests
import BeautifulSoup as bs
from decimal import Decimal
from datetime import datetime
from londonriots.models import TradeRate, Article, DBSession
import feedparser
import pprint
from sqlalchemy.orm.exc import NoResultFound


def extract_sibling(table_headers, tag):
    try:
        return ((th for th in table_headers
                 if th.text.startswith(unicode(tag)))
                .next()
                .nextSibling()[-1].text)
    except StopIteration:
        raise KeyError(tag)

url_template = "http://finance.yahoo.com/q?s=%(source)s%(target)s=X"
time_format = "%a, %d %b %Y %H:%M:%S %Z"

def CurrencyPriceYahoo(currency_pair):
        page = requests.get(url_template %{"source": currency_pair.source,
                                                "target": currency_pair.target})
        return PriceFromYahooPage(currency_pair, page.content)

def PriceFromYahooPage(currency_pair, page):
        dom = bs.BeautifulSoup(page)
        thh = dom.findAll("th")

        price = Decimal(extract_sibling(thh, "Last Trade"))
        date = datetime.now()
        return TradeRate(currency_pair, date, price)

def FetchArticles(currency_pair):
    url = currency_pair.article_feed
    articles = feedparser.parse(url)
    for entry in articles['entries']:
        link = entry['link']
        try:
            article = DBSession.query(Article).filter(
                    (Article.url==link)).one()
            continue
        except NoResultFound:
            pass
        body = requests.get(link).content.decode("utf-8", "replace")
        effective_date = datetime(*entry.updated_parsed[:6])
        yield Article(currency_pair, entry['link'], effective_date, body)
