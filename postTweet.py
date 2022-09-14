
import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN,
                       consumer_key=config.API_KEY,
                       consumer_secret=config.API_KEY_SECRET,
                       access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_TOKEN_SECRET)

# Replace the text with whatever you want to Tweet about
tweet_post = client.create_tweet(text='hello1')

print(tweet_post)
