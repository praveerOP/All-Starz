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
    print(tweets_desc)
    # print("-----------------------------------------")
    # print("-----------------------------------------")
    print(tweets_newlist)
    '''given_list=['realme C11 2021 ', 'realme C11 2021 ', 
    'SAMSUNG Galaxy F22 ', 'SAMSUNG Galaxy F22 ', 'realme C31 ', 'realme C31 ', 'POCO C31 ', 'realme C31 ', 
    'Infinix HOT 12 Play ', 'Infinix HOT 12 Play ', 'Infinix HOT 12 Play ', 'realme C31 ', 'POCO C31 ', 'realme C11 2021 ', 
    'POCO C31 ', 'realme 9', 'Infinix Note 12 ', 'Infinix Hot 11 2022 ', 'SAMSUNG Galaxy F13 ', 
    'SAMSUNG Galaxy F13 ', 'realme C20 ', 'Infinix Note 12 ', 'POCO M4 Pro ', 'realme 9 ', 'OPPO K10 ', 
    'REDMI 9i Sport ', 'realme C20', 'SAMSUNG Galaxy F13 ', 'vivo T1X ', 'vivo T1X ', 
    'vivo T1X ', 'vivo T1X ', 'REDMI 10 ','REDMI 10 ', 'MOTOROLA g31 ', 'REDMI 9i Sport ', 'POCO M4 Pro ',
    'REDMI Note 10 Pro ', 'vivo T1X ', 'realme C21Y ', 'REDMI Note 10T 5G ',
    'Infinix Hot 11 2022 ', 'OPPO Reno8 5G ', 'OPPO Reno8 5G ', 'realme 9 ', 'REDMI Note 10 Pro ', 'POCO M4 5G ']
    '''

   

    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import urllib.request
    # from IPython.display import HTML
    from operator import index

    pro_name = []
    pro_price = []
    pro_link = []
    class_list = set()
    page_num = input("Enter number of pages")
    for i in range (1, int(page_num)+1):
        url = "https://www.flipkart.com/search?q=mobiles&page=" +str(i)
        req = requests.get(url)
        content = BeautifulSoup(req.content, 'html.parser')
        # # get all tags
        # tags = {tag.name for tag in content.find_all()}
    
        # # iterate all tags
        # for tag in tags:
        #   # find all element of tag
        #   for i in content.find_all( tag ):
    
        #       # if tag has attribute of class
        #       if i.has_attr( "class" ):
    
        #           if len( i['class'] ) != 0:
        #               class_list.add(" ".join( i['class']))
    
        #   print( class_list )
        product_name = content.find_all('div', {"class" :"_4rR01T"})
        product_price = content.find_all('div', {"class" : "_30jeq3 _1_WHN1"})
        product_rating = content.find_all('div', {"class" : ""})
        link = content.find_all('a', {"class" : "_1fQZEK"})
        for tag in link:
        pro_link.append("https://www.flipkart.com"+tag['href'])

        for i in product_name:
        pro_name.append(i.text)
        for i in product_price:
        pro_price.append(i.text)

    data = ({"Product_name" : pro_name, "Product_price" : pro_price, "Product_link" : pro_link})
    df = pd.DataFrame.from_dict(data, orient= "index")
    df = df.transpose()
    def make_clickable(data):
        return f'<a target="_blank" href="{data}">{data}</a>'

    df.style.format({'Product_link': make_clickable})
    

twitter();

