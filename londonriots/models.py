import transaction

from sqlalchemy.orm import *

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from sqlalchemy import *

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class CurrencyPair(Base):
    __tablename__ = 'currencypair'
    __table_args__ = (UniqueConstraint("source", "target", name="unique_source_target"),)

    id = Column(Integer, primary_key=True)

    source = Column(Unicode(), nullable=False)
    target = Column(Unicode(), nullable=False)
    article_feed = Column(Unicode(), nullable=False)

    trade_rates = relationship("TradeRate", backref="currency_pair")
    article = relationship("Article", backref="currency_pair")

    def __init__(self, source, target, article_feed):
        self.source = unicode(source)
        self.target = unicode(target)
        self.article_feed = unicode(article_feed)

class TradeRate(Base):
    __tablename__ = "traderate"

    id = Column(Integer, primary_key=True)
    currency_pair_id = Column(Integer, ForeignKey("currencypair.id"), nullable=False)

    effective_date = Column(DateTime, nullable=False)
    rate = Column(Numeric(precision=15, scale=6), nullable=False)

    def __init__(self, currency_pair, effective_date, rate):
        self.currency_pair = currency_pair
        self.effective_date = effective_date
        self.rate = rate

class Article(Base):
    __tablename__ = "article"

    entity_frequencies = relationship("NamedEntityFrequency", backref="article")

    id = Column(Integer, primary_key=True)
    currency_pair_id = Column(Integer, ForeignKey("currencypair.id"), nullable=False)

    url = Column(Unicode(), nullable=False, unique=True)
    effective_date = Column(DateTime, nullable=False)
    source_text = Column(Text(), nullable=False)

    def __init__(self, currency_pair, url, effective_date, source_text):
        self.currency_pair = currency_pair
        self.url = unicode(url)
        self.effective_date = effective_date
        self.source_text = unicode(source_text)

class NamedEntity(Base):
    __tablename__ = "namedentity"

    id = Column(Integer, primary_key=True)

    text = Column(Unicode(), nullable=False, unique=True)

    def __init__(self, text):
        self.text = unicode(text)

class NamedEntityFrequency(Base):
    __tablename__ = "namedentityfrequency"

    entity = relationship("NamedEntity", backref="frequency")

    id = Column(Integer, primary_key=True)

    entity_id = Column(Integer, ForeignKey("namedentity.id"), nullable=False)
    article_id = Column(Integer, ForeignKey("article.id"), nullable=False)
    frequency = Column(Integer, nullable=False)

    def __init__(self, article, entity, frequency):
        self.article = article
        self.entity = entity
        self.frequency = frequency

class LRRoot(object):
    __name__ = None
    __parent__ = None

    def __getitem__(self, (source, target)):
        source, target = unicode(source), unicode(target)
        session = DBSession()

        try:
            item = session.query(CurrencyPair).filter(
                (CurrencyPair.source==source) & 
                (CurrencyPair.target==target)).one()

        except NoResultFound:
            raise KeyError((source, target))

        item.__parent__ = self
        item.__name__ = (source, target)
        return item

    def __iter__(self):
        session= DBSession()
        query = session.query(CurrencyPair)
        return iter(query)

root = LRRoot()

def root_factory(request):
    return root

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

    return DBSession

def appmaker(engine):
    initialize_sql(engine)
    return root_factory
