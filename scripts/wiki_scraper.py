"""
beautifulsoup4 scraper.py

usage: 
+ $python scraper.py # must add code to specify output
+ as third party module in conjunction with parser.py
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# avoid 403 response (or use WikiMedia API)
header = {'User-Agent': 'Mozilla/5.0'}

# create variable with url to target page
url = 'https://en.wikipedia.org/wiki/RuPaul%27s_Drag_Race_(season_5)' 

# scrape html at url
r = requests.get(url)

# turn the html into a beautifulsoup object
soup = BeautifulSoup(r.text, 'lxml')

