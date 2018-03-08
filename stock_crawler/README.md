# stock_crawler

The use to get specific data from specific company can be found in 'get_stock_data.py'

It's developed and tested in python 2.7.

## Requirment
	need the googlefinance-client-python from the orignial ropo, the pip install will only
	install the version 1.3.0 which has bug in it. The newest version 1.3.1 hasn't been published.
	
	$ git clone https://github.com/pdevty/googlefinance-client-python.git
	$ cd googlefinance-client-python
    $ python setup install

## Usage

```
Please make sure you install the package in the right way.
To use 'get_stock_data.py' to get the google stock data. Based on input parameter get price data 
(return pandas dataframe) and save as csv file, just follow the following examples.

python
from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data

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
get_stock_data(param_UA) 
get_stock_data(param_Tesla)
get_stock_data(param_Snapchat)


python
from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data

# Dow Jones
param = {
	'q': ".DJI", # Stock symbol (ex: "AAPL")
	'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
	'x': "INDEXDJX", # Stock exchange symbol on which stock is traded (ex: "NASD")
	'p': "1Y" # Period (Ex: "1Y" = 1 year)
}
# get price data (return pandas dataframe)
df = get_price_data(param)
print(df)
#                          Open      High       Low     Close     Volume
# 2016-05-17 05:00:00  17531.76   17755.8  17531.76  17710.71   88436105
# 2016-05-18 05:00:00  17701.46  17701.46  17469.92  17529.98  103253947
# 2016-05-19 05:00:00  17501.28  17636.22  17418.21  17526.62   79038923
# 2016-05-20 05:00:00  17514.16  17514.16  17331.07   17435.4   95531058
# 2016-05-21 05:00:00  17437.32  17571.75  17437.32  17500.94  111992332
# ...                       ...       ...       ...       ...        ...
```

## Environment

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