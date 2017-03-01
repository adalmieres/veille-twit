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
					access_token_secret=access_token_secret,
					sleep_on_rate_limit=True)

search = api.GetSearch(term="insurtech",count=100,result_type="recent")

print(search[1])

for t in search:
	print("@" + t.user.screen_name)
	url = "https://twitter.com/" +  str(t.user.screen_name) + "/status/" + str(t.id)
	print(url)
	print(t.text)
	print("==============")




