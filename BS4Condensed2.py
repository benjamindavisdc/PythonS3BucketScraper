from bs4 import BeautifulSoup
import requests
import re
import time
from googlesearch import search

with open('restaurant.txt', 'w', encoding="utf-8"):
    pass

def scrape_hours(text, pattern, output_format):
    with open('restaurant.txt', 'a', encoding="utf-8") as file:
        for match in re.findall(pattern, text):
            line = output_format.format(*match)
            file.write(line + '\n')
            print(line)

def scrape(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    response = requests.get(url)
    soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
    text = soup.get_text()

    patterns = [
        (r"(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\s*:\s*(.*?)(?=\n\n|$)",
         '{}: {}\n\t'),
        (r"(Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday)\s*-\s*(Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday)\s*(\d{1,2}(am|pm))\s*-\s*(\d{1,2}(am|pm))",
         '{} - {}: {} - {}'),
        (r"(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\s*\n*\s*(\d{1,2}:\d{2}\s*[A|P]M\s*-\s*\d{1,2}:\d{2}\s*[A|P]M)",
         '{}: {}\n\t'),
        (r"(Mon|Tue|Wed|Thu|Fri|Sat|Sun)(\d{1,2}:\d{2}\s*[AP]M)\s*-\s*(\d{1,2}:\d{2}\s*[AP]M)",
         '{}: {} - {}')]

    for pattern, output_format in patterns:
        scrape_hours(text, pattern, output_format)
    with open('restaurant.txt', 'a') as file:
        file.write(url + '\n')

query= (input("What is the business name? ")+" yelp")
for url in search(query, tld="com", num=3, stop=3, pause=2):
    print(url)
    scrape(url)