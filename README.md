# TwittMap

[Link](http://twittmap-env.etjvjrbft2.us-west-1.elasticbeanstalk.com/)

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

## TODO

- [x] Marker Clustering

- [x] Use ElasticSearch’s geospatial feature that shows tweets that are within a certain distance from the point the user clicks on the map.
