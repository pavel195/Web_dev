# спарсить данные с сайта , добавить их в базу данных
# и обработать с помощью numpy

import requests
from bs4 import BeautifulSoup

url = 'http://global-finances.ru/chislennost-naseleniya-rossii-po-godam/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

paragraphs = soup.find_all('p')

for p in paragraphs:
    print(p.text)