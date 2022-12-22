##test 3) 사이트 내에 인기검색종목과 주요해외지수를 각각 상한가인 종목만 
##        크롤링 하여 종목명과 주가지수를 아래와 같이 리스트로 정리해주세요.
##    결과 : [['써니전자','5,000'],['안랩','81,000']]~

import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/03/'
response = requests.get(URL)
soup = BeautifulSoup(response.text,'html.parser')

popular = []

for item in soup.select('#popularItemList > li') :
    if item.select_one('img').attrs['alt'] == '상한' :
        popular.append([item.select_one('a').text,item.select_one('span').text])

print(popular)

major = []

for item in soup.select('.lst_major > li') :
    if item.select_one('img').attrs['alt'] == '상한' :
        major.append([item.select_one('a').text,item.select_one('span').text])

print(major)