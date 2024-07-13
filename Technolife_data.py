import requests
import pandas as pd
from bs4 import BeautifulSoup

def Technolife():
    url = "https://www.technolife.ir/product/list/164_163_130/%D8%AA%D9%85%D8%A7%D9%85%DB%8C-%DA%A9%D8%A7%D9%85%D9%BE%DB%8C%D9%88%D8%AA%D8%B1%D9%87%D8%A7-%D9%88-%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D9%87%D8%A7?only_available=true&manufacturer_id=19&pto=20000000&pfrom=0"
    response = requests.get(url)

    soup = BeautifulSoup(response.content,"html.parser")

    sections = soup.find_all("section",class_="relative w-full rounded-[10px] bg-white pt-[52px] xl:max-w-[32%] 2xl:w-[24%] 3xl:w-[19.2%] border shadow-[0px_1px_4px_rgba(0,0,0,0.08)]")

    names=[]
    prices=[]
    for section in sections:
        name = section.find("h2",class_="yekanbakh-en line-clamp-3 h-[75px] overflow-hidden text-sm font-medium leading-6.5 -tracking-0.5 text-gray-800")
        price = section.find("p",class_="text-[22px] font-semiBold leading-5 text-gray-800")
        
        names.append(name.text)
        try :
            prices.append(price.text)
        except:
            prices.append(section.find("p",class_="text-[22px] font-semiBold leading-5 text-red-600").text)
            
    data = {"name":names,"price":prices}
    dataframe= pd.DataFrame(data)
    return dataframe
