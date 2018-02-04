# Import Tweepy, sleep, credentials.py
import tweepy
from time import sleep
from credentials import *
from numpy import genfromtxt
import json

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())

my_file = open('nasatwitteraccounts.csv', 'r') 
usernames = my_file.readlines()
my_file.close()
i = 55

for line in usernames:

    data = api.user_timeline(id = line,count=1,page=1)
    # json.dumps(data)
    # with open('cache/json/'+usernames[i] + '.json','w') as outfile:
    #     json.dump(data, outfile)
    for tweet_id in data:
        # if tweet_id['retweeted'] in ['False']
            # if tweet_id['lang'] in ["en"]
                print(line)
                print(tweet_id['id_str'])
                print(tweet_id['text'])
                print(i)
                print('retweeted')
                api.retweet(tweet_id['id_str'])

    i += 1
    sleep(10)

# Check if we have already retweeted "retweeted": false
# Check for "lang": "en"
