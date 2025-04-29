# importing libraries
import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup # type: ignore

# initialization of required entities
url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = '/top_50_films.csv'
df = pd.DataFrame(columns=["Average Rank", "Film", "Year"])
count = 0

# loading the webpage for web scraping
html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

# scraping the required information
tables = data.find_all('tbody')
rows = tables[0].find_all('tr')