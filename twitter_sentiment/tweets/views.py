# from django.shortcuts import render
import tweepy

from django.http import Http404, JsonResponse

from . import get_tweets


def tweets(search):
    """ Fetches Tweets with Tweepy """

    consumer_key = '7bdUIEJDOLveAiWuHK4dxQDqC'
    consumer_secret = 'wrvb59PcIjOP5kuQlmQYqmU3fo5GIMps3OnCmfT3aNNtKIFaGw'
    access_token = '1873426352-gvELy2xJU4VKazKnu1v2QgYWknpgovDktkCHDdU'
    access_token_secret = 'v8oHQs80fDTZbu16AGDOYYZlAyOIIjPo7o6seRme5glnl'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    def fetch_tweets(search):
        tweets_list = []
        tweets = api.search(search, count=100)

        for tweet in tweets:
            json_tweet = tweet._json
            tweets_list.append(json_tweet['text'])

        # print(formatted_tweets)

        return tweets_list

    return JsonResponse({"tweets": fetch_tweets('Trump')})
