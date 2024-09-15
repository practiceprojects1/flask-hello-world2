from flask import Flask, render_template
import textile
from os import read
from pickle import FALSE, TRUE
from pandas.io.parsers.readers import read_csv
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import smtplib
import re
import html

test = "is this working"






###########TESTING############
# create list for areas of interest
l = ["Russia", "China", "Chinese", "Iran", "Iranian", "Iranian","Microsoft", "Cisco"]

data1 = ''

def url1():
    global data1
    global l
    url = "https://thehackernews.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('a', class_='story-link')

    for article in articles:
        header = article.find('h2', class_='home-title').get_text()
        description = article.find('div', class_='home-desc').get_text()
        #print(article['href'])
        response1 = requests.get(article['href'])
        soup1 = BeautifulSoup(response1.text, 'html.parser')
        cves = re.findall(r'CVE-\d{4}-\d{4,}', str(soup1))
        ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\[\.\]\d{1,3}', str(soup1))

        if any(word in header for word in l) or any(word in description for word in l):
            cves = str(cves)
            cves = cves.replace("[", "")
            cves = cves.replace("]", "")
            ips = str(ips)
            ips = ips.replace("[", "")
            ips = ips.replace("]", "")
            data = header+ ":" + "\n\n" + description[0:500]+"..." + "\n\n" + "CVEs \n" + cves + "\n" + "IPs\n" + ips + "\n\n" +article['href'] + "\n\n" + "\n\n"
            data = str(data)
            data = re.sub(r'\t', '',data)
            data1 = data1 + "\n\n\n\n" + data

def url2():
  global data1
  global l
  url = "https://www.bleepingcomputer.com/"
  response = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'})
  soup = BeautifulSoup(response.text, 'html.parser')
  articles = soup.find_all('li')


  for article in articles:
    header = article.find('h4')
    description = article.find('p')
    link = article.find('a', href=True)
    #link = str(link['href'])
    #link = re.findall(r'(?:https?|ftp):\/\/[^\s/$.?#].[^\s]+', link)
    

    if header is not None and description is not None:
      header1 = header.text.strip()
      description1 = description.text.strip()
      
      if any(word in header1 for word in l) or any(word in description1 for word in l):
        response1 = requests.get(link['href'])
        soup1 = BeautifulSoup(response1.text, 'html.parser')
        cves = re.findall(r'CVE-\d{4}-\d{4,}', str(soup1))
        ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}', str(soup1))
        cves = str(cves)
        ips = str(ips)
        ips = ips.replace("0.0.1.1", "")
        ips = ips.replace("1.1.1.1", "")
        ips = ips.replace("\'", '')
        ips = ips.replace(",", ' ')
        cves = cves.replace("[", "")
        cves = cves.replace("]", "")
        ips = ips.replace("]", "")
        ips = ips.replace("[", "")
        data = header1 + ":" + "\n\n" + description1[0:500] + "..." + "\n\n" + "CVEs \n" + cves + "\n" + "IPs\n" + ips + "\n\n" + str(link['href']) + "\n\n"
        data = data
        data1 = data1 + "\n\n\n\n" + data


def convert_to_html():
   global data1
   url_pattern = r'http[s]?://[^\s]+'
   data1 = textile.textile(data1)
   for x in data1:
    url = re.search(url_pattern, x)
    url = str(url).replace("<p>","")



    #if x.startswith(word1):
      #x1 = x.replace("<p>", "")
      #x1 = "<a href=" + x1 + ">" + "</a>"



######### Add reformat html code here ##########


# Make all of the links clickable

###########END TEST############


app = Flask(__name__)

@app.route('/')
def home():
    global test
    global data1
    test1 = test
    return render_template('index3.html', test2=data1)

@app.route('/iocdatabase')
def database():
    return "This is the database location"
    

if __name__ == '__main__':
  url1()
  url2()
  convert_to_html()
  app.run(debug=True)
