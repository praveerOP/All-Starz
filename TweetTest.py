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


phone_list=["#Electronics -filter:tweets","#Samsung -filter:tweets","#Xiaomi -filter:tweets",
"#MiNote -filter:tweets"]#VIVO -filter:tweets"]
for i in phone_list:
    search_query = "#iPhone"
# get tweets from the API
    tweets = tw.Cursor(api.search_tweets,
                q=search_query,
                lang="en",
                since="2020-09-16").items(50)

# store the API responses in a list

    tweets_copy = []
    for tweet in tweets:
        tweets_copy.append(tweet)
    
print("Total Tweets fetched:", len(tweets_copy))
import pandas as pd

# intialize the dataframe
tweets_df = pd.DataFrame()

# populate the dataframe
for tweet in tweets_copy:
    hashtags = []
    try:
        for hashtag in tweet.entities["hashtags"]:
            hashtags.append(hashtag["text"])
        text = api.get_status(id=tweet.id, tweet_mode='extended').full_text
    except:
        pass
    tweets_df = tweets_df.append(pd.DataFrame({
                                               'hashtags': [hashtags if hashtags else None]
                                               }))
    tweets_df = tweets_df.reset_index(drop=True)

# show the dataframe
# print(tweets_df)
print(tweets_df.head())
tweets_list = []
print("test ",tweets_df.values[0])
# for i in tweets_df.values[0]:
#     print(tweets_list.extend(i[0]))
# tweets_list = list(set(tweets_list))
# # # tweet_lis=tweets_df.values.tolist()
# print (tweets_list)