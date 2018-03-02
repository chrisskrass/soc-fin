#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Haotian Zhang (AlexHtZhang)

'''This is an example on using the twitter_crawler to get specific desired data. Get the 
tweets on United Airlines 10000 per day, from 2017-04-04 to 2017-04-14 and save as .cvs files. Get the tweets on Tesla 10000 
per day, from 2018-01-29 to 2017-02-07 and save as .cvs files.

Function(s):
	get_tweets_united_airlines():
		"""Get the tweets on United Airlines 10000 per day, from 2017-04-04 to 2017-04-14 
		and save as .cvs files.
			:input: None
		    :type: None
		    :return: None
		    :type: None
		"""	

	get_tweets_tesla():
		"""Get the tweets on Tesla 10000 per day, from 2018-01-29 to 2017-02-07 and save 
		as .cvs files.
			:input: None
		    :type: None
		    :return: None
		    :type: None
		"""	

Requrements:
python 2.7.14.final.0
For install instructions, please go to https://www.python.org/downloads/ 
Make sure to install python: 2.7.14.final.0.


This program was developed and tested under following environments:
python: 2.7.14.final.0
python-bits: 64
OS: Darwin
OS-release: 16.7.0
machine: x86_64
processor: i386
byteorder: little
LC_ALL: None
LANG: en_US.UTF-8
LOCALE: None.None
'''

import sys
assert sys.version_info[0] < 3
from got import manager
import csv

# Example One
def get_tweets_united_airlines():
	"""Get the tweets on United Airlines 10000 per day, from 2017-04-04 to 2017-04-14 and save as .cvs files.
		:input: None
	    :type: None
	    :return: None
	    :type: None
	"""
	date_Day = ['04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '15']
	for date_DD in xrange(10):
		tweet_criteria = manager.TweetCriteria()
		tweet_criteria.setQuerySearch("United Airlines").setSince("2017-04-" 
			+ date_Day[date_DD]).setUntil("2017-04-" + date_Day[date_DD + 1]).setMaxTweets(10000)
		tweets = manager.TweetManager().getTweets(tweet_criteria)
		manager.TweetHelper().getCSV(tweets, 'United_Airlines_'+ "2017-04-" + date_Day[date_DD] + '.csv')

# Example Two
def get_tweets_tesla():
	"""Get the tweets on Tesla 10000 per day, from 2018-01-29 to 2017-02-07 and save as .cvs files.
		:input: None
	    :type: None
	    :return: None
	    :type: None
	"""
	date_Day = ['01-29', '01-30', '01-31', '02-01', '02-02', '02-03', '02-04', '02-05', '02-06', '02-07', '02-08']
	for date_DD in xrange(10):
		tweet_criteria = manager.TweetCriteria()
		tweet_criteria.setQuerySearch("United Airlines").setSince("2018-" 
			+ date_Day[date_DD]).setUntil("2018-" + date_Day[date_DD + 1]).setMaxTweets(10000)
		tweets = manager.TweetManager().getTweets(tweet_criteria)
		manager.TweetHelper().getCSV(tweets, 'TESLA_'+ "2018-" + date_Day[date_DD] + '.csv')

if __name__ == '__main__':
	get_tweets_united_airlines()
	get_tweets_tesla()
