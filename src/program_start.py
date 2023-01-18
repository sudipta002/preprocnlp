from simplify.stem import *
from simplify.lemmatizing import *
from simplify.punctuation import *
sentence = "hello, how are you doing after vaccine dose?"

# stemmed_sentence = porter_stemmer(sentence)
# print("Porter stemmer: ",stemmed_sentence)
# #
# #
# stemmed_sentence = lancaster_stemmer(sentence)
# print("Lancaster stemmer: ",stemmed_sentence)
# #
# stemmed_sentence = snowball_stemmer(sentence)
# print("Snowball stemmer: ",stemmed_sentence)
#
#
# lemm_sentence = wordnet_lemmatizer(sentence)
# print("WordNet lemmatizer: ",lemm_sentence)
# #
# lemm_sentence = spacy_lemmatizer(sentence)
# print("Spacy lemmatizer: ",lemm_sentence)

sentence_after = remove_punctuation(sentence, '?')
# sentence_after = remove_punctuation(sentence)
print(sentence_after)