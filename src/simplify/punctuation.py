import re
import string

def remove_punctuation(sentence, skip_punc=None):
    punc = string.punctuation
    list_punc = list(punc)
    if skip_punc is not None:
        list_skip_punc = list(skip_punc)
        refined_list_punc = list(set(list_punc) - set(list_skip_punc))
        result = ''.join([word for word in sentence if word not in refined_list_punc])
        return result
    else:
        result = ''.join([word for word in sentence if word not in list_punc])
        return result