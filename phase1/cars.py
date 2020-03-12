import requests
import time
import csv
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MAX_PAGE = 45
MAX_PAGE_PIG = 2
driver = webdriver.Chrome('./chromedriver.exe')

with open('result.csv', 'w') as f:
    f.write("Car , Price , Transmition, EXT_COLOR , INT_COLOR , Derivtrain \n")

for i in range(0, MAX_PAGE):
    page_num = str(i)
    url = "https://www.cars.com/for-sale/searchresults.action/?dealerType=localOnly&page=" + page_num + "&perPage=20&rd=99999&searchSource=GN_BREADCRUMB&sort=relevance&zc=92521"
    driver.get(url)
    #time.sleep(10)
    
    #create object
    car = driver.find_elements_by_xpath('//h2[@class="listing-row__title"]')
    price = driver.find_elements_by_xpath('//span[@class="listing-row__price "]')
    transmition = driver.find_elements_by_xpath("//li[strong = 'Transmission:']")
    ext_color = driver.find_elements_by_xpath("//li[strong = 'Ext. Color:']")
    int_color = driver.find_elements_by_xpath("//li[strong = 'Int. Color:']") 
    Derivtrain = driver.find_elements_by_xpath("//li[strong = 'Drivetrain:']")
    num_page_items = len(price)
    with open('result.csv', 'a') as f:
        for i in range(num_page_items):
           
            t_mission = (transmition[i].text.strip()).split(":")[-1].strip()
            e_color = (ext_color[i].text.strip()).split(":")[-1].strip() 
            i_color = (int_color[i].text.strip()).split(":")[-1].strip()
            Dev = (Derivtrain[i].text.strip()).split(":")[-1].strip() 
            
            f.write(car[i].text + "," + ((price[i].text).replace(',',''))+ "," + t_mission + "," + e_color + "," + i_color + "," + Dev + "\n")
            
driver.close()
