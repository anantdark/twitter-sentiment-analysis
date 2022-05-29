from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import tweepy
import numpy as np
import pandas as pd
import logging as logger


class Import_tweet_sentiment:

	consumer_key="h28toYwlYUF8iXeqPHu8tbNf8"
	consumer_secret="TGBvlwSsccFEptgc7ibxeCp6vL5AnIa41l8GnC3SaOmkJMVsl1"
	access_token="1530458824380850181-5bDGNSXjgSO7gEBKc94Kubz7hAswwc"
	access_token_secret="fyte8e9D3tL0jmyVvwfts1oS0DXqVBbdiwc41MdWsXG4L"

	def tweet_to_data_frame(self, tweets):
		df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
		return df

	def get_tweets(self, handle):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		auth_api = API(auth)
		logger.info("auth api set")
		# li  = auth_api.search_tweets(q = "sad")

		account = handle
		item = auth_api.user_timeline(id=account,count=20)
		df = self.tweet_to_data_frame(item)

		all_tweets = []
		for j in range(20):
			all_tweets.append(df.loc[j]['Tweets'])
		return all_tweets

	def get_hashtag(self, hashtag):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		auth_api = API(auth)
		# auth_api = tweepy.Client(consumer_key= self.consumer_key,consumer_secret= self.consumer_secret,access_token= self.access_token,access_token_secret= self.access_token_secret)

		account = hashtag
		all_tweets = []

		# for tweet in tweepy.Cursor(auth_api.search_tweets, q=account, lang='en').items(20):
		for tweet in auth_api.search_tweets(q=account , lang='en'):
			all_tweets.append(tweet.text)

		return all_tweets
