# Docker_telebot
This repo has telebot integrated with docker

Requirements:
1] Dockerfile : used to create docker image 
2] send_tweets_to_telegram.py : The python script which likes users mentioned in users.yml file..like their tweets and publish them to telegram
3] users.yml: Contains user list to work with
4] config.py: which has all the tokens
              access_token_secret=
              access_consumer_secret=
              consumer_key=
              consumer_secret=
              token=

Running the BOT
docker build -t telebot .
docker run telebot

