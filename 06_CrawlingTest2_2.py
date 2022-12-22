## Test2) 사이트내에 인기검색 종목과 주요해외지수를 각각 크롤링하여 종목명과 
##        상한, 하한 여부를 아래와 같이 리스트로 정리해주세요 
##    결과 : [['써니전자','상한],['삼성전자','하한']]~
##           [['다우산업','상한'],['나스닥','상한]]~

import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/03/'
response = requests.get(URL)
soup = BeautifulSoup(response.text,'html.parser')

popular = []
major = []

for item in soup.select('#popularItemList > li') :
    popular.append([item.select_one('a').text,item.select_one('img').attrs['alt']])

print(popular)

print('----')
for item in soup.select('ul.lst_major > li') :
    major.append([item.select_one('a').text, item.select_one('img').attrs['alt']])

print(major)