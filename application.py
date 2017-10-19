import threading, tweepy, time
from os import environ
from elasticsearch import Elasticsearch
from index import App
from streamer import Streamer

# keywords to stream
KEYWORDS = ['apple', 'bar', 'cat', 'dog', 'eat', 'food']

# run the app.
if __name__ == "__main__":
    # load api key and token
    auth = tweepy.OAuthHandler(environ['twitt_api_key'],
                               environ['twitt_api_secret'])
    auth.set_access_token(environ['twitt_token_key'],
                          environ['twitt_token_secret'])
    es = Elasticsearch([environ['es_host']])

    # start worker threads
    tweet_streamer, app = Streamer(auth, es, KEYWORDS), App(es)
    tasks, threads = (app.run, tweet_streamer.start), []
    for task in tasks:
        t = threading.Thread(target=task)
        t.daemon = True
        threads.append(t)
        print 'Starting', t
        t.start()

    while True:
        time.sleep(10)
