#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Haotian Zhang (AlexHtZhang)

'''This is an example on using the sentiment analysis on tweets on any desired date frame. 
Get the sentiment analysis on tweets on United Airlines 10000 per day, from 2017-04-04 to 
2017-04-14 and save as .cvs files. Get the sentiment analysis on tweets on Tesla 10000 per 
day, from 2018-01-29 to 2017-02-07 and save as .cvs files.

note: if you installed this package via python "setup.py install", you may need 
to import like this: 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

Function(s):
      get_sentiment_unitedairlines():
          """Get the sentiment analysis on tweets on United Airlines 10000 per day, 
          from 2017-04-04 to 2017-04-14 and save as .cvs files.
              :input: None
              :type: None
              :return: None
              :type: None
          """

      get_sentiment_tesla():
          """Get the sentiment analysis on tweets on Tesla 10000 per day, from 
          2018-01-29 to 2017-02-07 and save as .cvs files.
              :input: None
              :type: None
              :return: None
              :type: None
          """


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

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import codecs # support codecs.open encoding utf-8 in python2 
import pandas as pd # support csv reading


# Example One:
def get_sentiment_unitedairlines():
    """Get the sentiment analysis on tweets on United Airlines 10000 per day, 
    from 2017-04-04 to 2017-04-14 and save as .cvs files.
        :input: None
        :type: None
        :return: None
        :type: None
    """
    fields = ['date', 'retweets', 'favorites', 'text'] # files to read
    # get any desird day as you want
    date_Day = ['04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '15'] 
    for date_DD in xrange(10):
        csv_input = pd.read_csv('United_Airlines_'+ "2017-04-" + 
          date_Day[date_DD] + '.csv', skipinitialspace=True, usecols=fields)

        analyzer = SentimentIntensityAnalyzer()
        sentiment_neg = [] 
        sentiment_neu = []
        sentiment_pos = []
        sentiment_compound = []

        for sentence in csv_input.text:
            sentiment_single = analyzer.polarity_scores(str(sentence))
            sentiment_neg.append(sentiment_single['neg'])
            sentiment_neu.append(sentiment_single['neu'])
            sentiment_pos.append(sentiment_single['pos'])
            sentiment_compound.append(sentiment_single['compound'])

        csv_input['negative'] = sentiment_neg
        csv_input['neutral'] = sentiment_neu
        csv_input['positive'] = sentiment_pos
        csv_input['compound'] = sentiment_compound
        csv_input.to_csv('United_Airlines_Sentiment_'+ "2017-04-" + 
          date_Day[date_DD] + '.csv', index=False)

# Example Two:
def get_sentiment_tesla():
    """Get the sentiment analysis on tweets on Tesla 10000 per day, 
    from 2018-01-29 to 2017-02-07 and save as .cvs files.
        :input: None
        :type: None
        :return: None
        :type: None
    """
    fields = ['date', 'retweets', 'favorites', 'text'] # files to read
    # get any desird day as you want
    date_Day = ['01-29', '01-30', '01-31', '02-01', '02-02', '02-03',\
     '02-04', '02-05', '02-06', '02-07', '02-08'] 
    for date_DD in xrange(10):
        csv_input = pd.read_csv('TESLA_'+ "2018-" + date_Day[date_DD] 
          + '.csv', skipinitialspace=True, usecols=fields)

        analyzer = SentimentIntensityAnalyzer()
        sentiment_neg = []
        sentiment_neu = []
        sentiment_pos = []
        sentiment_compound = []

        for sentence in csv_input.text:
            sentiment_single = analyzer.polarity_scores(str(sentence))
            sentiment_neg.append(sentiment_single['neg'])
            sentiment_neu.append(sentiment_single['neu'])
            sentiment_pos.append(sentiment_single['pos'])
            sentiment_compound.append(sentiment_single['compound'])

        csv_input['negative'] = sentiment_neg
        csv_input['neutral'] = sentiment_neu
        csv_input['positive'] = sentiment_pos
        csv_input['compound'] = sentiment_compound
        csv_input.to_csv('TESLA_Sentiment_'+ "2018-" + date_Day[date_DD] 
          + '.csv', index=False)

get_sentiment_unitedairlines() # call get_sentiment_unitedairlines
get_sentiment_tesla() # call get_sentiment_tesla

