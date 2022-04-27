#There are so many libraries,frameworks and tools for task of web scraping.
#Commonly used libraries and modules are Scrapy,Selenium,BeautifulSoup,Urlib.request

#Here,searched for 'comparison of programming languages'
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Comparison_of_programming_languages")
soup = BeautifulSoup(html, "html.parser")
table = soup.findAll("table", {"class":"wikitable"})[0]
rows = table.findAll("tr")

with open("language.csv", "wt+", newline="") as f:
    writer = csv.writer(f)
    for i in rows:
        row = []
        for cell in i.findAll(["td", "th"]):
            row.append(cell.get_text())
        writer.writerow(row)
   
  
import pandas as pd
a = pd.read_csv("language.csv")
a.head()