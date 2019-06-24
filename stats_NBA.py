from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

    
#Clean "None"
#Ask user what year
#Asks user for players name

user_input = input("What player would you like to see stats on? : ")
print(user_input.lower())


#Analyzing the year
year = 2019

#Scraping URL page
url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)
html = urlopen(url)


#Passed features to get around error
soup = BeautifulSoup(html,features='lxml')

#use findALL() to get the column headers
soup.findAll('tr', limit=2)

#use getText() to extract the text we need into a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]

#Avoid rank
headers = headers[1:]

#Avoid the first header
rows = soup.findAll('tr')[1:]


player_stats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]




#2d structure with stats and headers as columns
stats_with_none = pd.DataFrame(player_stats, columns = headers)

new_stats = stats_with_none.dropna(axis=0, how='any')

count = 0

#List of player names
player_list = []
for i in player_stats:
    #Add each player names to list
    try:
        player_name = i[0]
        player_list.append(player_name.lower())
        count += 1
    #If empty do not add to list
    except IndexError:
        pass
        

#Matches user input to player lists
matching = [name for name in player_list if user_input.lower() in name]
print(matching)







