# This file only needs to be ran once every time your list of accounts your watching gets
#   updated so that your following all those accounts, if thats your thing. 
# Import Tweepy, sleep, credentials.py
import tweepy
from time import sleep
from credentials import *
from numpy import genfromtxt

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

my_file = open('nasatwitteraccounts.csv', 'r') 
usernames = my_file.readlines()
my_file.close()

i = 0

for line in usernames:
    user = api.get_user('@'+usernames[i])
    i = i + 1
    user.follow()
    sleep(10)
