import time
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

# make variables that point to the finviz screener stocks
base_url = 'https://finviz.com/screener.ashx?v=152&s=ta_mostvolatile&o=price'
result = requests.get(base_url)
src = result.content
soup = BeautifulSoup(src, 'html.parser')
plane = soup.find("div", {'id':"screener.content"})
table = plane.find("tr", {'class': "table-dark-row-cp"})
stock = table.find("a", {'class': "screener-link-primary"})
# make a variable that links to the overview of each stock
