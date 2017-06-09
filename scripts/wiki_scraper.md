# RPDR wiki contestant ID scraper 1.0.0
nicholas chung, 2017 | nich.chung@gmail.com
***

beautifulsoup4 parser

scrape, parse, and write contestant table to CSV:
 
 1. load and assign URL to bs4 object 
 2. select table by position
 3. assign table data to variables
 4. make dataframe from combined variables
 5. save dataframe to CSV

*run script from scripts/ in project directory*

#### import modules
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
'''

#### avoid 403 response (or use WikiMedia API)
'''
header = {'User-Agent': 'Mozilla/5.0'}
'''

#### create variable with url to target page
'''
url = 'https://en.wikipedia.org/wiki/RuPaul%27s_Drag_Race_(season_5)' 
'''

#### scrape html at url
'''
r = requests.get(url)
'''

#### turn html into bs4 object
'''
soup = BeautifulSoup(r.text, 'lxml')
'''

#### create variables to store scraped data
'''
contestant = []
name = []
age = []
hometown = []
outcome = []
'''

#### create object from [second] table
'''
table = soup('table')[1]
'''

#### find all <tr> tag pairs; skip first one (table header)
    # create variable for each <td> pair 
    # create variable of string inside first <td> pair
    # append variable to 'name' 
'''
for row in table.find_all('tr')[1:]:
    
    col = row.find_all('td')

    column_1 = col[0].text.strip()
    contestant.append(column_1)
    
    column_2 = col[1].text.strip()
    name.append(column_2)
    
    column_3 = col[2].text.strip()
    age.append(column_3)
    
    column_4 = col[3].text.strip()
    hometown.append(column_4)
    
    column_5 = col[4].text.strip()
    outcome.append(column_5)
'''
    

#### create variable of value of columns
'''
columns = {'contestant': contestant, 'name': name, 'age': age, 'hometown': hometown, 'outcome': outcome}
'''

#### create dataframe from 'columns' variable with 'from_dict' to account for arrays with different n, flip dataframe axes, and confirm column order
'''
results = pd.DataFrame.from_dict(columns, orient='index')
results = results.transpose()
results = results[['contestant', 'name', 'age', 'hometown', 'outcome']]
'''


#### encode and save to CSV as UTF-8
'''
results.to_csv('../data/contestants.csv', encoding='utf-8')
'''
