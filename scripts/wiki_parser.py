"""
beautifulsoup4 parser.py

scrape outcomes table for RPDR visualization project:
 + select table by position
 + assign table data to variables
 + make dataframe from combined variables
 + save dataframe to CSV

nicholas chung, 2017
nich.chung@gmail.com
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# select scraper and import data
from wiki_scraper import soup

# create variables to store scraped data
contestant = []
ep_1 = []
ep_2 = []
ep_3 = []
ep_4 = []
ep_5 = []
ep_6 = []
ep_7 = []
ep_8 = []
ep_9 = []
ep_10 = []
ep_11 = []
ep_12 = []
ep_14 = []


# create object from [third] table
table = soup('table')[2]

# find all <tr> tag pairs; skip first one (table header)
for row in table.find_all('tr')[1:]:
    
    # create variable for each <td> pair 
    col = row.find_all('td')

    # create variable of string inside first <td> pair
    column_1 = col[0].text.strip()
    # append variable to 'contestant' 
    contestant.append(column_1)
    
    # create variable of string inside second <td> pair
    column_2 = col[1].text.strip()
    # append variable to 'ep_1' 
    ep_1.append(column_2)
    
    # create variable of string inside third <td> pair
    column_3 = col[2].text.strip()
    # append variable to 'ep_2' 
    ep_2.append(column_3)
    
    # create variable of string inside fourth <td> pair
    column_4 = col[3].text.strip()
    # append variable to 'ep_3' 
    ep_3.append(column_4)
    
    # create variable of string inside fifth <td> pair
    column_5 = col[4].text.strip()
    # append variable to 'ep_4' 
    ep_4.append(column_5)
    
    # create variable of string inside sixth <td> pair
    column_6 = col[5].text.strip()
    # append variable to 'ep_5' 
    ep_5.append(column_6)
    
    # create variable of string inside seventh <td> pair
    column_7 = col[6].text.strip()
    # append variable to 'ep_6' 
    ep_6.append(column_7)
    
    # create variable of string inside eight <td> pair
    column_8 = col[7].text.strip()
    # append variable to 'ep_7' 
    ep_7.append(column_8)

    # create variable of string inside ninth <td> pair
    column_9 = col[8].text.strip()
    # append variable to 'ep_8' 
    ep_8.append(column_9)

    # create variable of string inside tenth <td> pair
    column_10 = col[9].text.strip()
    # append variable to 'ep_9' 
    ep_9.append(column_10)

    # create variable of string inside eleventh <td> pair
    column_11 = col[10].text.strip()
    # append variable to 'ep_10' 
    ep_10.append(column_11)

    # create variable of string inside twelfth <td> pair
    column_12 = col[11].text.strip()
    # append variable to 'ep_11' 
    ep_11.append(column_12)

    # create variable of string inside thirteenth <td> pair
    column_13 = col[12].text.strip()
    # append variable to 'ep_12'
    ep_12.append(column_13)

    # create variable of string inside fourteenth <td> pair
    column_15 = col[14].text.strip()
    # append variable to 'ep_12' 
    ep_14.append(column_14)


# create variable of value of columns
columns = {'contestant': contestant, 'ep_1': ep_1, 'ep_2': ep_2, 'ep_3': ep_3, 'ep_4': ep_4, 'ep_5': ep_5, 'ep_6': ep_6, 'ep_7': ep_7, 'ep_8': ep_8, 'ep_9': ep_9, 'ep_10': ep_10, 'ep_11': ep_11, 'ep_12': ep_12, 'ep_14': ep_14}

# create dataframe from 'columns' variable with 'from_dict' to account for arrays with different n
results = pd.DataFrame.from_dict(columns, orient='index')
# flip dataframe axes
results = results.transpose()
# reset column order
results = results[['contestant', 'ep_1', 'ep_2', 'ep_3', 'ep_4', 'ep_5', 'ep_6', 'ep_7', 'ep_8', 'ep_9', 'ep_10', 'ep_11', 'ep_12', 'ep_14']]


# save to CSV
results.to_csv('../data/results.csv')
