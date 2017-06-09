"""
beautifulsoup4 parser.py

RPDR contestant id scraper 1.0.0

scrape contestant table for RPDR visualization project:
 + select table by position
 + assign table data to variables
 + make dataframe from combined variables
 + confirm proper encoding
 + save dataframe to CSV

nicholas chung, 2017
nich.chung@gmail.com
"""

from bs4 import BeautifulSoup
import pandas as pd

# select scraper and import data
from wiki_scraper import soup

# create variables to store scraped data
contestant = []
name = []
age = []
hometown = []
outcome = []


# create object from [second] table
table = soup('table')[1]

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
    # append variable to 'name' 
    name.append(column_2)
    
    # create variable of string inside third <td> pair
    column_3 = col[2].text.strip()
    # append variable to 'age' 
    age.append(column_3)
    
    # create variable of string inside fourth <td> pair
    column_4 = col[3].text.strip()
    # append variable to 'hometown' 
    hometown.append(column_4)
    
    # create variable of string inside fifth <td> pair
    column_5 = col[4].text.strip()
    # append variable to 'outcome' 
    outcome.append(column_5)
    

# create variable of value of columns
columns = {'contestant': contestant, 'name': name, 'age': age, 'hometown': hometown, 'outcome': outcome}

# create dataframe from 'columns' variable with 'from_dict' to account for arrays with different n
results = pd.DataFrame.from_dict(columns, orient='index')
# flip dataframe axes
results = results.transpose()
# reset column order
results = results[['contestant', 'name', 'age', 'hometown', 'outcome']]


# confirm unicode encoding
results = results.apply(lambda x: pd.lib.infer_dtype(x.values))
results[results=='unicode']

# save to CSV
results.to_csv('../data/contestants.csv')
