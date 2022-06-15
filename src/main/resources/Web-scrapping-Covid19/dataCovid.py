#from lib2to3.pgen2 import driver
from os import link
from numpy import product
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time


driver = webdriver.Chrome('D:\chromedriver.exe')
driver.get('https://covid19.gob.sv/')

last_height = driver.execute_script('return c')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height
    
soup = BeautifulSoup(driver.page_source, 'lxml')
charts_covid = soup.find_all('div', class_ = 'igc-graph-group')

df = pd.DataFrame({'Link':['']})

for chart in charts_covid:
    try:
        link = chart.find('rect', class_ = 'igc-crosshair-overlay').get('href')
        df = df.append({'Link':link}, ingnore_index = True)
    except:
        pass
    break

