#Adapted from https://hackernoon.com/scraping-yahoo-finance-data-using-python-ayu3zyl


"""
Links
Crypto - https://in.finance.yahoo.com/cryptocurrencies
Indices - https://in.finance.yahoo.com/world-indices
Mutual Funds - https://in.finance.yahoo.com/mutualfunds
Gainers - https://in.finance.yahoo.com/gainers
Losers - https://in.finance.yahoo.com/losers
"""

import requests 
from bs4 import BeautifulSoup
import csv 
import pandas as pd 


prices=[]
names=[]
changes=[]
percentChanges=[]
marketCaps=[]
totalVolumes=[]
circulatingSupplys=[]
 
CryptoCurrenciesUrl = "https://in.finance.yahoo.com/world-indices"
r= requests.get(CryptoCurrenciesUrl)
data=r.text
soup=BeautifulSoup(data, features="html.parser")


counter = 40
for i in range(40, 404, 14):
   for row in soup.find_all('tbody'):
      for srow in row.find_all('tr'):
         for name in srow.find_all('td', attrs={'class':'data-col1'}):
            names.append(name.text)
         for price in srow.find_all('td', attrs={'class':'data-col2'}):
            prices.append(price.text)
         for change in srow.find_all('td', attrs={'class':'data-col3'}):
            changes.append(change.text)
         for percentChange in srow.find_all('td', attrs={'class':'data-col4'}):
            percentChanges.append(percentChange.text)

            df = pd.DataFrame({"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges})

""""
for listing in soup.find_all('tr', attrs={'class':'SimpleDataTableRow'}):
   for name in listing.find_all('td', attrs={'aria-label':'Name'}):
      names.append(name.text)
   for price in listing.find_all('td', attrs={'aria-label':'Price (intraday)'}):
      prices.append(price.find('span').text)
   for change in listing.find_all('td', attrs={'aria-label':'Change'}):
      changes.append(change.text)
   for percentChange in listing.find_all('td', attrs={'aria-label':'% change'}):
      percentChanges.append(percentChange.text)
   for marketCap in listing.find_all('td', attrs={'aria-label':'Market cap'}):
      marketCaps.append(marketCap.text)
   for totalVolume in listing.find_all('td', attrs={'aria-label':'Avg vol (3-month)'}):
      totalVolumes.append(totalVolume.text)
   for circulatingSupply in listing.find_all('td', attrs={'aria-label':'Volume'}):
      circulatingSupplys.append(circulatingSupply.text)
 
df = pd.DataFrame({"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges, "Market Cap": marketCaps, "Average Volume": totalVolumes,"Volume":circulatingSupplys})
"""
"""
   #For Cryptos
for listing in soup.find_all('tr', attrs={'class':'SimpleDataTableRow'}):
   for name in listing.find_all('td', attrs={'aria-label':'Name'}):
      names.append(name.text)
   for price in listing.find_all('td', attrs={'aria-label':'Price (intraday)'}):
      prices.append(price.find('span').text)
   for change in listing.find_all('td', attrs={'aria-label':'Change'}):
      changes.append(change.text)
   for percentChange in listing.find_all('td', attrs={'aria-label':'% change'}):
      percentChanges.append(percentChange.text)
   for marketCap in listing.find_all('td', attrs={'aria-label':'Market cap'}):
      marketCaps.append(marketCap.text)
   for totalVolume in listing.find_all('td', attrs={'aria-label':'Total volume all currencies (24 hrs)'}):
      totalVolumes.append(totalVolume.text)
   for circulatingSupply in listing.find_all('td', attrs={'aria-label':'Circulating supply'}):
      circulatingSupplys.append(circulatingSupply.text)

df = pd.DataFrame({"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges})
"""

""" World Indices

            """
 


print(df)