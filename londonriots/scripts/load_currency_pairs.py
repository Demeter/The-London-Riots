from londonriots.scripts import environment
import sys
import londonriots.models as models
import transaction
TEST_FEED_URL = "http://news.google.com/news?hl=en&gl=us&q=%(source)s+%(target)s&um=1&ie=UTF-8&output=rss"
currency_pair_args = (("GBP", "USD"), ("EUR", "USD"), ("GBP", "JPY"), ("USD", "JPY"), ("AUD", "USD"))

def main():
    with environment(sys.argv) as env:
        for source, target in currency_pair_args:
            try:
                currency_pair = models.root[source, target]
                print "Found", source, target
            except KeyError:
                currency_pair = models.CurrencyPair(source, target, TEST_FEED_URL % {"source": source, "target": target})
                models.DBSession.add(currency_pair)
                print "Created", source, target

        transaction.commit()
