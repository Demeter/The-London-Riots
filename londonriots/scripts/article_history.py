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
        currency_pair = models.DBSession.merge(currency_pair)
        articles = currency.FetchArticles(currency_pair)
        for article in articles:
            print article.url, article.effective_date
            models.DBSession.flush()
    transaction.commit()
    print
