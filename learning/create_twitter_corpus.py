from spacy.en import English

import string
punctuations = string.punctuation


parser = English()

file_name = '/home/vox/nltk_data/corpora/twitter_samples/negative_tweets.json'

file_str = str(open(file_name).read())

sentences = file_str.split(',')

new_list = []


def find_tweet(word, string):
    if word in string:
        new_list.append((string.strip('"text": '), 'neg'))


def clean_text(text):
    return text.strip().lower()


for sent in sentences:
    find_tweet('"text":', sent)


print(new_list)
