import sys
import unittest

from pyramid import testing
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
import londonriots.models as models
import transaction
from paste.deploy import appconfig
from sqlalchemy import engine_from_config
session = None

import os

def _initTestingDB():
    global session
    if session: return session

    ini_path = os.environ.get("TEST_INI", 'development.ini')

    conf = appconfig('config:' + ini_path, 
            relative_to=".")

    # Bind Engine Based on Config
    engine = engine_from_config(conf, 'sqlalchemy.')
    session = models.initialize_sql(engine)

    return session

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
