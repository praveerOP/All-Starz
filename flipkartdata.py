import requests
import pandas as pd
import time
from bs4 import BeautifulSoup

product_name = []
product_description = []
description_test = []
product_cost = []
product_rating = []
product_rating_count = []

#Page data
page_num = input("Enter number of pages: ")
for i in range (1, int(page_num)+1):
    web_url = r'https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles%7CMobiles&requestId=37d62a62-dc34-4686-851d-9f369991700a&as-searchtext=mobile&sort=popularity'
    web_pages = page_num

    concat_web_url = web_url + str(web_pages)
    web_url_response = requests.get(concat_web_url)

    if web_url_response.status_code != 200:
        print("Request returned error code: " + str(web_url_response.status_code))
    else:
        soup = BeautifulSoup(web_url_response.content, "html.parser")
        results = soup.find_all("div", class_="_13oc-S")

        for results_value in results:

            result_product_name = results_value.find("div", class_="_4rR01T")
            if result_product_name is None:
                product_name.append("NA")
            else:
                product_name.append(result_product_name.text)
            
            result_product_description=results_value.find("ul", class_="_1xgFaf")
            if result_product_description is None:
                product_description.append("NA")
            else:
                product_description.append(result_product_description.text)
            
            result_product_cost=results_value.find("div", class_="_30jeq3 _1_WHN1")
            if result_product_cost is None:
                product_cost.append("0")    
            else:
                product_cost.append(result_product_cost.text)
            
            result_product_rating=results_value.find("div", class_="_3LWZlK")
            if result_product_rating is None:
                product_rating.append("0")
            else:
                product_rating.append(result_product_rating.text)
            
            result_product_rating_count=results_value.find("span", class_="_2_R_DZ")
            if result_product_rating_count is None:
                product_rating_count.append("0 Ratings & 0 Reviews")
            else:
                product_rating_count.append(result_product_rating_count.text)

    time.sleep(5)

#Storing data in dataframe
    df_data=pd.DataFrame()
    df_data['Product Name'] = product_name
    df_data['Product Description'] = product_description
    df_data['Product Cost'] = product_cost
    df_data['Product Rating'] = product_rating
    df_data['Product Rating and Review Count'] = product_rating_count

    df_data['Product Rating']=df_data['Product Rating'].astype(float)
    df_data['Product Cost']=df_data['Product Cost'].apply(lambda i: i.replace("₹","")) \
                        .apply(lambda i: i.replace(",",""))
    df_data['Product Cost']=df_data['Product Cost'].apply(lambda i: i.strip()).astype(float)

    df_data['Product Rating Count']=df_data['Product Rating and Review Count'].str.split("&").str[0]
    df_data['Product Rating Count']=df_data['Product Rating Count'].apply(lambda i: i.replace("Ratings","")) \
                               .apply(lambda i: i.replace(",",""))
    df_data['Product Rating Count']=df_data['Product Rating Count'].apply(lambda i: i.strip()).astype(int)

    df_data['Product Review Count']=df_data['Product Rating and Review Count'].str.split("&").str[1]
    df_data['Product Review Count']=df_data['Product Review Count'].apply(lambda i: i.replace("Reviews","")) \
                               .apply(lambda i: i.replace(",",""))
    df_data['Product Review Count']=df_data['Product Review Count'].apply(lambda i: i.strip()).astype(int)

    print(df_data)