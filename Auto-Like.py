import tweepy
import time
from time import sleep

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


while True:

    for tweet in tweepy.Cursor(api.search_tweets, q='INPUT-WORD-HERE-TO-MONITOR').items():
        try:
            print('\nTweet by: @' + tweet.user.screen_name)
            print(tweet.text)

        # check that bot has not already favorited the tweet
        # Favorite the tweet
            if not tweet.favorited:
                tweet.favorite()
                print('Liked')
                sleep(240)


        except tweepy.errors.TweepyException as e:
            print(e)
