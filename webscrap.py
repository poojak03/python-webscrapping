# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 18:03:21 2019

@author: pooja.kamble
"""
import pandas as pd
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myurl = "<url of site for scrapping>"

#hit the url
uClient = uReq(myurl)

#All content of web page wil store in page_html variable
page_html = uClient.read()

uClient.close()

#Parse the html variable
page_soup = soup(page_html, 'html.parser')

page_soup.h1

products=[] #List to store name of the product
prices=[] #List to store price of the product
#ratings=[] #List to store rating of the product

for a in page_soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'}) #read the class by name
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    #rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})

	#append in array
    products.append(name.text)
    prices.append(price.text)
    #ratings.append(rating.text)
    
df = pd.DataFrame({'Product Name':products,'Price':prices}) 

#Generate csv file with all product list and price
df.to_csv(r'D:/web-scrapping/products.csv', index=False, encoding='utf-8')