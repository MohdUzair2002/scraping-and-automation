from re import sub
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import pandas as pd
import csv
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import os
import urllib
import math
import sys
import time
from bs4 import BeautifulSoup
data=[]
chrome_options = Options()
availableprod=[]

chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("user-data-dir=C:/Users/user/AppData/Local/Google/Chrome/User Data")

chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
S=Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=S,options=chrome_options)
browser.maximize_window()
i=1


file=pd.read_excel('Links.xlsx')

links=file['Link'].tolist()
time.sleep(2)
for link in links:
    # s=link[0].split()
    data.append((link[0:].split("H"))[-1][0:-1])
print(data)
    
while(i<=56):
    url="https://www.hermes.com/hk/en/"
    browser.get(url)
    time.sleep(15)
    try:
     searchbutton=browser.find_element(By.XPATH,"//*[@class='btn search icon icon-search']").click()
    except:
        pass
    search_button=browser.find_element(By.XPATH,"//*[@class='field-search']").send_keys("H"+data[i])
    browser.find_element(By.XPATH,"//*[@class='field-search']").send_keys(Keys.RETURN)
    time.sleep(5)
    try:
      pro=WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH,"//*[@class='product-item']")))
      browser.execute_script("arguments[0].click();", pro)

    except:
        pass  
    try:
        cart=WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH,"//*[@name='add-to-cart']")))
        availableprod.append("i")

    except:
        pass
    print(availableprod)
    if (i==56):
        i=0
    i+=1
