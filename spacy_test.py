# import spacy
# nlp = spacy.load('en')
#
# doc = str(open('test_doc.txt').read())
# doc = nlp(doc)
#
# print(dir(doc))

from spacy.en import English

from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS as stopwords  # noqa: E501
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

import string
punctuations = string.punctuation


parser = English()


# Custom transformer using spaCy
class predictors(TransformerMixin):
    def transform(self, X, **transform_params):
        return [clean_text(text) for text in X]

    def fit(self, X, y=None, **fit_params):
        return self

    def get_params(self, deep=True):
        return {}


# Basic utility function to clean the text
def clean_text(text):
    return text.strip().lower()


# Create spacy tokenizer that parses a sentence and generates tokens
# these can also be replaced by word vectors
def spacy_tokenizer(sentence):
    tokens = parser(sentence)

    tokens = [tok.lemma_.lower().strip() if tok.lemma_ != "-PRON-" else tok.lower_ for tok in tokens]  # noqa: E501


    # tokens = [tok for tok in tokens if (tok not in stopwords and tok not in punctuations)]  # noqa: E501
    tokens = [tok for tok in tokens if (tok not in punctuations)]  # noqa: E501
    print(tokens)
    return tokens


# create vectorizer object to generate feature vectors, we will use custom
# spacy’s tokenizer
vectorizer = CountVectorizer(tokenizer=spacy_tokenizer, ngram_range=(1, 3))

classifier = LinearSVC()


# Create the  pipeline to clean, tokenize, vectorize, and classify
pipe = Pipeline([("cleaner", predictors()),
                 ('vectorizer', vectorizer),
                 ('classifier', classifier)])

# Load sample data
train = [('I love this sandwich.', 'pos'),
         ('this is an amazing place!', 'pos'),
         ('I feel very good about these beers.', 'pos'),
         ('this is my best work.', 'pos'),
         ("what an awesome view", 'pos'),
         ('I do not like this restaurant', 'neg'),
         ('I am tired of this stuff.', 'neg'),
         ("I can't deal with this", 'neg'),
         ('he is my sworn enemy!', 'neg'),
         ('my boss is horrible.', 'neg'),
         ('Ney York is on the east coast.', 'net'),
         ('My commute to work is about one hour.', 'net'),
         ('How do I change my oil?', 'net'),
         ('What is the weather like tomorrow?', 'net'),
         ('I bought the bigger one', 'net')
]

test =   [('the beer was good.', 'pos'),
         ('I do not enjoy my job', 'neg'),
         ("I ain't feelin dandy today.", 'neg'),
         ("I feel amazing!", 'pos'),
         ('Gary is a good friend of mine.', 'pos'),
         ("I can't believe I'm doing this.", 'neg'),
         ("Gary is not a good friend of mine.", 'neg'),
         ("This is not good.", 'neg'),
         ("Trump is ruining our country!", 'neg'),
         ('I never liked this restaurant!', 'neg'),
         ('I bought the bigger one', 'net'),
         ('The training data must be used.', 'net')
]

# Create model and measure accuracy
pipe.fit([x[0] for x in train], [x[1] for x in train])
pred_data = pipe.predict([x[0] for x in test])
for (sample, pred) in zip(test, pred_data):
    print(sample, pred)
print("Accuracy:", accuracy_score([x[1] for x in test], pred_data))

for word in stopwords:
    if word is "not":
        print('It exists: ', word)
