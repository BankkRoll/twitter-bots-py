import tweepy
from time import sleep
import os


access_token_secret = os.environ['access_token_secret']
access_token = os.environ['access_token']
consumer_secret = os.environ['consumer_secret']
consumer_key = os.environ['consumer_key']


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


print("Follow everyone a user follows. Bankkroll.eth")


target_screen_name = api.get_user(screen_name='@bankkroll_eth')

while True:
    try:

        for follower in target_screen_name.friends():
            if not follower.protected:
                if not follower.following:
                    api.create_friendship(screen_name = follower.screen_name)
                    print(follower.screen_name + ' was just followed by @' + target_screen_name.screen_name)
                    target_screen_name = follower
                    sleep(320)
    except tweepy.errors.TweepyException as e:
        print(e)
