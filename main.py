import tweepy
from twitter_api_key import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

status_id = 1359804116713631747

try:
    # delete tweet
    api.destroy_status(status_id)
except:
    print("error")
