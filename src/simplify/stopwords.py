from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def remove_stopwords(sentence, skip_words=None):
    """
    This function removes all stopwords from the text. But if you want to retain special stop words in
    the text, please pass them through skip_punc argument.
    :param sentence: text
    :param skip_words: text.
    :return: text
    """
    stop_words = stopwords.words('english')
    word_tokens = word_tokenize(sentence)
    if skip_words is not None:
        refined_stop_words = list(set(stop_words) - set([skip_words]))
        result = ' '.join([word for word in word_tokens if word not in refined_stop_words])
        return result
    else:
        result = ' '.join([word for word in word_tokens if word not in stop_words])
        return result
