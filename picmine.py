
import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages')
import tweepy
import requests
auth = tweepy.OAuthHandler("PsazOZ7UXJRNqhjSg677VPQ9j", "W0aPNz7QCZdWFFpCJhEfW3Z5m0wxtAstKJHZtxdKpfYjr20PBC")
auth.set_access_token("3635072542-Kus6Ks2pniRZMY45Us1PePKNtZfO2sI8mjh5Lvi", "LcZKfw9jA0YkOKnkvOWZKa8N9OmbK68rjXGkadgIgNGe5")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets: 
   for media in tweet.entities.get("media",[{}]):
      print media
      #checks if there is any media-entity
      if media.get("type",None) == "photo":
          # checks if the entity is of the type "photo"
          image_content=requests.get(media["media_url"])
          #print "IMG123"
          #print image_content

         # tweet.entities["media"]["media_url"]
