# importing libraries
import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup  # type: ignore

# initialization of required entities
url = "https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films"
db_name = "Movies.db"
table_name = "Top_50"
csv_path = "./top_50_films.csv"
df = pd.DataFrame(columns=["Average Rank", "Film", "Year"])
count = 0

# loading the webpage for web scraping
html_page = requests.get(url).text
data = BeautifulSoup(html_page, "html.parser")

# scraping the required information
tables = data.find_all("tbody")
rows = tables[0].find_all("tr")

# iterate over the rows to find the required data
for row in rows:
    # restrict to 50 entries
    if count < 50:
        col = row.find_all("td")
        if len(col) != 0:
            data_dict = {
                "Average Rank": col[0].contents[0],
                "Film": col[1].contents[0],
                "Year": col[2].contents[0],
            }
            df1 = pd.DataFrame(data=data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
            count += 1
    else:
        break

# printing the contents of dataframe
print(df)

# saving to csv file
df.to_csv(csv_path)

# Storing to database

# initializing database connection
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()