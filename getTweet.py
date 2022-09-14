import tweepy
import config



# authorization of consumer key and consumer secret
client = tweepy.Client(bearer_token=config.BEARER_TOKEN,
                       consumer_key=config.API_KEY,
                       consumer_secret=config.API_KEY_SECRET,
                       access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_TOKEN_SECRET)

  
# the ID of the status
tweetid = 1570108201693216769
  
tweet = client.get_tweet(tweetid)

tweet_data = tweet.data
print(tweet_data)
  



