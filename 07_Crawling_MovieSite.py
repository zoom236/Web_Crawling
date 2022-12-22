import requests
from bs4 import BeautifulSoup

URL = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'
response = requests.get(URL)
print(response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')
for movie in soup.select('table.list_ranking tr td.title'):
    print(movie.text.strip())
    
## 순위 까지 가지고 오고 싶으면 
for i, movie in enumerate(soup.select('table.list_ranking tr td.title')):
    print(i + 1, movie.text.strip())
    
##enumerate = 인덱스 번호 붙이기 0번부터 붙이기때문에 +1 해준거 