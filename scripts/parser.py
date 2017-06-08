import requests
from bs4 import BeautifulSoup
import pandas as pd

from wiki_scraper import soup

# create variables to store scraped data
rank = []
contestant = []
age = []
hometown = []
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
ep_13 = []
ep_14 = []

# results table has color-coded data; check page for key 
color = []

# create an object of the first object that is class=dataframe
table = soup.find("table", class_='wikitable')

# find all the <tr> tag pairs; skip the first one (table header)
for row in table.find_all('tr')[1:]:
    
    # create a variable for each <td> pair 
    col = row.find_all('td')

    # create a variable of the string inside the first <td> pair
    column_1 = col[0].text.strip()
    # append variable to 'rank' variable
    rank.append(column_1)
    
    # create a variable of the string inside the second <td> pair
    column_2 = col[2].text.strip()
    # append variable to 'contestant' variable
    contestant.append(column_2)
    
    # create a variable of the string inside the third <td> pair
    column_3 = col[4].text.strip()
    # append variable to 'age' variable
    age.append(column_3)
    
    # create a variable of the string inside the fourth <td> pair
    column_4 = col[5].text.strip()
    # append variable to 'hometown' variable
    hometown.append(column_4)
    
    # create a variable of the string inside the fifth <td> pair
    column_5 = col[6].text.strip()
    # append variable to 'ep_1' variable
    ep_1.append(column_5)
    
    # create a variable of the string inside the sixth <td> pair
    column_6 = col[7].text.strip()
    # append variable to 'ep_2' variable
    ep_2.append(column_6)
    
    # create a variable of the string inside the seventh <td> pair
    column_7 = col[8].text.strip()
    # append variable to 'ep_3' variable
    ep_3.append(column_7)
    
    # create a variable of the string inside the eight <td> pair
    column_8 = col[9].text.strip()
    # append variable to 'ep_4' variable
    ep_4.append(column_8)

    # create a variable of the string inside the ninth <td> pair
    column_9 = col[10].text.strip()
    # append variable to 'ep_5' variable
    ep_5.append(column_9)

    # create a variable of the string inside the tenth <td> pair
    column_10 = col[11].text.strip()
    # append variable to 'ep_6' variable
    ep_6.append(column_10)

    # create a variable of the string inside the eleventh <td> pair
    column_11 = col[12].text.strip()
    # append variable to 'ep_7' variable
    ep_7.append(column_11)

    # create a variable of the string inside the twelfth <td> pair
    column_12 = col[13].text.strip()
    # append variable to 'ep_8' variable
    ep_8.append(column_12)

    # create a variable of the string inside the thirteenth <td> pair
    column_13 = col[14].text.strip()
    # append variable to 'ep_9' variable
    ep_9.append(column_13)

    # create a variable of the string inside the fourteenth <td> pair
    column_14 = col[15].text.strip()
    # append variable to 'ep_10' variable
    ep_10.append(column_14)

    # create a variable of the string inside the fifteenth <td> pair
    column_15 = col[16].text.strip()
    # append variable to 'ep_11' variable
    ep_11.append(column_15)
    
    # create a variable of the string inside the sixteenth <td> pair
    column_16 = col[17].text.strip()
    # append variable to 'ep_12' variable
    ep_12.append(column_16)
    
    # create a variable of the string inside the seventeenth <td> pair
    column_17 = col[18].text.strip()
    # append variable to 'ep_13' variable
    ep_13.append(column_17)
    
    # create a variable of the string inside the eighteenth <td> pair
    column_18 = col[19].text.strip()
    # append variable to 'ep_14' variable
    ep_14.append(column_18)

# create variable of value of columns
columns = {'rank': rank, 'contestant': contestant, 'age': age, 'hometown': hometown, 'ep_1': ep_1, 'ep_2': ep_2, 'ep_3': ep_3, 'ep_4': ep_4, 'ep_5': ep_5, 'ep_6': ep_6, 'ep_7': ep_7, 'ep_8': ep_8, 'ep_9': ep_9, 'ep_10': ep_10, 'ep_11': ep_11, 'ep_12': ep_12, 'ep_13': ep_13, 'ep_14': ep_14}

# create dataframe from 'columns' variable
results = pd.DataFrame(columns)
