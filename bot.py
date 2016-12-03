#!/usr/bin/env python3

import yaml
import twitter

with open("conf.yml", 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)

consumer_key = cfg['twitter']['consumer_key']
consumer_secret = cfg['twitter']['consumer_secret']
access_token = cfg['twitter']['access_token']
access_token_secret = cfg['twitter']['access_token_secret']

api = twitter.Api(consumer_key=consumer_key,
					consumer_secret=consumer_secret,
					access_token_key=access_token,
					access_token_secret=access_token_secret)

search = api.GetSearch(raw_query="q=covea %23covea lang%3Afr&src=typd")

for t in search:
	print(t.text)
	print(t.user.screen_name)
	print("==============")




