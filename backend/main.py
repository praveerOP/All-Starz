from typing import Union
from fastapi import FastAPI 
from Twitter.TweetTest import twitter
tweets = []
tweets_dict = twitter()
# for i in tweets_df:
#     print(i)
# print(tweets_df.head())
# print(tweets_df)
app = FastAPI()
@app.get("/")
def read_root():
    return {"Smartphones":tweets_dict }


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}