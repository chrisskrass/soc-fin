#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Haotian Zhang (AlexHtZhang)

'''This is an example on getting the google stock data. Based on input parameter get price data 
(return pandas dataframe), save as csv file

	need the googlefinance-client-python from the orignial ropo, the pip install will only
	install the version 1.3.0 which has bug in it. The newest version 1.3.1 hasn't been published.
	
	$ git clone https://github.com/pdevty/googlefinance-client-python.git
	$ cd googlefinance-client-python
    $ python setup install

Function(s):
	def get_stock_data(param):
		"""based on input parameter get price data (return pandas dataframe),
		save as csv file
			:input: param
	        :type: dict 
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
from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data

def get_stock_data(param):
	'''based on input parameter get price data (return pandas dataframe),
	save as csv file
		:input: param
        :type: dict 
        :return: None
        :type: None
	'''
	# input should be a dict with only for pairs
	assert isinstance(param, dict) 
	assert all(map(lambda i:isinstance(i,str),param))
	assert 'q' in param # Stock symbol (ex: "AAPL")
	assert 'i' in param # Interval size in seconds ("86400" = 1 day intervals)
	assert 'x' in param # Stock exchange symbol on which stock is traded (ex: "NASD")
	assert 'p' in param # Period (Ex: "1Y" = 1 year)
	df = get_price_data(param)
	df.to_csv(param['q'] + '_' + param['i'] + '_' + param['x'] + '_' + param['p'] + '.csv')
	return 


# United Airlines
param_UA = {
	'q': "UAL", # Stock symbol (ex: "AAPL")
	'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
	'x': "NYSE", # Stock exchange symbol on which stock is traded (ex: "NASD")
	'p': "5Y" # Period (Ex: "1Y" = 1 year)
}

# Tesla 
param_Tesla = {
	'q': "TSLA", # Stock symbol (ex: "AAPL")
	'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
	'x': "NASDAQ", # Stock exchange symbol on which stock is traded (ex: "NASD")
	'p': "5Y" # Period (Ex: "1Y" = 1 year)
}

param_Snapchat = {
	'q': "SNAP", # Stock symbol (ex: "AAPL")
	'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
	'x': "NYSE", # Stock exchange symbol on which stock is traded (ex: "NASD")
	'p': "5Y" # Period (Ex: "1Y" = 1 year)
}
# call get_stock_data to get desired stock data
# get_stock_data(param_UA) 
# get_stock_data(param_Tesla)
get_stock_data(param_Snapchat)