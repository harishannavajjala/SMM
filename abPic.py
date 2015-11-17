import tweepy
#import csv
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener, Stream, json
from tweepy import Stream
import requests

def definition():
    global tweetline
 


access_token = "118330101-3fV9CEDtE5zJdLtAWMc8F8j1x79yRuQbgw1jV3Ne"
access_token_secret = "oWRsuWKpfANHbKXzGDQclV0PJBirJV11DLZ21suSdQwWl"
consumer_key = "RRpVayYRM9K0JTVR9lkjbNjrM"
consumer_secret = "h004JaL7O05jBJKrayWWA7Kb10gBr4ANj3vCoOcE4tAXL99u7o"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


class StdOutListener(StreamListener):

    def on_data(self, data):
        #print data
        tweet = json.loads(data)
        print tweet
        #dataset=data.Get()
        for media in tweet.get("media",[{}]):
                #print "found"
                #print media
                #checks if there is any media-entity
                if media.get("type",None) == "photo":
                    # checks if the entity is of the type "photo"
                    image_content=requests.get(media["media_url"])
                    print "image found"
                    print image_content
        print "returned true"
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    
    print "before filter"
    #This line filter Twitter Streams to capture data by the keywords: "#happy", "#sad", "#disgusted", "#fearful", "#angry", "#surprised", "#scared"
    stream.filter(track=["#biryani", "#burger", "#taco", "#pizza", "#pasta", "#dosa", "#sushi"])
    print"done"
    

# single_tweet = '@Harish09306 - another test tweet using tweepy'
# api.update_status(status=single_tweet)
print "updated"