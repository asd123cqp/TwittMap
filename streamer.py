# -*- coding: utf-8 -*-
import tweepy
from os import environ
from searcher import es

# keywords to stream
KEYWORDS = ['apple', 'bar', 'cat', 'dog', 'eat', 'food']

def parse_tweet(tweet):
    return {'user_name': tweet['user']['name'],
            'screen_name': tweet['user']['screen_name'],
            'text': tweet['text'],
            'location': {'lat': tweet['coordinates']['coordinates'][1],
                         'lon': tweet['coordinates']['coordinates'][0]},
            'date': tweet['created_at']}

class StreamListener(tweepy.StreamListener):
    """docstring for StreamListener"""

    # save twitts to Elastic Search
    def on_status(self, status):
        # reject twitts without geotag
        if status._json['coordinates'] is None:
            return
        tweet = parse_tweet(status._json)
        print tweet, "\n---------------"
        es.index(index="tweets", doc_type="tweet", body=tweet)

class Streamer:
    """docstring for Streamer"""
    def __init__(self, auth=None, keywords=['foo']):
        self.keywords = keywords
        self.streamer = tweepy.Stream(auth=auth, listener=StreamListener())

    def run(self):
        self.streamer.filter(None, self.keywords)
        self.streamer.userstream(None)

if __name__ == '__main__':

    twitter_auth = tweepy.OAuthHandler(environ['twitt_api_key'],
                               environ['twitt_api_secret'])
    twitter_auth.set_access_token(environ['twitt_token_key'],
                          environ['twitt_token_secret'])

    print es.info()
    print "---------------\nStreamming...\n---------------"
    streamer = Streamer(twitter_auth, KEYWORDS)
    streamer.run()
