##test3) html 문서내에 모든 a태그에 링크된 페이지에 있는 내용을 읽어 출력해주세요
##결과 : 크롤링 연습사이트 01-1 페이지입니다.
##       크롤링 연습사이트 01-2 페이지입니다.
##       크롤링 연습사이트 01-3 페이지입니다.
##       크롤링 연습사이트 01-4 페이지입니다.

import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

for atag in soup.find_all('a') :
    response2 = requests.get('https://crawlingstudy-dd3c9.web.app/01/' + atag.attrs['href'])
    soup = BeautifulSoup(response2.text,'html.parser')
    print(soup.find('p').text.strip())
    #print(soup.find('p').text) 공백이나 엔터도 출력됨 
