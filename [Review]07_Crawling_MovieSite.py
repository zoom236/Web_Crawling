import requests
from bs4 import BeautifulSoup

URL = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'
response = requests.get(URL)
soup = BeautifulSoup(response.text,'html.parser')

for idx, movie in enumerate(soup.select('#old_content .list_ranking tr > td.title')):
    print(idx +1, movie.select_one('a').attrs['title'])
