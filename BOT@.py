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
url="https://www.bhphotovideo.com/c/product/1547009-REG/canon_eos_r5_mirrorless_digital.html"
browser.get(url)