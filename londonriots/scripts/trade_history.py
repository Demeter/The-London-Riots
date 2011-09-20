from londonriots.scripts import environment
import sys
import londonriots.models as models
import londonriots.feeds.currency as currency
import transaction
import time
import logging

log = logging.getLogger(__name__)

def main():
    with environment(sys.argv) as env:
        while True:
            start_time = time.time()

            try:
                fetch()
                transaction.commit()
            except:
                transaction.abort()
                log.error(tb.format_exc())

            models.DBSession.close()

            time_delta = time.time() - start_time
            time.sleep(30 - time_delta)

def fetch():
    currency_pairs = models.DBSession.query(models.CurrencyPair)
    for currency_pair in currency_pairs:
        price = currency.CurrencyPriceYahoo(currency_pair)
        log.info("Fetched %s -> %s: %s at %s",
                 currency_pair.source,
                 currency_pair.target, 
                 price.rate, 
                 price.effective_date)

