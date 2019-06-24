from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

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

#Avoid the first header row
rows = soup.findAll('tr')[1:]


player_stats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]


stats = pd.DataFrame(player_stats, columns = headers)
stats.head(10)
print(stats)
