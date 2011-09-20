from londonriots.scripts import environment
import sys
import londonriots.models as models
import londonriots.feeds.currency as currency
import transaction
import time
import logging
import traceback as tb

log = logging.getLogger(__name__)

def main():
    with environment(sys.argv) as env:
        while True:
            try:
                fetch()
                transaction.commit()
            except:
                transaction.rollback()
                log.error(tb.format_exc())

            models.DBSession.close()
            time.sleep(30)

def fetch():
    currency_pairs = models.DBSession.query(models.CurrencyPair)
    for currency_pair in currency_pairs:
        currency_pair = models.DBSession.merge(currency_pair)
        articles = currency.FetchArticles(currency_pair)
        for article in articles:
            log.info("Fetching article %s, effective %s", 
                     article.url, 
                     article.effective_date)
