import requests
from bs4 import BeautifulSoup

#인기검색종목과 주요해외지수 / 중목명과 주가지수를 리스트로 표현 [['써니전자','5000'],['삼성전자','55,200']~]/ [['다우산업','28,647.43'],['나스닥','9,015.03]'~]

url = 'https://crawlingstudy-dd3c9.web.app/03/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

popular = []
result = soup.select("#popularItemList > li")
for pop in result:
    popular.append([pop.select_one('a').text,pop.select_one('span').text])
print(popular)

major = []

for maj in soup.select('.lst_major > li'):
    major.append([maj.select_one('a').text, maj.select_one('span').text])
print(major)
