# %%

## importing libraries

import requests
from bs4 import BeautifulSoup 
import json
import pyjsparser
import js2xml
from datetime import datetime, date, timedelta
import pandas as pd


# %%

### scraping active cases

def scrape(country):
    url = 'https://www.worldometers.info/coronavirus/country/' + country + '/'
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    scripts = soup.find_all('script')
    counter = 0
    retlist = [ ]
    retlist.append(country);
    while counter < len(scripts):
        try:
            if js2xml.parse(scripts[counter].string).xpath('//property[@name="title"]//string/text()')[0] in ['Active Cases']:
                retlist.append(js2xml.parse(scripts[counter].string).xpath('//property[@name="title"]//string/text()')[0])
                retlist = retlist + json.loads('[' + scripts[counter].string.split('data: [', 1)[1].split(']', 1)[0] + ']')
        except:
            pass
        counter = counter + 1
    return retlist

countries = ['us']
#for country in countries:
    #print((scrape(country)))

active_cases_us=scrape(country)[2:]

print(active_cases_us)
len(active_cases_us)

# %%

## adding a date range

sdate = date(2020, 2, 15)   # start date
edate = date(2020, 11, 16)   # end date

delta = edate - sdate       # as timedelta


date_list= []
for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    date_list.append(day)
    #print(day)

print(date_list)

len(date_list)
# %%

##dictionary with the active cases and dates

dict_active_cases_us=[]
for d, c in zip(date_list, active_cases_us):
    dict_x={"datetime":d, "active_cases":c}
    dict_active_cases_us.append(dict_x)

print(dict_active_cases_us)

# %%

### converting dict into a dataframe

df_active_cases_us=pd.DataFrame(dict_active_cases_us, columns=["datetime", "active_cases"])

# %%

### trimming the date range

startdate = pd.to_datetime("2020-03-01").date()
enddate = pd.to_datetime("2020-09-30").date()
df_active_cases_us.loc[startdate:enddate]

# %%
