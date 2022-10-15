import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.worldometers.info/coronavirus/'

page = requests.get(url)

soup = BeautifulSoup = (page.text, 'lxml')
soup

# obtain information from html tag <table>

table1 = soup.find('table', id='main_tables_countries_today')
table1

# obtain information from html tag <th>

headers = []
for i in table1.find_all('th'):
    title = i.text
    headers.append(title)
