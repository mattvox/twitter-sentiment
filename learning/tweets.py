import tweepy
import json

consumer_key = '7bdUIEJDOLveAiWuHK4dxQDqC'
consumer_secret = 'wrvb59PcIjOP5kuQlmQYqmU3fo5GIMps3OnCmfT3aNNtKIFaGw'
access_token = '1873426352-gvELy2xJU4VKazKnu1v2QgYWknpgovDktkCHDdU'
access_token_secret = 'v8oHQs80fDTZbu16AGDOYYZlAyOIIjPo7o6seRme5glnl'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

trump_tweets = api.search('Trump', count=100)

formatted_tweets = []

for tweet in trump_tweets:
    json_tweet = tweet._json
    formatted_tweets.append(json_tweet['text'])

# print(trump_tweets[0]._json)

for index, tweet in enumerate(formatted_tweets):
    # if index < 10:
    print(index, ':', tweet, '\n')

# print(type(trump_tweets))

# print(trump_tweets)

# print(dir(trump_tweets))

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
