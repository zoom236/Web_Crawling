## test1) 사이트 내에 인기 검색종목과 주요해외지수를 각각 크롤링하여 종목명과 
##        주가지수를 아래와 같이 리스트로 정리해주세요.
## 결과 : [['써니전자','5,000'],['삼성전자','55,200']]~
## 연습사이트 : https://crawlingstudy-dd3c9.web.app/03/

import requests
from bs4 import BeautifulSoup

URL ='https://crawlingstudy-dd3c9.web.app/03/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

popular = []

for item in soup.select('#popularItemList > li') :
    popular.append([item.select_one('a').text,item.select_one('span').text])

print(popular)
print('----------')

major = []

for item in soup.select('.lst_major> li') :
    major.append([item.select_one('a').text,item.select_one('span').text])

print(major)
