from londonriots.models import Article, DBSession, NamedEntity, NamedEntityFrequency, TradeRate
import datetime as dt

def named_entities_in_time_range(currency_pair, start_time, epsilon):
    articles = DBSession.query(NamedEntity).join(NamedEntityFrequency).join(Article).filter(
            (Article.effective_date >= start_time) &
            (Article.effective_date <= start_time + epsilon) &
            (Article.currency_pair == currency_pair) &
            (NamedEntityFrequency.frequency > 1))
    return articles

def currency_price_at_time(currency_pair, time):
    rates = DBSession.query(TradeRate).filter(
            (TradeRate.effective_date >= time - dt.timedelta(seconds=60)) &
            (TradeRate.effective_date <= time + dt.timedelta(seconds=60)) &
            (TradeRate.currency_pair == currency_pair))
    n = rates.count()
    if n == 0: raise KeyError("No trade information available for that time.")

    rate = sum(r.rate for r in rates)/n
    return rate
