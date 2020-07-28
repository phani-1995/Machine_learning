import tweepy
from textblob import TextBlob
from tweepy import OAuthHandler
import matplotlib.pyplot as plt
ckey = ***********************************
csecret = **********************************
atoken = **********************************
asecret = ***********************************

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)


api = tweepy.API(auth)
tweets =  api.search('MODI')

for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment[0]>0:
        print("positive")
    else:
        print("Negative")

