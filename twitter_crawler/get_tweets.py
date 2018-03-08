#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Haotian Zhang (AlexHtZhang)

'''This is an example on using the twitter_crawler to get specific desired data and save them into .csv files.

Function(s):
	get_tweets( search_query, company_name, date_list, max_tweets_perday):
		"""Get the tweets on sepecified company from company_name and search key word from search_query, 
		in the duration of date_list, in the amount of tweets as max_tweets_perday and save as .cvs files
		for data of each single day in the name fashion of company_name+data.csv.

		Note: The input parameter date_list should follow the YYYY-MM-DD format. For example: ['2018-02-02', 
		'2018-02-03', '2018-02-04'] The last day is inclusive in the result but required, so if you want to 
		get the data for only one desired day, you still need input the string of the day after that day.

			:input: search_query
		    :type: string
		    :input: company_name
		    :type: string
			:input: date_list
		    :type: list of string(s)
			:input: max_tweets_perday
		    :type: int
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
assert sys.version_info[0] < 3 # assure the python version smaller than 3.0
from got import manager
import csv


def get_tweets( search_query, company_name, date_list, max_tweets_perday):
	"""Get the tweets on sepecified company from company_name and search key word from search_query, 
	in the duration of date_list, in the amount of tweets as max_tweets_perday and save as .cvs files
	for data of each single day in the name fashion of company_name+data.csv.

	Note: The input parameter date_list should follow the YYYY-MM-DD format. For example: ['2018-02-02', 
	'2018-02-03', '2018-02-04'] The last day is inclusive in the result but required.

		:input: search_query
	    :type: string
	    :input: company_name
	    :type: string
		:input: date_list
	    :type: list of string(s)
		:input: max_tweets_perday
	    :type: int
	    :return: None
	    :type: None
	"""
	assert isinstance(search_query, str) # input search_query should be str
	assert isinstance(company_name, str) # input company_name should be str
	assert isinstance(date_list, list) # input date_list should be list
	assert isinstance(max_tweets_perday, int) # input max_tweets_perday should be int

	assert len(date_list) > 1 # input date_list should have length greater than one, last date is inclusive.
	assert all(map(lambda i:isinstance(i,str), date_list)) # input date_list should be a list of str

	date_Day = date_list
	for date_DD in xrange(len(date_Day) - 1):
		tweet_criteria = manager.TweetCriteria()
		tweet_criteria.setQuerySearch(search_query).setSince(
			date_Day[date_DD]).setUntil(date_Day[date_DD + 1]).setMaxTweets(max_tweets_perday)
		tweets = manager.TweetManager().getTweets(tweet_criteria)
		manager.TweetHelper().getCSV(tweets, company_name + '_'+ date_Day[date_DD] + '.csv')

	return

# Example usage of get_tweets
get_tweets( 'example', 'example', ['2018-02-18', '2018-02-19'], 1)

# get tweets for our intrest
get_tweets( 'United Airlines', 'United_Airlines', ['2017-04-04', '2017-04-05', '2017-04-06', '2017-04-07', \
	'2017-04-08', '2017-04-09', '2017-04-10', '2017-04-11', '2017-04-12', '2017-04-13', '2017-04-15'], 10000)
get_tweets( 'Snapchat', 'SNAPCHAT', ['2018-02-17', '2018-02-18', '2018-02-19',  '2018-02-20', '2018-02-21', \
	'2018-02-22', '2018-02-23', '2018-02-24', '2018-02-25', '2018-02-26', '2018-02-27', '2018-02-28'], 10000)
get_tweets( 'Tesla', 'TESLA', ['2018-02-02', '2018-02-03', '2018-02-04', '2018-02-05', '2018-02-06', \
	'2018-02-07', '2018-02-08', '2018-02-09', '2018-02-10', '2018-02-11', '2018-02-12'], 10000)


