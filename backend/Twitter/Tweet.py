import tweepy
#Accessing twitter api
access_token = "1551145058258153473-utDfnXHO0FX3N1RYKP57AeldcDXZSm"
access_token_secret = "bOqz0kjpCnhtiRkpYPzVVGwiiZJnQfYMu8z2rbqecPPYh"

api_key = "euNAFXf1a4shi829O9DKt7DYS"
api_key_secret = "sZAEQi4SvFZ9DgUqtRJuay6THNNy6fpLPUVlKE8P47xjs6j37Y"

auth = tweepy.OAuthHandler(consumer_key= api_key, consumer_secret= api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print(api)

#Location access
india_woeid = 23424848

trend_result = api.get_place_trends(india_woeid)

try:

    for trend in trend_result[0]["trends"][:50]:
        print(trend["name"])
        print(trend["tweet_volume"])

except:
    print("Error")


