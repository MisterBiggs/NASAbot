# This file only needs to be ran once every time your list of accounts your watching gets
#   updated so that your following all those accounts, if thats your thing. 
# Import Tweepy, sleep, credentials.py
from time import sleep

import tweepy
from numpy import genfromtxt

from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

my_file = open('nasatwitteraccounts.csv', 'r') 
usernames = my_file.readlines()
my_file.close()

i = 1

for line in usernames:
    user = api.get_user(usernames[i])
    i = i + 1
    if user.following == False:
        user.follow()
        print('@'+ usernames[i] +' Followed!')
        sleep(61)
    else:
        print('You were already following @'+ usernames[i])
        sleep(61)
