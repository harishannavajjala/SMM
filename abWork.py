import tweepy
import pprint
import mechanize
import os
from BeautifulSoup import BeautifulSoup
import urllib


from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener,Stream,json
from tweepy import Stream
import requests



access_token = "3635072542-Kus6Ks2pniRZMY45Us1PePKNtZfO2sI8mjh5Lvi"
access_token_secret = "LcZKfw9jA0YkOKnkvOWZKa8N9OmbK68rjXGkadgIgNGe5"
consumer_key = "PsazOZ7UXJRNqhjSg677VPQ9j"
consumer_secret = "W0aPNz7QCZdWFFpCJhEfW3Z5m0wxtAstKJHZtxdKpfYjr20PBC"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


class StdOutListener(StreamListener):
    imgcount=0

    def on_data(self, data):

        tweet = json.loads(data)
        if u'entities' in tweet:
            if u'media' in tweet[u'entities']:
                 if  u'media_url' in tweet[u'entities'][u'media'][0]:
                     #print tweet[u'text']
                     url = tweet[u'entities'][u'media'][0][u'media_url']
                     #print url
                     khaana = "khaana"
                     if "#pizza" in tweet[u'text']:
                         #print "HEYYYYYY....ITSS A pIZZA"
                         khaana = "pizza"
                     self.imgcount=self.imgcount+1
                     #print self.imgcount
                     name=khaana+str(self.imgcount)+".jpg"
                     print name
                     urllib.urlretrieve(url, name)
        return True


    def on_error(self, status):
        print status


if __name__ == '__main__':


    #This handles Twitter authetification and the connection to Twitter Streaming API
    listener1 = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener1)

    #This line filter Twitter Streams to capture data by the keywords: "#happy", "#sad", "#disgusted", "#fearful", "#angry", "#surprised", "#scared"
    print "before filter"
    stream.filter(track=["#biryani", "#burger", "#taco", "#pizza", "#pasta", "#dosa", "#sushi"])

# api.update_status(status=single_tweet)
print "updated"

