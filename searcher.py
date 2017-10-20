# -*- coding: utf-8 -*-
import sys
from os import environ
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

# hack to deal with encoding issue
reload(sys)
sys.setdefaultencoding('UTF8')

host = environ['es_host']
awsauth = AWS4Auth(environ['aws_key'],
                   environ['aws_secret'],
                   environ['aws_region'], 'es')

es = Elasticsearch(hosts=[{'host': host, 'port': 443}],
                   http_auth=awsauth,
                   use_ssl=True,
                   verify_certs=True,
                   connection_class=RequestsHttpConnection)



if __name__ == '__main__':

    # define structure
    request_body = {
        'mappings': {
            'tweet': {
                'properties': {
                    'user_name': {'type': 'string'},
                    'screen_name': {'type': 'string'},
                    'text': {'type': 'string'},
                    'location': {'type': 'geo_point'},
                    'date': {'type': 'string'}
                }
            }
        }
    }

    es.indices.create(index='tweets', body=request_body)
