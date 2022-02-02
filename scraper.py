import re
import requests
from bs4 import BeautifulSoup
import csv
from datetime import date

today = date.today()

url = "http://infokemarau.water.gov.my/drought_monitor.cfm"
headers = {'user-agent': 'my-agent/1.0.1'}

soup = BeautifulSoup(requests.get(url, headers=headers).text)

tables = soup.find(text=re.compile('5006401')) #find the station name
stationNo = tables.text
balanceStorage = tables.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.text
lastUpdate = tables.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.text
today = date.today()

def scraper(): #creates a temp.csv file to store current data
    with open('bukitMerah.csv', 'a', newline='') as temp:
        writer = csv.writer(temp, delimiter=',')
        writer.writerow([today,balanceStorage.strip(),stationNo.strip(),lastUpdate.strip()])
