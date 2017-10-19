import json
from flask import Flask, render_template, request

class App:
    """docstring for App"""
    def __init__(self, es=None):
        self.es = es
        app = Flask(__name__)
        self.app = app

        @app.route('/')
        def index():
            return render_template('index.html',
                                   kw='all',
                                   tweets=self.get_tweets('all'))
        @app.route('/search/')
        def search():
            kw = request.args.get('q')
            return render_template('index.html',
                                   kw=kw,
                                   tweets=self.get_tweets(kw))

    def get_tweets(self, kw):
        if kw == 'all':
            body = {"query": {"match_all": {}}}
        else:
            body = {"query": {"match": {'text': {'query': kw}}}}

        # search tweets with es
        data = self.es.search(index="tweet_index",
                              body=body,
                              size=10000)['hits']['hits']

        # parse raw data & return
        tweets = [t['_source'] for t in data]
        return json.dumps(tweets)

    def run(self):
        self.app.run()
