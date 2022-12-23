import pymysql


###mysql 접속 
# db = pymysql.connect(host = 서버IP, Port = 포트 , user = 아이디, passwd = 패스워드, db = db명, charset = 'utf8')

db = pymysql.connect(host = 'localhost', port = 3306, user = 'study', password = 'study', db = 'study', charset = 'utf8')

cursor = db.cursor()

###테이블 생성 

#sql = """
#CREATE TABLE python(
#    name varchar(20) NOT NULL,
#    math int null,
#    science int null,
#    PRIMARY KEY (name)
#)
#"""

#cursor.execute(sql)
#db.commit()

###테이블에 데이터 입력 

#sql = """
#INSERT INTO python
#VALUES ('홍길동', 20, 50)
#"""

#cursor.execute(sql)
#db.commit()


#sql = """
#INSERT INTO python
#VALUES ('이몽룡', 60, 20)
#"""

#cursor.execute(sql)
#db.commit()

###데이터 삭제

sql = """
DELETE FROM python
WHERE name ='이몽룡'
"""

cursor.execute(sql)
db.commit()



###데이터 조회

sql = """
SELECT *
    FROM python
"""
cursor.execute(sql)
rs = cursor.fetchall()


print(rs)
