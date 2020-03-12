# cs105-prj-phase3-lovecars

![omt diagram](image/demo.png)

# Overview
As we know cars are important to people based on their futures such that; Brand, Model, size, power, gas mileage, PRICE, and ...
I found this can be interesting because of my interest in cars, so I decided to find a data set of car future and their prices. Most of the dealership selling their cars lower than the actual MSRP, which I will look into it in this project. We will also look at the popularity and number of sales, regarding brands or cars’ future. 

# Goals
In the introduction, we described the overall idea of this project, but let’s look more specifically at the purpose of this project. I chose this topic as my final project just not because I love cars and it’s my interest. I chose because it’s one of the most important needs of humans these days. I always had questions about MSRP, and how these numbers coming from, and how, and why dealership selling their cars under these prices. What makes one car special to others, and how one can sell more in this market. Why one brand is more popular to others. How new cars with hybrid engines, or electric cars effects these prices, and popularity. We will look into most of these questions, and analyzing them in this project.

# Objective
To accomplish this project, we need to collect useful and accurate data. Some of these data already exist as CSV file that we are going to use, but for other types of data that we need, we are going to obtain them by web crawling using selenium. I found a data of “Car features and their corresponding MSRP” which have information about make, model, year, engine, and other properties of the car used to predict its price. Here is the website that I'm crawling it:
https://www.cars.com/for-sale/searchresults.action/?dealerType=localOnly&page=1&perPage=20&rd=99999&searchSource=GN_BREADCRUMB&sort=relevance&zc=92521 

# How to run the code!
To run the code for web crwaling, you need to install selenium : pip install -U selenium 
You also need to install and download right version of google driver : https://sites.google.com/a/chromium.org/chromedriver/downloads
More information how to install all drivers for selenuim can find here : https://selenium-python.readthedocs.io/installation.html



