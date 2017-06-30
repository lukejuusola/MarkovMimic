#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'twitter consumer key'
CONSUMER_SECRET = 'twitter consumer secret key'
ACCESS_KEY = 'twitter access key'
ACCESS_SECRET = 'twitter access secet key'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
username = 'MattMarkov007'
# test tweet
# api.update_status("sometimes i just really need some soup, you know?")
