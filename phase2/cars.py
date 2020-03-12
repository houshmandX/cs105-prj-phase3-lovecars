import requests
import time
import csv
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MAX_PAGE = 50
driver = webdriver.Chrome('./chromedriver.exe')

with open('result.csv', 'w') as f:
    f.write("Year, Brand , Model , Title, Mile , Price , Transmition, EXT_COLOR , INT_COLOR , Derivtrain, zipcode \n")
    f.align='r'
    f.border=False
for i in range(0, MAX_PAGE):
    zipcode = str(89107)
    page_num = str(i)
    url = "https://www.cars.com/for-sale/searchresults.action/?dealerType=localOnly&page=" + page_num + "&perPage=100&rd=99999&searchSource=GN_BREADCRUMB&sort=relevance&zc=" + zipcode
    driver.get(url)
    #time.sleep(4)

    #create object
    car = driver.find_elements_by_xpath('//h2[@class="listing-row__title"]')
    price = driver.find_elements_by_xpath('//span[@class="listing-row__price "] | //span[@class="listing-row__price new"]')
    transmition = driver.find_elements_by_xpath("//li[strong = 'Transmission:']")
    ext_color = driver.find_elements_by_xpath("//li[strong = 'Ext. Color:']")
    int_color = driver.find_elements_by_xpath("//li[strong = 'Int. Color:']") 
    Derivtrain = driver.find_elements_by_xpath("//li[strong = 'Drivetrain:']")
    dealer = driver.find_elements_by_xpath('//div[@class="listing-row__dealer__basic-details"]')
    #rate = driver.find_elements_by_xpath('//div[@class="dealer-rating-stars "]')
    tit = driver.find_elements_by_xpath('//div[@class="listing-row__stocktype"]')
    sub_mile = driver.find_elements_by_xpath('//div[@class="payment-section"]')
    mile = driver.find_elements_by_xpath('//span[(@class="listing-row__mileage")]')
    num_page_items = len(price)
    with open('result.csv', 'a') as f:
        for i in range(num_page_items):
            st2 = car[i].text
            year = (st2.split(' ', 1)[0])
            car2 = (st2.split(' ', 1)[1])
            brand = car2.split(' ', 1)[0]
            if len(car2) >= 8 : 
                model = car2.split(' ', 1)[1]
            else:
                model = "NULL" 
            prices = ((price[i].text).replace(',','')).split("$")[-1].strip()
            t_mission = (transmition[i].text.strip()).split(":")[-1].strip()
            e_color = (ext_color[i].text.strip()).split(":")[-1].strip() 
            i_color = (int_color[i].text.strip()).split(":")[-1].strip()
            Dev = (Derivtrain[i].text.strip()).split(":")[-1].strip()
            st3 = (sub_mile[i].text)
            
            #rating = ((rate[i].text).split(' ', 1)[0])
            #Reviewer = (((rate[i].text).rsplit(' ', 1)[0]).rsplit(' ', 1)[1]).split("(")[-1].strip()
            #print(st +"size: "+ str(len(st)))
              
            if len(st3) == 17 :
                m = (st3.split(' ', 2)[1]).replace(',','')
            elif len(st3) == 18 :    
                m = (st3.split(' ', 2)[1]).replace(',','')
            else:
                m = "0"
                
            f.write(year + "," + brand + "," + model + "," + tit[i].text + "," + m + "," + prices + "," + t_mission + "," + e_color + "," + i_color + "," + Dev + "," + zipcode + "\n")
            f.align='l'
            f.border=False
driver.close()
