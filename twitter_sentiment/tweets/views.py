# from django.shortcuts import render

from django.http import Http404, JsonResponse

import get_tweets


def tweets(search):
    """ Fetches Tweets with Tweepy """
    new_tweets = get_tweets.fetch_tweets(search)
    return JsonResponse({new_tweets})
