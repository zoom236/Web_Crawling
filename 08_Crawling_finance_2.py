# 주가 크롤링
# https://finance.naver.com/sise/sise_quant.nhn
# 1) 전일대비 상승한 항목만 품목명, 현재가, 전일비를 크롤링해주세요.


import requests
from bs4 import BeautifulSoup

URL = 'https://finance.naver.com/sise/sise_quant.nhn'
response = requests.get(URL)
soup = BeautifulSoup(response.text,'html.parser')

data = []

for content in soup.select('table.type_2 tr') :
    if len(content.select('td')) !=12 :
        continue
    
    status = '변화없음'
    
    if content.select('td')[3].select_one('img') != None :         
        status = content.select('td')[3].select_one('img').attrs['alt']
     
    if status == '상승' :
        
        #print(content.select('td')[0].text,
        #      content.select('td')[1].text,
        #      content.select('td')[2].text,
        #      content.select('td')[3].select_one('span').text.strip())
        
        data.append({
            'num' : content.select('td')[0].text,
            '종목명' : content.select('td')[1].text,
            '현재가' : content.select('td')[2].text,
            '전일비' : content.select('td')[3].select_one('span').text.strip()
        })
print(data)    
    