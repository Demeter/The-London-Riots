import londonriots.models as models
from BeautifulSoup import BeautifulStoneSoup
import nltk
import itertools as it
from sqlalchemy.orm.exc import NoResultFound
import htmllib

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

def extract_named_entities(article):
    article_text = BeautifulStoneSoup(article.source_text, convertEntities=BeautifulStoneSoup.HTML_ENTITIES)
    try:
        h = it.chain(article_text.findAll("h1"), article_text.findAll("h2"), article_text.findAll("h3"), article_text.findAll("h4")).next()
    except StopIteration:
        return
    text = u" ".join(p.text for p in h.findAllNext("p"))
    sentences =  nltk.sent_tokenize(text)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    tagged_sentences = [nltk.pos_tag(sent) for sent in sentences]
    tagged_sentences = [nltk.ne_chunk(sent, binary=True) for sent in tagged_sentences]
    for sent in tagged_sentences:
        for pos in sent:
            if isinstance(pos, tuple): continue
            yield u" ".join((w for (w,p) in pos))
