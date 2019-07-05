from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd



def convert_percent(val):
    """
    Convert the percentage string to an actual floating point percent
    """
    new_val = val * 100
    return float(new_val)


user_input = input("What player would you like to see stats on? : ")


#To display full data for player
pd.set_option('display.max_columns', None)


#Analyzing the year
year = 2019

#Scraping URL page with specific year
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

#Pull information from site in to 2d
player_stats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]


#2d structure with stats and headers as columns
stats_with_none = pd.DataFrame(player_stats, columns = headers)

#Get rid of 'None' values, drops row
new_stats = stats_with_none.dropna(axis=0, how='any')


#Find player with user input
player_df = new_stats[new_stats['Player'] == user_input]



player_df.info()
#player_df['AST'].plot()
#print(layer_df[1])



print(player_df['FT%'])














'''count = 0
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
'''








