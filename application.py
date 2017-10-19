# -*- coding: utf-8 -*-
import json
from flask import Flask, render_template, request
from searcher import es

# helper function
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
    return json.dumps(tweets)


# init
application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html',
                           kw='all',
                           tweets=get_tweets('all'))
@application.route('/search/')
def search():
    kw = request.args.get('q')
    return render_template('index.html',
                           kw=kw,
                           tweets=get_tweets(kw))

# run the app.
if __name__ == "__main__":
    application.debug = True
    application.run()
