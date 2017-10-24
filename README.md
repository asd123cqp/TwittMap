# TwittMap

[Link](http://twittmap-env.etjvjrbft2.us-west-1.elasticbeanstalk.com/)

TwittMap is Assignment 1 for COMS 6998-Cloud Computing and Big Data. We use Tweepy for streaming the real-time tweet, store them into AWS ElasticSearch. The back-end server is Flask on AWS Elastic Beanstalk.

![demo](static/images/demo-v1.2.jpg)

## How to get started?

- [x] Develop a web app with something simple and deploy that using Elastic Bean Stalk.
- [x] Modify your webapp to be able to put a tag on a map using GoogleMaps API.
- [x] Use Twitter API to collect 10MB or so Twitts and process these offline. Allow user to search along few key words and display those twitts on the map. You also extract location tags when available from the Twitts. If no geotag available, you may infer the location from the keywords (i.e., any mention of places), if no mention of places, then feel free to choose a location randomly.
- [x] Next you may want to look at streaming API to get the twitts in real-time and process and add to the whole process.

## Environment Variables

Please set up your environment variables before deploying:

- "twitt_api_key": Consumer Key (API Key)
- "twitt_api_secret": Consumer Secret (API Secret)
- "twitt_token_key": Access Token
- "twitt_token_secret": Access Token Secret
- "aws_key": AWS User Access key ID
- "aws_secret": AWS User Access key Secret Token
- "aws_region": AWS Elasticsearch Region
- "es_host": Elasticsearch Host Address

## Architecture
- streamer.py Using Tweepy to stream real-time tweet into Elastic Search
- application.py The main server program using Flask to search tweets in Elastic Search
- static/index.html The homepage html file of this project
- static/javascript/script.js Javascript file to manipulate with Google Map api