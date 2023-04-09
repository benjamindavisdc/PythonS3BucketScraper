from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from requests_html import HTML, HTMLSession
import pandas as pd
import requests
from googlesearch import search
import re
import time

query= (input("What is the business name? ")+" yelp")

def scrape(i):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    response = requests.get(i)
    #time.sleep(2)
    soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
    text = soup.get_text()
    with open('restaurant.txt', 'w', encoding="utf-8") as file:
        #file.write("full text:" +text)
        hours_pattern = r"(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\s*:\s*(.*?)(?=\n\n|$)"
        for match in re.findall(hours_pattern, text):
            line = match[0] + ': ' + match[1].replace('\n','\n\t')+ '\n'
            file.write(line)
            print(line)
    with open('restaurant.txt', 'a', encoding="utf-8") as file:
        #file.write("full text:" +text)
        hours_pattern = r"(Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday)\s*-\s*(Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday)\s*(\d{1,2}(am|pm))\s*-\s*(\d{1,2}(am|pm))"
        for match in re.findall(hours_pattern, text):
            line = (f"{match[0]} - {match[1]}: {match[2]} - {match[4]}")
            file.write(line)
            print(line)
    with open('restaurant.txt', 'a', encoding="utf-8") as file:
        #file.write("full text:" +text)
        hours_pattern = r"(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\s*\n*\s*(\d{1,2}:\d{2}\s*[A|P]M\s*-\s*\d{1,2}:\d{2}\s*[A|P]M)"
        for match in re.findall(hours_pattern, text):
            line = match[0] + ': ' + match[1].replace('\n','\n\t')+ '\n'
            file.write(line)
            print(line)
    with open('restaurant.txt', 'a', encoding="utf-8") as file:
        #file.write("full text:" +text)
        hours_pattern = r"(Mon|Tue|Wed|Thu|Fri|Sat|Sun)(\d{1,2}:\d{2}\s*[AP]M)\s*-\s*(\d{1,2}:\d{2}\s*[AP]M)"
        for match in re.findall(hours_pattern, text):
            day = match[0]
            start_time = match[1]
            end_time = match[2]
            file.write(f"{day}: {start_time} - {end_time}")
            print((f"{day}: {start_time} - {end_time}"))


for i in search(query, tld="com", num=3, stop=3, pause=2):
    print(i)
    scrape(i)