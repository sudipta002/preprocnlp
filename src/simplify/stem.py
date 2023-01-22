import nltk
from nltk import PorterStemmer
from nltk import LancasterStemmer
from nltk import SnowballStemmer

from nltk.tokenize import word_tokenize


def text_to_word_token(sentence):
    return word_tokenize(sentence)


def word_stemmer(token_words, stemmer):
    stem_sentence = ' '.join([stemmer.stem(w) for w in token_words])
    return stem_sentence


def porter_stemmer(sentence):
    """
    It applies porter stemmer on text.
    :param sentence: text
    :return: text
    """
    stemmer = PorterStemmer()
    token_words = text_to_word_token(sentence)
    stemmed_sentence = word_stemmer(token_words, stemmer)
    return stemmed_sentence


def lancaster_stemmer(sentence):
    """
    It applies lancaster stemmer on text.
    :param sentence: text
    :return: text
    """
    stemmer = LancasterStemmer()
    token_words = text_to_word_token(sentence)
    stemmed_sentence = word_stemmer(token_words, stemmer)
    return stemmed_sentence


def snowball_stemmer(sentence):
    """
    It applies snowball stemmer on text.
    :param sentence: text
    :return: text
    """
    stemmer = SnowballStemmer(language='english')
    token_words = text_to_word_token(sentence)
    stemmed_sentence = word_stemmer(token_words, stemmer)
    return stemmed_sentence
