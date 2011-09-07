import unittest

from pyramid import testing
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
import londonriots.models as models
import transaction

def _initTestingDB():
    session = models.initialize_sql(create_engine('sqlite://'))

    try:
        populate(session)
    except IntegrityError:
        transaction.abort()

    return session

def populate(session):
    session.add(models.CurrencyPair(source=u'GBP', target="AUD"))

class TestLR(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.session = _initTestingDB()

    def tearDown(self):
        testing.tearDown()
        transaction.abort()
        self.session.remove()

    @property
    def root(self):
        return models.LRRoot()
