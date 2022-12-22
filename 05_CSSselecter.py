# soup.select_one(셀렉터) - 셀렉터에 일치하는 하나의 태그만 리스트로 표현
# select_one.~text는 가능 
# soup.select(셀렉터) - 셀렉터에 일치하는 모든 태그 리스트로 표현 
# select.~text 는 불가능 찾고 싶으면 [위치]해서 찾아야함.
import requests

from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/02/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
result = soup.select("#title")
result1 = soup.select("title")
result2 = soup.select("#content")
result3 = soup.select(".blue")
result4 = soup.select(".bold.blue")
result5 = soup.select("div#title.bold.blue")
print(result[0])
print(result[0].text)
print(result1)
print(result2)
print(result3)

for element in result3 :
    print(element.text)


result6 = soup.select("a[href]")
result7 = soup.select('a[href$=".com"]')
result8 = soup.select('a[target = "_blank"]')
print(result6)
print(result7)
print(result8)
print('--------------')

result9 = soup.select('div#winter p') #후손셀렉터 
result0 = soup.select('div#winter > p') #후손셀렉터 
print(result9)
print('--------------')
print(result0)