import londonriots.models as models
from BeautifulSoup import BeautifulSoup
import nltk
import itertools as it
from sqlalchemy.orm.exc import NoResultFound

def tag_article(article):
    for word_frequency in article.word_frequencies:
        models.DBSession.delete(word_frequency)
    tagged_words = extract_text(article)
    for (word, pos), v in it.groupby(sorted(tagged_words)):
        try:
            tagged_word =  models.DBSession.query(models.TaggedWord).filter(
                    (models.TaggedWord.word == word) &
                    (models.TaggedWord.pos == pos)).one()
        except NoResultFound:
            tagged_word = models.TaggedWord(word, pos)
        models.WordFrequency(article, tagged_word, len(list(v)))

def extract_text(article):
    article_text = BeautifulSoup(article.source_text)
    try:
        h = it.chain(article_text.findAll("h1"), article_text.findAll("h2"), article_text.findAll("h3"), article_text.findAll("h4")).next()
    except StopIteration:
        return []
    text = u" ".join(p.text for p in h.findAllNext("p"))
    word_tokenize = nltk.word_tokenize(text)
    tagged_words = [(w,unicode(p)) for w,p in nltk.pos_tag(word_tokenize)]
    return tagged_words
