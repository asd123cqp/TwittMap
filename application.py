# -*- coding: utf-8 -*-
import json
from flask import Flask, render_template, request, current_app
from searcher import es

# helper functions
def get_tweets(kw, dist=None, loc=None):
    query = {"query": {"bool": {}}}
    if kw == 'all':
        query["query"]["bool"]["must"] = {"match_all": {}}
    else:
        query["query"]["bool"]["must"] = {"match": {'text': {'query': kw}}}

    if dist:
        query["query"]["bool"]["filter"] = {
            "geo_distance": {
                "distance": dist,
                "location": loc
            }
        }

    # search tweets with es
    data = es.search(index="tweets",
                     body=query,
                     size=10000)['hits']['hits']

    # parse raw data & return
    tweets = [t['_source'] for t in data] if data else []
    return json.dumps(tweets)

# init
application = Flask(__name__)

# static index file
@application.route('/')
def index():
    return current_app.send_static_file('index.html')

# response to query
@application.route('/search/')
def search():
    kw, dist = request.args.get('kw'), request.args.get('rad')
    if not dist:
        return get_tweets(kw)

    loc = request.args.get('loc')
    return get_tweets(kw, dist + 'km', loc)

# run the app.
if __name__ == "__main__":
    # application.debug = True
    application.run()
