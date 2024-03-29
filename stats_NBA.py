from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np



def convert_percent(val):
    """
    Convert the percentage string to an actual floating point percent
    """
    new_val = val * 100
    return float(new_val)

def calculate_gamescore():
    pass


#Welcome message
print("Welcome! Please enter the players name that you would like to look up and which year.") 
print("This pulls live data from basketball-reference.com") 
user_input = input("What player would you like to see stats on? : ")
user_year = int(input("Which year would you like? : "))
game_score_bool = input("Would you like to calculate Game Score Statistic? (Y/N) : ")



#To display full data for player
pd.set_option('display.max_columns', None)




#Scraping URL page with specific year
url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(user_year)
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

#Pull and store information from site
player_stats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]


#DataFrame structure with stats and headers as columns
stats_with_none = pd.DataFrame(player_stats, columns = headers)



#Cells have whitespace, change value to NaN
stats_with_none = stats_with_none.replace('', np.nan)



#Get rid of 'None' values, drops row
stats_with_none = stats_with_none.dropna(axis=0, how='any')




#Change Headers from string to Int and float
stats_with_none = stats_with_none.astype({"Age":'int64',"G":'int64',"GS":'int64',
                  "MP":'float64',"FG":'float64',"FGA":'float64',
                  "FG%":'float64', "3P":'float64', "3PA":'float64',
                  "3P%":'float64', "2P": 'float64', "2PA":'float64',
                  "2P%":'float64', "eFG%": 'float64', "FT":'float64',
                  "FTA":'float64', "FT%": 'float64', "ORB": 'float64',
                  "DRB": 'float64', "TRB": 'float64', "AST": 'float64',
                  "STL": 'float64', "BLK": 'float64', "TOV": 'float64',
                  "PF": 'float64', "PTS": 'float64'})






##Find player with user input
player_df = stats_with_none[stats_with_none['Player'] == user_input]

#Calculate a players game score
game_score = player_df["PTS"] + (.4 * player_df["FG"]) \
             - (0.7 * player_df["FGA"]) - (.4 * (player_df["FTA"]-player_df["FT"]))\
            + (0.7 * player_df["ORB"]) + (0.3 * player_df["DRB"]) + player_df["STL"] + \
            (0.7 * player_df["AST"]) + (0.7 * player_df["BLK"]) - (0.4 * player_df["PF"])\
            - player_df["TOV"]


#Print player stats
print()
print("The stats for your player are: ")
print(player_df)

#Print game score if user says yes
if game_score_bool == "Y":
    print("***" * 10)
    print("Refrence: Game score for an average player is 10.")
    print(f"The game score statistic for {user_input} is: ")
    print(game_score)
























