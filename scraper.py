#Credit to Nigel Aw for guidance.

import re
import requests
from bs4 import BeautifulSoup
import csv
from datetime import date

today = date.today()

url = "http://infokemarau.water.gov.my/drought_monitor.cfm"
headers = {'user-agent': 'my-agent/1.0.1'}

site = requests.get(url, headers=headers).text
soup = BeautifulSoup(site,'lxml')
table = soup.findAll('table', id="dis_tbl")[0]
rows = table.findAll('tr')

data_list = []

for row in rows:
    if "Empangan Bukit Merah" in row.text:
        for column in row.findAll('td'):
            data_list.append(column.text.strip())

balanceStorage = data_list[10]
lastUpdated = data_list[11]

def scraper():
    with open('bukitMerah.csv', 'a', newline='') as temp:
        writer = csv.writer(temp, delimiter=',')
        writer.writerow([today,balanceStorage,lastUpdated])
