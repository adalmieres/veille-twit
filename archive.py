#!/usr/bin/env python3

import yaml
import json
import twitter
import os

with open("conf.yml", 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)

consumer_key = cfg['twitter']['consumer_key']
consumer_secret = cfg['twitter']['consumer_secret']
access_token = cfg['twitter']['access_token']
access_token_secret = cfg['twitter']['access_token_secret']
pseudo = "@"
pseudo += cfg['twitter']['screen_name']

api = twitter.Api(consumer_key=consumer_key,
					consumer_secret=consumer_secret,
					access_token_key=access_token,
					access_token_secret=access_token_secret,
					sleep_on_rate_limit=True)

# this part archive all my tweet exept RTs

oldestID=None

while True:
    status = api.GetUserTimeline(screen_name=pseudo, count=200, max_id=oldestID, include_rts=False)

    for s in status:
        print(str(s.id) + str(":") + str(s.created_at))
        with open('status.json','a') as jsonFile:
            jsonFile.write(str(s._json) + os.linesep)
        if oldestID == None:
            oldestID = s.id
        if s.id < oldestID:
            oldestID = s.id

    if len(status)==1:
        break
