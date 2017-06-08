"""
beautiful soup 4 scraper.py

usage: $python scraper.py

# todo: 
# 1. adjust encoding at write to save useful tags for parsing
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://rupaulsdragrace.wikia.com/wiki/RuPaul%27s_Drag_Race_(Season_5)' 

# scrape the html at the url
r = requests.get(url)

# turn the html into a beautiful soup object
soup = BeautifulSoup(r.text, 'lxml')

