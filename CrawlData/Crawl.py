import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import datetime
import  main
from time import sleep
import requests
date = []
time = []
forecast = []
tem = []
rain = []
rainper = []
cloud = []
pressure = []
wind = []
gust = []
kt = []
if __name__ == '__main__':
    url = "https://www.worldweatheronline.com/ha-noi-weather-history/vn.aspx"
    driver = webdriver.Chrome(executable_path="chromedriver")
    driver.maximize_window()
    driver.get(url)
    x=5000
    date_object = datetime.date.today()
    #date_object = datetime.datetime(2008, 8, 29)
    while x>0:
        dat = driver.find_element(By.ID,"ctl00_MainContentHolder_txtPastDate")
        button = driver.find_element(By.ID, "ctl00_MainContentHolder_butShowPastWeather")
        date_object = date_object + datetime.timedelta(days=-1)
        date = date_object.strftime("%m/%d/%Y")
        dat.send_keys(date)
        button.click()
        content = driver.page_source
        main.laytt(content)
        if x==1:
            main.intt()
        x-=1




