from londonriots.models import Article, DBSession

def articles_in_time_range(start_time, epsilon):
    articles = DBSession.query(Article).filter(
            (Article.effective_date >= start_time) &
            (Article.effective_date <= start_time + epsilon))
    return articles
