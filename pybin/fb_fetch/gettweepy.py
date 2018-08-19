import tweepy
import io
import sys
import json

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
consumer_key = '5xkVhGal96k1EXRyV9JeZmFCi'
consumer_secret = 'Cut5G4hkMnRbbZhLKtN5BY1txU9pQnP3VtfXZapvngdjeeKyps'
access_token = '991152905154510853-pPDAVrnIZm6qU34vvWuca2HsATwLc7V'
access_token_secret = '0n6Ul2oWix2a4HT04poQvbcVYI6CM4nNVSzcSt79Z4RnW'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
auth.set_access_token(access_token, access_token_secret)

# tweets = api.search(q="#白猫", lang="en", count=10, tweet_mode="extended")
# mystream = tweepy.Stream(auth = api.auth,tweet_mode = 'extended')
user = api.get_user(screen_name = 'naturefour')
uid = user.id
public_tweets = api.user_timeline(user.id,count = 5, include_rts = False,tweet_mode='extended')
#print(user.id,user.followers_count,user.name,user.location)
def getUserId():
	return uid
#print("it is user id :",getUserId())

def getPT():
	return public_tweets

def from_public_to_dict(cid, personal_tweets):
	arr = []
	#print(cid, personal_tweets)
	for extended_tweet in personal_tweets:
		tweet = {}
		tweet["cid"] = cid
		tweet["text_id"] = extended_tweet.id
		tweet["content"] = extended_tweet.full_text
		tweet["created_at"] = str(extended_tweet.created_at)
		#print(extended_tweet.full_text, "\n", extended_tweet.created_at, "\n", 			extended_tweet.id, "\n")  # ,extended_tweet.entities.hashtags.text
		#print(tweet)
		arr.append(tweet)
	return arr

#some = from_public_to_dict(getUserId(), getPT())
#print(some)
