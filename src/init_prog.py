from simplify.stem import *
from simplify.lemmatizing import *
from simplify.punctuation import *
from src.simplify.stopwords import *

sample_sentence = "hello, how are you doing after vaccine dose?"
# sample_sentence = None
stemmed_sentence = porter_stemmer(sample_sentence)
print("Porter stemmer: ", stemmed_sentence)
#
#
stemmed_sentence = lancaster_stemmer(sample_sentence)
print("Lancaster stemmer: ", stemmed_sentence)
#
stemmed_sentence = snowball_stemmer(sample_sentence)
print("Snowball stemmer: ", stemmed_sentence)


lemm_sentence = wordnet_lemmatizer(sample_sentence)
print("WordNet lemmatizer: ", lemm_sentence)
#
lemm_sentence = spacy_lemmatizer(sample_sentence)
print("Spacy lemmatizer: ", lemm_sentence)

sentence_after = remove_punctuation(sample_sentence, '?')
# sentence_after = remove_punctuation(sample_sentence)
print("Punctuation removal: ", sentence_after)

# removed_stop_words = remove_stopwords(sample_sentence, skip_words='you')
removed_stop_words = remove_stopwords(sample_sentence, skip_words=None)
print("Stop words removal: ", removed_stop_words)