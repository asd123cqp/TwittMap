import tweepy

def parse_tweet(tweet):
    return {'username': tweet['user']['name'],
            'nickname': tweet['user']['screen_name'],
            'text': tweet['text'],
            'coord': tweet['coordinates']['coordinates'],
            'date': tweet['created_at']}

class StreamListener(tweepy.StreamListener):
    """docstring for StreamListener"""
    def __init__(self, es=None):
        super(StreamListener, self).__init__()
        self.es = es

    # save twitts to Elastic Search
    def on_status(self, status):
        # reject twitts without geotag
        if status._json['coordinates'] is None:
            return

        self.es.index(index="tweet_index",
                      doc_type="tweet",
                      body=parse_tweet(status._json))

class Streamer:
    """docstring for Streamer"""
    def __init__(self, auth=None, es=None, keywords=['foo']):
        self.keywords = keywords
        self.streamer = tweepy.Stream(auth=auth, listener=StreamListener(es))

    def start(self):
        self.streamer.filter(None, self.keywords)
        self.streamer.userstream(None)
