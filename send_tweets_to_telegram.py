#!/usr/bin/env python


import tweepy
from time import sleep
import pytz 
import tzlocal
import json
import yaml
import requests
import telebot
from datetime import datetime, timedelta
from config import access_token,access_token_secret,consumer_key, consumer_secret ,TOKEN
import sys
reload(sys)
sys.setdefaultencoding('utf8')

tb = telebot.TeleBot(TOKEN)



##Setting up authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

##Extracting local timezone
local_timezone = tzlocal.get_localzone() # get pytz tzinfo

##Selecting dateformat 
directive="%d-%m-%Y %I:%M:%S %p"
yesterday = datetime.today () - timedelta (days=1)


max=5
def yaml_load(filepname):
	with open(filename,'r') as read:
		data = yaml.load(read)
		return data

def like_func(user):
	for tweet in tweepy.Cursor(api.user_timeline,screen_name="@"+user,lang="en",tweet_mode="extended").items(max):
		try:
			##Changing tweet timings to local timings		
			utc_time = datetime.strptime(str(tweet.created_at), "%Y-%m-%d %H:%M:%S")
			local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)
			
			
			
			if tweet.created_at > yesterday:
				at=local_time.strftime(directive)
				print(at)
				##Checking for retweets and printing tweets
				if  hasattr(tweet, 'retweeted_status'):
					txt=tweet.retweeted_status.full_text
					t_type="Retweet"
					
				else:	
					txt=tweet.full_text
					t_type="Tweet"					

				print txt
	
				url="https://twitter.com/" + user + "/status/" + str(tweet.id)
				by=t_type + " by : @" + user + "\nAt : " + at + "\n-----------------------------------------------\n" 
				msg= by + txt + "\n\n" + "Go to Tweet -> " + url + "\n \n"
				tb.send_message(chat_id="@apychannel1",text=msg)
				print
		
				##Checking if tweet is already liked or not and liking accordingly
				if tweet.favorited:
					print "This tweet has been already liked"
					print
				else:
					api.create_favorite(tweet.id)
					print "Successfully Liked"
					print

				print ("Tweet length: " + str(len(txt)))
				print url
				
				#for url in tweet.entities['urls']:
				#	expanded_url=url['display_url']
				#	print expanded_url
				print "----------------------------------------------------------------------------------------"
			else:
				break
				
		except tweepy.TweepError as e:
			print(e.reason)
			sleep(10)
			continue
		except	StopIteration:
			break
	


if __name__ == "__main__":
	filename="users.yml"
	data=yaml_load(filename)
	val = data.get('Users')
	for i in val:
		print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
		print "Running Bot for user " +i
		print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
		like_func(i)
		
	


