##Test1) 아래 url의 영화랭킹을 데이터베이스에 입력해주세요.
## url : https://movie.naver.com/movie/sdb/rank/rmovie.nhn

import requests
from bs4 import BeautifulSoup
import pymysql

URL = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
response = requests.get(URL)
soup = BeautifulSoup(response.text,'html.parser')


db = pymysql.connect(host = 'localhost', port = 3306, user = 'study', passwd= 'study', db = 'study', charset = 'utf8')
cursor = db.cursor()



for idx, movies in enumerate(soup.select('table.list_ranking td.title')) :
    
    sql= f"""
        INSERT INTO movie
        VALUES ({idx+1},'{movies.text}')
    """
    cursor.execute(sql)
    db.commit()
    
   # print(idx+1,movies.text.strip())

cursor.close()
db.close()

    

