##test2) html문서내에 Table 내에 th와 td에 있는 값들을 크롤링해 아래와 같은 딕셔너리 형태를 만들어보세요
##결과 : [{'이름':'이몽룡','나이':'34'},{'이름':'홍길동','나이':'23'}]

import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)
soup = BeautifulSoup(response.text,"html.parser")

key = []
value = []

for element in soup.find("table").find_all("th") :
    key.append(element.text)

for element in soup.find('table').find("tbody").find_all("tr") :
    temp = []
    for td_element in element.find_all('td') :
        temp.append(td_element.text)
    #value.append(temp) 이것을 딕셔너리 형태로 만들려면
    value.append(dict(zip(key,temp))) 
print(value)
