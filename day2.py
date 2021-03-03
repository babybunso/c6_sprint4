from IPython import embed
from time import sleep
import random as r
from bs4 import BeautifulSoup as BS
import re
import requests

# '/usr/local/bin/chromedriver'
BASE_URL = 'https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area'
HEADER = {'User-Agent': 'Moziila/5.0 (X11; Linux x86_64)'}

r.seed(42)

def delay(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    sleep(seconds)

def html_content(path):
    return requests.get(BASE_URL + path, HEADER)

def scrape(ms=2):
    html = html_content('')
    soup = BS(html.content, 'lxml')
    table = soup.find_all('table', class_=re.compile('wiki'))
    # table = soup.find('table', class_= 'wikitable sortable')
    print(len(table))
    delay(ms)

def main():
    scrape()

if __name__ == '__main__':
    main()