from botAuth import *
import tweepy, time

accountsToScrape = ['matthewdudee']
username = "matthewdudee"


statuses = []
page = 1
while True:
	try:
		page_statuses = api.user_timeline(username, page=page)
	except tweepy.error.RateLimitError:
		time.sleep(60 * 15.)
		continue
	if(not page_statuses):
		break
	statuses += page_statuses
	page += 1
	
