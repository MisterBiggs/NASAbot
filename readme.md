
# Retweeting Bot

## Table of Contents
<li><a href="#Usage Instructions">Usage Instructions</a></li>

## Usage Instructions

Below are detailed instructions on how to use the Retweeting bot

### Ignored Files

[credentials.py](./credentials.py) is not included in the git repository because it contains secret keys. This file will have to be editied to include your own keys from the Twitter Developer website.

```python
consumer_key = 'Blah'
consumer_secret = 'BlahBlah'
access_token = 'BlahBlahBlah'
access_token_secret = 'BlahBlahBlahBlah'
```
### List of accounts to monitor

The default configuration is setup to follow all of NASA's official twitter accounts and to retweet anything that they tweet. So to have similar functionality you would have to create a .csv file with only the names of the accounts you wish to follow/retweet without the '@' symbol like below.

```csv
NASAKennedy
NASA_Langley
NASA_Marshall
```

## Resources Used

Below are all the resources used in order to make this project.

### Digital Ocean Guides

[How to install python3](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-16-04-server)

[How to create a twitter app](https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app)

[Python3 tweepy library](https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library)

### Other Resources

[Regex](https://regex101.com/r/g61Gax/2)

[Twitter Developer](https://developer.twitter.com/)

[Tweepy Documentation](http://docs.tweepy.org/en/v3.5.0/)


