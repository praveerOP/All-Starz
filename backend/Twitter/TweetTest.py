# import tweepy
import tweepy as tw
import pandas as pd

def twitter():
    #Twitter API key and API secret
    access_token = "1551145058258153473-utDfnXHO0FX3N1RYKP57AeldcDXZSm"
    access_token_secret = "bOqz0kjpCnhtiRkpYPzVVGwiiZJnQfYMu8z2rbqecPPYh"

    my_api_key = "euNAFXf1a4shi829O9DKt7DYS"
    my_api_secret = "sZAEQi4SvFZ9DgUqtRJuay6THNNy6fpLPUVlKE8P47xjs6j37Y"

    # authenticate
    auth = tw.OAuthHandler(my_api_key, my_api_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    tweets_copy = []
    tweets_df = pd.DataFrame()
    phone_list=["#samsung","#xiaomi","#moto","#vivo","#oppo","#iPhone","#redmi","#apple",
    "#asus","#lenovo"]
    for i in phone_list:
        search_query = i
    # get tweets from the API
        tweets = tw.Cursor(api.search_tweets,
                    q=search_query,
                    lang="en",
                    since="2021-07-01").items(50)

    # store the API responses in a list
        for tweet in tweets:
            tweets_copy.append(tweet)
        
    print("Total Tweets fetched:", len(tweets_copy))
    for tweet in tweets_copy:
        hashtags = []
        try:
            for hashtag in tweet.entities["hashtags"]:
                hashtags.append(hashtag["text"])
            text = api.get_status(id=tweet.id, tweet_mode='extended').full_text
        except:
            pass
        tweets_df = tweets_df.append(pd.DataFrame({
                                                'user_description': tweet.user.description,
                                                'hashtags': [hashtags if hashtags else None]
                                                }))
    print(tweets_df.head())
    tweets_list = tweets_df['hashtags'].tolist()
    tweets_desc = tweets_df['user_description'].tolist()
    tweets_newlist = []
    for k in tweets_list:
        if k != None:
            tweets_newlist.extend(k)
    frequency={}
    for item in tweets_newlist:
        if item in frequency:

            frequency[item] += 1
        else:
            frequency[item] = 1
    frequency=dict(sorted(frequency.items(), key=lambda item: item[1],reverse=True))
    print(frequency)
    print(tweets_desc)
    print(tweets_newlist)  
    return frequency, tweets_desc
# twitter();

