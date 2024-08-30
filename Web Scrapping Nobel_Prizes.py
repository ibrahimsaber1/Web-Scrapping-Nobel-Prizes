# Assignment
link = "https://en.wikipedia.org/wiki/List_of_Nobel_laureates"
#     Year	Physics	Chemistry	Physiologyor Medicine	Literature	Peace	Economics
# ![image.png](attachment:image.png)

# Import the required modules
import requests
from bs4 import BeautifulSoup

response = requests.get("https://en.wikipedia.org/wiki/List_of_Nobel_laureates")
soup = BeautifulSoup(response.text, "html.parser")

table_tags = soup.find("table", attrs={"class":"wikitable sortable"})
row_tags = table_tags.find_all("tr")
len(row_tags)
row_data = row_tags[1].text.split("\n")
# 1 -the year in row
row_year = row_data[1]
row_year
# 2 -the Physics in row

row_Physics = row_data[3]
row_Physics
# 3- the Chemistry in row

row_Chemistry = row_data[5]
row_Chemistry
# 4- the Physiologyor Medicine in row

row_Physio_Med = row_data[7]
row_Physio_Med
# 5- the Literature in row
row_Literature = row_data[9]
row_Literature
# 6- the Peace in row
row_Peace = row_data[11]
row_Peace
# 7- the Economics in row
row_Economics = row_data[13]
row_Economics


import requests
from bs4 import BeautifulSoup
import pandas as pd


response = requests.get("https://en.wikipedia.org/wiki/List_of_Nobel_laureates")
soup = BeautifulSoup(response.text, "html.parser")
table_tags = soup.find("table", attrs={"class": "wikitable sortable"})

with open("Nobel_Prizes.csv", mode="w", encoding="utf-8") as df:
    df.write("year,Physics,Chemistry,Physiologyor Medicine,Literature,Peace,Economics,null\n")  # corrected header
    for i in range(1, 124):
        row_tags = table_tags.find_all("tr")
        row_data = row_tags[i].text.split("\n")
        # 1- the year in row
        try:
            row_year = row_data[1]  
        except:
            row_year = "N/A"
            
        # 2 -the Physics in row
        try:
            row_Physics = row_data[3]
        except:
            row_Physics = "N/A"
            
        # 3- the Chemistry in row
        try:
            row_Chemistry = row_data[5]
        except:
            row_Chemistry = "N/A"
            
        # 4- the Physiologyor Medicine in row
        try:
            row_Physio_Med = row_data[7]
        except:
            row_Physio_Med= "N/A"
        # 5- the Literature in row
        try:
            row_Literature = row_data[9]
        except:
            row_Literature = "N/A"
        # 6- the Peace in row
        try:
            row_Peace = row_data[11]
        except:
            row_Peace = "N/A"
        # 7- the Economics in row
        try:
            row_Economics = row_data[13]
        except IndexError:
            row_Economics = "N/A"  # corrected value if not found
        df.write(f"{row_year},{row_Physics},{row_Chemistry},{row_Physio_Med},{row_Literature},{row_Peace},"/{row_Economics}"/\n")


df = pd.read_csv("Nobel_Prizes.csv")
df
df.head()
print('done!!')
#:)