import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import requests
from operator import index

def flipkart():
    pro_name = []
    pro_price = []
    pro_link = []
    class_list = set()
    page_num = input("Enter number of pages")
    for i in range (1, int(page_num)+1):
        url = "https://www.flipkart.com/search?q=mobiles&page=" +str(i)
        req = requests.get(url)
        content = BeautifulSoup(req.content, 'html.parser')
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
    return data
# flipkart()