from londonriots.scripts import environment
import sys
import londonriots.models as models
import transaction
TEST_FEED_URL = "http://news.google.com/news?hl=en&gl=us&q=usd+aud&um=1&ie=UTF-8&output=rss"
currency_pair_args = ("GBP", "USD", TEST_FEED_URL)

def main():
    with environment(sys.argv) as env:
        print env
        print models.root
        try:
            currency_pair = models.root[(currency_pair_args[0], currency_pair_args[1])]
        except KeyError:
            currency_pair = models.CurrencyPair(*currency_pair_args)
            models.DBSession.add(currency_pair)
            print "Created."

        transaction.commit()
        print currency_pair
