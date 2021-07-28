from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv
import requests
import pandas as pd
url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page = requests.get(url)
print(page)
soup = BeautifulSoup(page.text,"html.parser")
startable = soup.find('table')
templist = []
tablerows = startable.find_all('tr')
for tr in tablerows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    templist.append(row)
starnames = []
distance = []
mass = []
radius = []
lum = []
for i in range(1,len(templist)):
    starnames.append(templist[i][1])
    distance.append(templist[i][3])
    mass.append(templist[i][5])
    radius.append(templist[i][6])
    lum.append(templist[i][7])
df2 = pd.DataFrame(list(zip(starnames,distance,mass,radius,lum)),columns = ['starname','distance','mass','radius','lum'])
print(df2)
df2.to_csv('brightstar.csv')