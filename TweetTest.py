# import tweepy
import tweepy as tw

# your Twitter API key and API secret
access_token = "1551145058258153473-utDfnXHO0FX3N1RYKP57AeldcDXZSm"
access_token_secret = "bOqz0kjpCnhtiRkpYPzVVGwiiZJnQfYMu8z2rbqecPPYh"

my_api_key = "euNAFXf1a4shi829O9DKt7DYS"
my_api_secret = "sZAEQi4SvFZ9DgUqtRJuay6THNNy6fpLPUVlKE8P47xjs6j37Y"

# authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)
