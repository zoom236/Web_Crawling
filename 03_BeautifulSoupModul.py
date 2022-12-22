##BeautifulSoup 모듈은 Html에서 손쉽게 원하는 데이터를 가져올 수 있도록 지원해주는 모듈 

import requests

from bs4 import BeautifulSoup #bs4 내에 BeautifulSoup을 추가해줘 

URL = 'https://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL) #위 url접속 
soup = BeautifulSoup(response.text, 'html.parser') #매개변수 1 : html문서, 매개변수 2: 어떤 parser을 사용할 건지 우리는 html 문서 내에서 데이터를 가져올 것이므로 html.parser 
result = soup.find('title') #위 웹페이지에서 title태그의 내용을 찾아줘

print(result)
print(result.text) #태그없이 title 내용만 가져와줘 