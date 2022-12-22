import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01'
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
result = soup.find("title")
print(result)
print(result.text)

result1 = soup.find("p") #가장 상단에 있는 태그 하나만
result2 = soup.find_all("p",limit=2)#일치하는 모든태그 (limit : 가져올 개수 제한, 생략가능)

result3 = soup.find("th","tablehead")#옵션값이 class가 tablehead인것
result4 = soup.find("th", class_="tablehead") #옵션값이 class가 tablehead인것 위의 문장이랑 같은 결과
result5 = soup.find("th", attrs = {"class":"tablehead"}) # 옵션값 class가 tablehead인것(옵션명 변경가능)
result6 = soup.find("h1", attrs = {"title": "welcome"})#옵션값 title이 welcome인것 (옵션명 변경가능)
result7 = soup.find(id="hello")#옵션값이 id가 hello인것 

print(result1) #result1~7 넣어서 결과 보기 

##결과값 내에서 다시 검색 

result8 = soup.find("table")
result9 = result8.find("tbody")
#result8 = soup.find("table").find("tbody") 해도 같은 결과값 

print(result8)
print("---------")
print(result9)
##result.text : 태그내에 내용만 추출 
##result.attrs["옵션명"] : 태그내에 옵션을 추출 
print("---------")
result0 = soup.find('a')
print(result0.attrs['href'])
print(result0.text)
