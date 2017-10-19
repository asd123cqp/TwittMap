# -*- coding: utf-8 -*-
import json
from flask import Flask, render_template, request
from searcher import es

# helper functions
def get_tweets(kw):
    if kw == 'all':
        body = {"query": {"match_all": {}}}
    else:
        body = {"query": {"match": {'text': {'query': kw}}}}

    # search tweets with es
    data = es.search(index="tweet_index",
                     body=body,
                     size=10000)['hits']['hits']

    # parse raw data & return
    tweets = [t['_source'] for t in data]
    return json.dumps(tweets), len(tweets)

def render_kw(kw):
    tweets, num = get_tweets(kw)
    return render_template('index.html', kw=kw,
                           tweets=tweets, num=num)

# init
application = Flask(__name__)

@application.route('/')
def index():
    return render_kw('all')

@application.route('/search/')
def search():
    return render_kw(request.args.get('q'))

# run the app.
if __name__ == "__main__":
    application.debug = True
    application.run()
