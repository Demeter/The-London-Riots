import unittest

from pyramid import testing
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
import londonriots.models as models

def _initTestingDB():
    session = models.initialize_sql(create_engine('sqlite://'))
    try:
        populate(session)
    except IntegrityError:
        transaction.abort()

    return session

def populate(session):
    session.add(models.CurrencyPair(source=u'GBP', target="AUD"))

class TestLRRoot(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.session = _initTestingDB()

    def tearDown(self):
        testing.tearDown()
        self.session.remove()

    @property
    def root(self):
        return models.LRRoot()

    def test___getitem__hit(self):
        root = self.root
        first = root[("GBP", "AUD")]

    def test___getitem__miss(self):
        root = self.root
        self.assertRaises(KeyError, root.__getitem__, ("USD", "JPY"))

    def test___iter__(self):
        root = self.root
        iterable = iter(root)
        result = list(iterable)
        self.assertEqual(len(result), 1)
        model = result[0]
        self.assertEqual(model.id, 1)
