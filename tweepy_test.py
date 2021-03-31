import tweepy
import schedule
import time

consumer_key = 
consumer_secret = 

key = 
secret = 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

f = open("twinkle.txt", "r")

word_list = []

for line in f.readlines():
	words = line.split(" ")
	for word in words:
		if word[-1] == "\n":
			word = word[:-1]
		
		word_list.append(word)

def word_tweeter():
	api.update_status(word_list[0])
	word_list.pop(0)

try:
	schedule.every(1).minutes.do(word_tweeter)

	while True:
		schedule.run_pending()
		time.sleep(1)
except:
	print("Complete")


#api.update_status("Test2")


#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)
