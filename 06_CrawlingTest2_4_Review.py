import requests
from bs4 import BeautifulSoup
# 분양중인 아파트 정보를 클로링 하여 아래와 같이 딕셔너리 형태로 정리 
url = 'https://crawlingstudy-dd3c9.web.app/03'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
apt = []
for sale in soup.select('.sale_list> li'):
    name = sale.select_one('a').text
    apt.append({
        '이름': name,
        '분양가' : sale.select('.sale_detail dd.txt')[0].text.replace(' 만원','').replace(',',''),
        '유형' : sale.select('.sale_detail dd.txt')[1].text.split('|')[0],
        '분양유형' : sale.select('.sale_detail dd.txt')[1].text.split('|')[1],
        '세대수' : sale.select('.sale_detail dd.txt')[2].text.split('|')[0],
        '평형': sale.select('.sale_detail dd.txt')[2].text.split('|')[1]
    })
print(apt)