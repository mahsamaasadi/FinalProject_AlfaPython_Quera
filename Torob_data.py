import requests
import pandas as pd
from bs4 import BeautifulSoup

def Torob():
    url= "https://torob.com/browse/99/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D9%88-%D9%86%D9%88%D8%AA-%D8%A8%D9%88%DA%A9-laptop/b/29/asus-%D8%A7%DB%8C%D8%B3%D9%88%D8%B3/?price__gt=10000000&price__lt=20000000&stock_status=new&available=true"
    response = requests.get(url)

    soup = BeautifulSoup(response.text,"html.parser")

    names_html = soup.find_all("h2",class_="jsx-9e6201846c11ef54 product-name")
    prices_html = soup.find_all("div",class_="jsx-9e6201846c11ef54 product-price-text")

    names=[]
    for name in names_html:
        names.append(name.text)
    
    prices=[]
    for price in prices_html:
        prices.append(price.text)

    data = {"name":names,"price":prices}
    dataframe=pd.DataFrame(data)

    return dataframe
