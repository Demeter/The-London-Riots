"""Extracts the current currency rate from a Yahoo Finance page."""

import requests
import BeautifulSoup as bs
from decimal import Decimal
from datetime import datetime

def extract_sibling(table_headers, tag):
    return ((th for th in table_headers
             if th.text.startswith(unicode(tag)))
            .next()
            .nextSibling()[-1].text)

class CurrencyPrice(object):
    url_template = "http://finance.yahoo.com/q?s=%(source)s%(target)s=X"
    time_format = "%a, %d %b %Y %H:%M:%S %Z"

    def __init__(self, (source, target)):
        self.source, self.target = source, target

        self.fetch()

    def fetch(self):
        page = requests.get(self.url_template %{"source": self.source,
                                                "target": self.target})

        dom = bs.BeautifulSoup(page.content)

        thh = dom.findAll("th")

        self.price = Decimal(extract_sibling(thh, "Last Trade"))
        self.date = datetime.strptime(page.headers["date"], self.time_format)
