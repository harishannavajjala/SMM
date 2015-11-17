import tweepy
auth = tweepy.OAuthHandler("PsazOZ7UXJRNqhjSg677VPQ9j", "W0aPNz7QCZdWFFpCJhEfW3Z5m0wxtAstKJHZtxdKpfYjr20PBC")
auth.set_access_token("3635072542-Kus6Ks2pniRZMY45Us1PePKNtZfO2sI8mjh5Lvi", "LcZKfw9jA0YkOKnkvOWZKa8N9OmbK68rjXGkadgIgNGe5")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print "TWEET123 "+tweet.text


