# tokenizing - word tokenizers or sentence tokenizers
# lexicons and corporas
# corpora - body of text, i.e. medical journal, speeches, English language
# lexicon - words and their meaning

# investor speal 'bull' - someone who is positive about the market
# english speak 'bull' - scary animal you don't want running at you

import nltk

# from nltk.tokenize import sent_tokenize, word_tokenize
#
# example_text = 'Hello Mr. Smith, how are you you doing today? The weather is great and Python is awesome. The sky is pinkish-blue. You should not eat cardboard.'

# print(sent_tokenize(example_text))
#
# print(word_tokenize(example_text))
#
# for i in word_tokenize(example_text):
#     print(i)

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example showing off stop word filtration."

stop_words = set(stopwords.words('english'))

words = word_tokenize(example_sentence)

# filtered_sentence = []
#
# for w in words:
#     if w not in stop_words:
#         filtered_sentence.append(w)
#
# print(filtered_sentence)

# filtered_sentence = [w for w in words if not w in stop_words]

# print(filtered_sentence)
