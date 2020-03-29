import time
import requests
from bs4 import beautifulsoup

result = requests.get("https://finviz.com/screener.ashx?v=111&s=ta_mostvolatile&f=geo_usa")
soup = BeautifulSoup(req.content, 'html.parser')
