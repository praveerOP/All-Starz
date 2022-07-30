# import tweepy
import tweepy as tw
import pandas as pd

def twitter():
    # your Twitter API key and API secret
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
    "#asus","#lenovo","#hp","#"]
    for i in phone_list:
        search_query = i
    # get tweets from the API
        tweets = tw.Cursor(api.search_tweets,
                    q=search_query,
                    lang="en",
                    since="2020-09-16").items(10)

    # store the API responses in a list

        
        for tweet in tweets:
            tweets_copy.append(tweet)
        
    print("Total Tweets fetched:", len(tweets_copy))
    # intialize the dataframe
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
                                                'user_description': tweet.user.description,
                                                'hashtags': [hashtags if hashtags else None]
                                                }))
        # tweets_df = tweets_df.reset_index(drop=True)
    # show the dataframe
    # print(tweets_df)
    print(tweets_df.head())
    tweets_list = tweets_df['hashtags'].tolist()
    tweets_desc = tweets_df['user_description'].tolist()
    tweets_newlist = []
    for k in tweets_list:
        if k != None:
            tweets_newlist.extend(k)

    # for i in tweets_df['hashtags']:
    #     if i[0]!=None:
    #         tweets_list.extend(i[0])
    frequency={}
    for item in tweets_newlist:
        # checking the element in dictionary
        if item in frequency:
        # incrementing the counr
            frequency[item] += 1
        else:
        # initializing the count
            frequency[item] = 1
    # printing the frequency
    #print (tweets_list)
    frequency=dict(sorted(frequency.items(), key=lambda item: item[1],reverse=True))
    print(frequency)
    # return frequency
    #possible extractable feature 
    # fet=[]
    # possible_list=["Samsung Galaxy","Oppo"]
    # tweet_list=[]
    # print(tweets_desc)
    # print("-----------------------------------------")
    # print("-----------------------------------------")
    print(tweets_newlist)
    given_list=['realme C11 2021 (Cool Grey, 64 GB)', 'realme C11 2021 (Cool Grey, 32 GB)', 
    'SAMSUNG Galaxy F22 (Denim Black, 64 GB)', 'SAMSUNG Galaxy F22 (Denim Blue, 64 GB)', 'realme C31 (Dark Green, 32 GB)', 
    'realme C31 (Light Silver, 32 GB)', 'POCO C31 (Royal Blue, 64 GB)', 'realme C31 (Dark Green, 64 GB)', 
    'Infinix HOT 12 Play (Racing Black, 64 GB)', 'Infinix HOT 12 Play (Horizon Blue, 64 GB)', 'Infinix HOT 12 Play (Daylight Green, 64 GB)', 
    'realme C31 (Light Silver, 64 GB)', 'POCO C31 (Royal Blue, 32 GB)', 'realme C11 2021 (Cool Blue, 32 GB)', 
    'POCO C31 (Shadow Gray, 64 GB)', 'realme 9 (Sunburst Gold, 128 GB)', 'Infinix Note 12 (Jewel Blue, 64 GB)', 
    'Infinix Hot 11 2022 (Sunset Gold, 64 GB)', 'SAMSUNG Galaxy F13 (Waterfall Blue, 64 GB)', 
    'SAMSUNG Galaxy F13 (Sunrise Copper, 64 GB)', 'realme C20 (Cool Grey, 32 GB)', 'Infinix Note 12 (Force Black, 64 GB)', 
    'POCO M4 Pro (Power Black, 64 GB)', 'realme 9 (Stargaze White, 128 GB)', 'OPPO K10 (Black Carbon, 128 GB)', 
    'REDMI 9i Sport (Coral Green, 64 GB)', 'OPPO K10 (Blue Flame, 128 GB)', 'realme C20 (Cool Blue, 32 GB)', 
    'SAMSUNG Galaxy F13 (Nightsky Green, 64 GB)', 'vivo T1X (Space Blue, 128 GB)', 'vivo T1X (Gravity Black, 64 GB)', 
    'vivo T1X (Space Blue, 128 GB)', 'vivo T1X (Gravity Black, 128 GB)', 'REDMI 10 (Pacific Blue, 64 GB)',
     'REDMI 10 (Midnight Black, 64 GB)', 'MOTOROLA g31 (Baby Blue, 64 GB)', 'REDMI 9i Sport (Carbon Black, 64 GB)', 
     'POCO M4 Pro (Cool Blue, 64 GB)', 'REDMI Note 10 Pro (Vintage Bronze, 128 GB)', 'vivo T1X (Space Blue, 64 GB)', 
     'realme C21Y (Cross Black, 64 GB)', 'REDMI Note 10T 5G (Metallic Blue, 64 GB)', 'Infinix Hot 11 2022 (Aurora Green, 64 GB)', 
     'OPPO Reno8 5G (Shimmer Gold, 128 GB)', 'OPPO Reno8 5G (Shimmer Black, 128 GB)', 'realme 9 (Stargaze White, 128 GB)', 
     'REDMI Note 10 Pro (Dark Night, 128 GB)', 'POCO M4 5G (Power Black, 64 GB)']    

twitter();

