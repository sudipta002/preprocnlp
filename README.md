Text Preprocessing with Python

This repository contains Python code for text preprocessing, including tokenization, stopword removal, and stemming/ lemmatization.

**Dependencies:**

- Python 3.9
- Spacy
- NLTK library

**How to use:**

- Clone or download this repository to your local machine.
- Install the required libraries if you haven't already by running pip install -r requirements.txt.
- Run the init_prog.py file with sample text.

**Example:**

sample_sentence = "hello, how are you doing after vaccine dose?"

- Porter stemmer:  hello , how are you do after vaccin dose ?
- Lancaster stemmer:  hello , how ar you doing aft vaccin dos ?
- Snowball stemmer:  hello , how are you do after vaccin dose ?
- WordNet lemmatizer:  hello , how are you doing after vaccine dose ?
- Spacy lemmatizer:  hello , how be you do after vaccine dose ?
- Punctuation removal:  hello how are you doing after vaccine dose?
- Stop words removal:  hello , vaccine dose ?

Enjoy preprocessing your text data with Python!