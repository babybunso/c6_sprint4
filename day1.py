from time import sleep
import random as r
from IPython import embed
from bs4 import BeautifulSoup
import re
import requests

r.seed(42)

def delay(seconds):
    print(f'Sleeping for {seconds} second(s)')
    sleep(seconds)

def main():
    for i in range(5):
        print (i)
        delay(seconds=r.randint(1, 5))

def emb():
    a = 5
    b = 3
    embed()
    print(a)
    print(b)

def generate_html():
    return '''
        <html>
            <head>testing</head>
            <body>
                <!-- <div id='target'>Hello World</div> -->
                <a href="/a.html">A</a>
                <a href="/b.html">B</a>
                <a href="/c.html">C</a>
                <a href="/d.html">D</a>
                <a href="/e.html">E</a>

                <script>
                    var hello = 'yoh';
                    alert(hello);
                </script>
            </body>
        </html>
    '''

def scrape1():
    html_doc = generate_html()
    soup = BeautifulSoup(html_doc, 'html.parser')
    target = soup.find(id='target')
    print(target.get_text())

def scrape2():
    html_doc = generate_html()
    soup = BeautifulSoup(html_doc, 'html.parser')
    a_elements = soup.find_all('a', href=True)
    for a in a_elements:
        print(a['href'].split('/')[1])

def scrape3():
    html_doc = generate_html()
    pattern = re.compile(r"var hello = '(.*?)';$", re.MULTILINE | re.DOTALL)
    print(pattern.search(html_doc).group(1))

headers = {'User-Agent': 'Moziila/5.0 (X11; Linux x86_64)'}
# time.sleep(2)
BASE_URL = 'https://albertyumol.github.io/'

def extract_html_content(url):
    response = requests.get(url, headers)
    return response.text

def req(page):
    if page == 1:
        target_url = BASE_URL + 'index.html'
    else:
        target_url = BASE_URL + f'page{page}/index.html'

    html_content = extract_html_content(target_url)
    # print(html_content)
    scrape_titles(html_content)

def scrape_titles(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    h2_elements = soup.find_all('h2')
    for i, h2 in enumerate(h2_elements):
        print(f'{h2.a.text}')

if __name__ == '__main__':
    for i in range(4):
        req(i + 1)

