from django.shortcuts import render

from django.http import Http404, JsonResponse


def get_tweets(request):
    """ Fetches Tweets with Tweepy """
    return JsonResponse({"data": {}})
