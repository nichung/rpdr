"""
beautiful soup 4 scraper.py

usage: $python scraper.py [url]

# todo: 
# 1. adjust encoding at write to save useful tags for parsing
# 2. pass output file as parameter with argv such that 
#    $python scraper.py [output] [url]
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sys import argv

# open output file
scraped_data = open("scrape_data.txt", "w")

# unpack argv and assign to variables
script, url = argv

# scrape the html at the url
r = requests.get(url)

# turn the html into a beautiful soup object
soup = BeautifulSoup(r.text, 'lxml')

# get all text from the html
just_text = soup.get_text()

# write values to output file
scraped_data.write(just_text.encode('utf-8'))

# close output file
scraped_data.close()
# print soup
