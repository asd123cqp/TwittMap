import threading, tweepy, json, time
from elasticsearch import Elasticsearch
from index import App
from streamer import Streamer

# keywords to stream
KEYWORDS = ['apple', 'bar', 'cat', 'dog', 'eat', 'food']

# file to store auth
KEYFILE = './keys.json'

# run the app.
if __name__ == "__main__":
    # load api key and token
    with open(KEYFILE, 'r') as f:
        keys = json.load(f)
        auth = tweepy.OAuthHandler(keys['twitt_api_key'],
                                   keys['twitt_api_secret'])
        auth.set_access_token(keys['twitt_token_key'],
                              keys['twitt_token_secret'])
        es = Elasticsearch([keys['es_host']])
        # es = Elasticsearch()

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
