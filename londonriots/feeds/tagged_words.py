import londonriots.models as models
from BeautifulSoup import BeautifulStoneSoup
import nltk
import itertools as it
from sqlalchemy.orm.exc import NoResultFound
import htmllib

def tag_article(article):
    for word_frequency in article.entity_frequencies:
        models.DBSession.delete(word_frequency)
    named_entities = extract_named_entities(article)
    frequencies = []
    for text, matches in it.groupby(sorted(named_entities)):
        try:
            named_entity =  models.DBSession.query(models.NamedEntity).filter(
                    (models.NamedEntity.text == text)).one()
        except NoResultFound:
            named_entity = models.NamedEntity(text)
        frequencies.append(models.NamedEntityFrequency(article, 
                                                       named_entity,
                                                       len(list(matches))))

    return frequencies

def extract_named_entities(article):
    article_text = BeautifulStoneSoup(article.source_text, convertEntities=BeautifulStoneSoup.HTML_ENTITIES)
    try:
        h = it.chain(article_text.findAll("h1"), article_text.findAll("h2"), article_text.findAll("h3"), article_text.findAll("h4")).next()
    except StopIteration:
        return
    text = u" ".join(p.text for p in h.findAllNext("p"))
    sentences =  nltk.sent_tokenize(text)
    tokenized_sentences = [nltk.word_tokenize(sent) for sent in sentences]
    tagged_sentences = [nltk.pos_tag(sent) for sent in tokenized_sentences]
    named_entity_chunks = [nltk.ne_chunk(sent, binary=True) for sent in tagged_sentences]
    for chunk in named_entity_chunks:
        for pos in chunk:
            if isinstance(pos, tuple): continue
            yield u" ".join((w for (w,p) in pos))
