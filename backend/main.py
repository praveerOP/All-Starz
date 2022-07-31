from typing import Union
from fastapi import FastAPI
from fuzzywuzzy import process
import re
from Flipkart.flipkartdata import flipkart
from Twitter.TweetTest import twitter

tweets = []
tweets_dict, tweets_desc = twitter()#get twitter data
data = flipkart()#get flipkart data

names_match = []
for i in data["Product_name"]:
  names_match.append(re.sub("[\(\[].*?[\)\]]", "", i))
print(names_match, len(names_match))
print("Tweets_desc: ", tweets_desc)
str2Match = "|".join(tweets_desc)
print("Str2match",str2Match)
strOptions = names_match
Ratios = process.extract(str2Match,strOptions)
print("Ratios : ",Ratios)

#Matching twitter trends with flipkart data
strOptions = names_match
matched_entries = []
for name in str2Match:
   Ratios = process.extract(name,strOptions, limit = 1)
   matched_entries.append(Ratios)
# print(matched_entries)

#Calculating most frequent product trends and storing sorted results in non ascending order
matched_dict = {}
for i in matched_entries:
  if(i[0][0]in matched_dict):
    matched_dict[i[0][0]] += i[0][1] 
  else:
    matched_dict[i[0][0]] = i[0][1] 
item_dict = dict(sorted(matched_dict.items(), key=lambda item: item[1], reverse = True))
# print(item_dict)

#Creating endpoints to access different product categories 
app = FastAPI()
@app.get("/smartphones")
def read_root():
    return {"Smartphones":item_dict }

