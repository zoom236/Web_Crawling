import requests
from bs4 import BeautifulSoup

URL = 'https://finance.naver.com/sise/sise_quant.nhn'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

#data = []
for finance in soup.select('table.type_2 tr') :
    if len(finance.select('td'))!= 12:
        continue
    print(finance.select('td')[0].text,finance.select('td')[1].text,finance.select('td')[2].text)
    
    
    #data.append({
    #    'num' : finance.select('td')[0].text,
    #    '종목명' : finance.select('td')[1].text})
#print(data)
   