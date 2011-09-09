from londonriots.scripts import environment
import sys
import londonriots.models as models
import londonriots.feeds.currency as currency
import transaction
import time

def main():
    with environment(sys.argv) as env:
        while True:
            fetch()
            time.sleep(30)

def fetch():
    currency_pairs = models.DBSession.query(models.CurrencyPair)
    for currency_pair in currency_pairs:
        price = currency.CurrencyPriceYahoo(currency_pair)
        print currency_pair.source, currency_pair.target, price.rate, price.effective_date
    print
    transaction.commit()
