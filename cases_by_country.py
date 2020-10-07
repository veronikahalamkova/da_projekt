import requests
from bs4 import BeautifulSoup 
import json
import pyjsparser
import js2xml

def scrape(country):
    url = 'https://www.worldometers.info/coronavirus/country/' + country + '/'
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    scripts = soup.find_all('script')
    counter = 0
    retlist = [ ]
    retlist.append(country);
    while counter < len(scripts):
        try:
            if js2xml.parse(scripts[counter].string).xpath('//property[@name="title"]//string/text()')[0] in ["Daily New Cases",'Total Cases', 'Active Cases', 'Total Deaths', "Daily New Deaths"]:
                retlist.append(js2xml.parse(scripts[counter].string).xpath('//property[@name="title"]//string/text()')[0])
                retlist = retlist + json.loads('[' + scripts[counter].string.split('data: [', 1)[1].split(']', 1)[0] + ']')
        except:
            pass
        counter = counter + 1
    return retlist

countries = ['czech-republic','us', 'uk','spain', 'italy', 'france', 'germany', 'china']
for country in countries:
    print(scrape(country))