## 영화랭킹을 데이터 베이스에 입력 

import requests
from bs4 import BeautifulSoup
import pymysql


url = 'http://movie.naver.com/movie/sdb/rank/rmovie.naver'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

    
db = pymysql.connect(host= 'localhost', port = 3306, user= 'study', passwd= 'study', db = 'study', charset='utf8')
cursor= db.cursor()
 
sql= """
CREATE TABLE MovieRanking (
    ranking int NOT NULL,
    name varchar(100) NOT NULL,
    primary key(ranking)
)
"""   
cursor.execute(sql)
db.commit

for idx, movie in enumerate(soup.select('.list_ranking tbody td.title')) :
    sql = f"""
    insert into MovieRanking
    Value ({idx+1},'{movie.select_one('.tit3').text.strip()}')
    """
    cursor.execute(sql)
    db.commit()

cursor.close()
db.close()
