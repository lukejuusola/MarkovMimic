from botAuth import *
import time, tweepy, datetime
import ScrapeTweets as MattData
from MarkovChainBot import *
from html.parser import HTMLParser
import datetime

m = MarkovChainBot([r'@.*', '^rt$', r'http.*'])
tweets = [x.text for x in MattData.statuses]
m.data = tweets
m.Train()
p = HTMLParser()
logfile = open('errorlog.txt', 'a')

def LogException(logfile, error):
	logfile.write(str(datetime.datetime.now()) + ': ')
	logfile.write(str(error))
	logfile.write('\n')

if __name__ == '__main__':
	while True:
		tweet = m.GenerateText().strip()
		print(username + ' tweeted @ ' + str(datetime.datetime.now()))
		print(tweet)
		if(tweet):
			try:
				api.update_status(p.unescape(tweet))
			except Exception as error:
				print('An error occurred')
				LogException(logfile, error)	
		time.sleep(60*60)


