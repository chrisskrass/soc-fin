# ECE180_Winter2018_Group8

A friendly list for grader -- Files for grading:
twitter_crawler/get_tweets.py
twitter_analyzer/get_sentiment_data.py
stock_crawler/get_stock_data.py

## Introduction

The goal of this project was to compare positive and negative statements posted on twitter and comparing them to effects they could have on the stock market.

***Beaware if you want to reproduce the result of this project, it may take hours to days to get the twitter data, since the offical API has restriction, we used 'Get-Old-Tweets-Programatically'. If you want to replot the result, all the data is avaliable in this repo.***

Key Events:
1. Snapchat stock loses $1.3 billion after Kylie Jenner tweet  (Feb 21, 2018)
2. Elon Musk Sent His Tesla to Space (Feb 6, 2018)
3. United airlines scandal, beat passenger (April 9, 2017)


## Pipline

1. Data Acquisition & Preprocessing:

	get stock data
	      |
	get twitter data
	      |
	sentiment analyze on twitter data

2. Data Visulization:

	plot&visulization


## Data Acquisition & Preprocessing

Data acquisition & preprocessing was done in the following folders:

```
twitter_crawler
stock_crawler
twitter_analyzer
```

In the ***readme.md file in each folder***, there are comprehensive guidlines on how to install reuse use the files. All the files and functions are well documented and support 'help' commend.

All the desired data are stored in the following folders.

```
twitter_data
stock_data
semtiment_data
```


## Data Visulization