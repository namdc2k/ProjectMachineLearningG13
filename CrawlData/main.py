import numpy
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import csv
import requests
url = "https://www.worldweatheronline.com/ha-noi-weather-history/vn.aspx"
content = requests.get(url).content
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
def laytt(content):
    soup = BeautifulSoup(content, 'html.parser')
    body_part=soup.find('body')
    table=body_part.find('table',{"class": "days-details-table"})
    td=table.findAll('td',{"class": "days-details-row-header-item"})
    img=table.findAll('img',{"class": "days-table-forecast-img"})
    tdi=table.findAll('td',{"class": "days-details-row-item"})
    day=body_part.find('div',{"class": "input-group input-append date"})
    days=day.find('input')
    count=0;
    while (count<8):
        date.append(days['value'])
        forecast.append(img[count]['title'])
        time.append(tdi[count*10].text[:5])
        kt.append(tdi[1+count*10].text)
        tem.append(tdi[2+count*10].text)
        rain.append(tdi[3+count*10].text)
        rainper.append(tdi[4+count*10].text)
        cloud.append(tdi[5+count*10].text)
        pressure.append(tdi[6+count*10].text)
        wind.append(tdi[7+count*10].text)
        gust.append(tdi[8+count*10].text)
        kt.append(tdi[9+count*10].text)
        count+=1
def intt():
    mang=np.array([date,time,forecast,tem,rain,rainper,cloud,pressure,wind,gust])
    mang=mang.T
    # head=numpy.array(["day","time","forecast","tem","rain","rain%","cloud","pressure","wind","gust"])
    # head=head.T
    # pd.DataFrame(head).to_csv('weather.csv',header=None,mode='a',index=False)
    pd.DataFrame(mang).to_csv('weather2.csv',header=None,mode='a',index=False)
if __name__ == '__main__':
    laytt(content)
    intt()