from londonriots.models import Article, DBSession, NamedEntity, NamedEntityFrequency

def named_entities_in_time_range(start_time, epsilon):
    articles = DBSession.query(NamedEntity).join(NamedEntityFrequency).join(Article).filter(
            (Article.effective_date >= start_time) &
            (Article.effective_date <= start_time + epsilon) &
            (NamedEntityFrequency.frequency > 1))
    return articles
