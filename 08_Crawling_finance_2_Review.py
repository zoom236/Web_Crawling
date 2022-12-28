import requests
from bs4 import BeautifulSoup

URL = 'https://finance.naver.com/sise/sise_quant.nhn'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

for finance in soup.select('#contentarea table.type_2 tr'):
    if len(finance.select('td')) != 12 :
        continue

    if finance.select('td')[3].select_one('img') != None :
        if finance.select('td')[3].select_one('img').attrs['height'] == "11" :
            continue
        if  finance.select('td')[3].select_one('img').attrs['alt'] =="상승" :
            print(finance.select('td')[0].text,finance.select('td')[1].text,finance.select('td')[2].text,finance.select('td')[3].select_one('span').text.strip())