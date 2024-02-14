import requests
from bs4 import BeautifulSoup as bs
import numpy as np
url = 'https://world-weather.ru/pogoda/united_kingdom/london/'
headers_ = {'User-Agent':'Chrome/39.0.2171.95'}
months = 'january february march may june july august september'.split()
temprature_list = [[]*12]
for month in months:
    temps = []
    url_ = url + month + '-2022/'
    data = requests.get(url_,headers = headers_)
    data_ = bs(data.content, 'html.parser')
    month_data = data_.find('ul',class_ = 'ww-month')
    # print(month_data)
    temprature_list = [int(elem.text[:-1]) for elem in month_data.find_all('span')]
    for elem in month_data.find_all('span'):
        temps.append(elem.text)
        print(elem.text)
    # print(temprature_list)
    temprature_array = np.array(temprature_list)
    print(f'Для месяца  {month}: \n'
          f'{" ".join(temps)} \n'
          f'Mаксимальная температура: {np.max(temprature_array)} \n'
          f'СРЕДНЯЯ ТЕМП: {np.min(temprature_array)} \n'
          f'Минимальная темп : {np.min(temprature_array)} \n'
          f'Дисперсия : {np.var(temprature_array)} \n'
          f'Стандартное отклонение : {np.std(temprature_array):.2f}'
          f'')