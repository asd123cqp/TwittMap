# TwittMap

[Link](https://twittmap.cqp.cloud/)

TwittMap is Assignment 1 for COMS 6998-Cloud Computing and Big Data. It shows tweets on Google Maps and allows users to filter tweets by keywords or geo distance. Tweepy is used to stream treal-time tweets with selected keywords into AWS ElasticSearch.

Previously, the Flask back-end server was used to serve static files and to make ElasticSearch queries for clients. In v2.0, I moved the ElasticSearch querying functionality to client side, and now a back-end server is no longer necessary.

![demo](static/images/demo-v1.2.1.jpg)

## Architecture

- `streamer.py`: Stream real-time tweet with selected keywords into AWS Elastic Search
  - Usage: `python streamer.py`

- `static/index.html`: The homepage html file of this project

- `static/javascript/script.js`: Javascript file to manipulate with Google Map api

- (Depreciated)`application.py`: Flask Server to ~~search tweets in Elastic Search and~~ serve `/static/` files -> better use other servers.

## Environment Variables

Please set up your environment variables before streaming tweets to ElasticSearch with `streamer.py`:

- `twitt_api_key`: Consumer Key (API Key)
- `twitt_api_secret`: Consumer Secret (API Secret)
- `twitt_token_key`: Access Token
- `twitt_token_secret`: Access Token Secret
- `es_host`: Elasticsearch Host Address
- `aws_region`: AWS Elasticsearch Region
- `aws_key`: AWS User Access key ID (Not needed if your Elasticsearch server allows public write access)
- `aws_secret`: AWS User Access key Secret Token (Not needed if your Elasticsearch server allows public write access)
