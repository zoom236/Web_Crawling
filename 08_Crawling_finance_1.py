# 주가 크롤링
# https://finance.naver.com/sise/sise_quant.nhn
# 1) 품목명과 현재가를 크롤링 해주세요.

import requests
from bs4 import BeautifulSoup

URL = 'https://finance.naver.com/sise/sise_quant.nhn'
response = requests.get(URL)
soup = BeautifulSoup(response.text,'html.parser')

data=[]

for content in soup.select('table.type_2 tr') :
    if len(content.select('td')) != 12:
        continue
    data.append({
        'num' :content.select('td')[0].text,
        '종목명' : content.select('td')[1].text,
        '현재가' : content.select('td')[2].text
    })
print(data)
 