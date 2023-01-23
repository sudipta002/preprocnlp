import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('omw-1.4')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
import spacy
from nltk.tokenize import word_tokenize


def text_to_word_token(sentence):
    return word_tokenize(sentence)


def word_lem(token_words, lemmat):
    lemm_sentence = ' '.join([lemmat.lemmatize(w) for w in token_words])
    return lemm_sentence


def wordnet_lemmatizer(sentence):
    """
    It applies wordnet lemmatizer on text.
    :param sentence: text
    :return: text
    """
    assert type(sentence) is not None
    lemmatizer = WordNetLemmatizer()
    token_words = text_to_word_token(sentence)
    lemm_sentence = word_lem(token_words, lemmatizer)
    return lemm_sentence


def spacy_lemmatizer(sentence):
    """
    It applies spacy temmatizer on text.
    :param sentence: text
    :return: text
    """
    try:
        nlp = spacy.load('en_core_web_sm')
    except:
        raise
    doc = nlp(sentence)
    token_words = [token for token in doc]
    lemm_sentence = " ".join([token.lemma_ for token in token_words])
    return lemm_sentence
