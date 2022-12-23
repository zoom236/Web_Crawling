#Test1) 아래 채용사이트의 채용정보 10페이지를 크롤링하고 (회사명, 회사설명, 채용정보(회사별 여러개)) 해당 데이터를 데이터베이스에 저장해주세요.
#https://www.rocketpunch.com/jobs

import requests
from bs4 import BeautifulSoup
import json
import pymysql

db = pymysql.connect(host = 'localhost', port=3306, user='study', passwd = 'study', db = 'study', charset = 'utf8')
cursor = db.cursor()

for page in range(1,11) :

    print(page)
    response = requests.get(f'https://www.rocketpunch.com/api/jobs/template?page={page}&q=') #privew안에 template이 현재 json 형태
    soup = BeautifulSoup(response.json()['data']['template'], 'html.parser')#json 형태 안에 html형태가 들어가 있는 경우 

    for company in soup.select('div.company-list div.company'):
        name = company.select_one('div.company-name h4 strong').text
        description = company.select_one('div.description').text.replace('🌏','')#.replace('🌏','')로 에러가 나올때 마다 특수문자 제거 
        #혹은 ALTER TABLE study.company CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; 로 MySQL에서 유니코드 변경 
        
        print(name)
        print(description)
        
        #company_sql = f"""
        #    INSERT INTO company(name, description)
        #    VALUES ('{name}','{description}')
        #"""
        #이렇게 입려하면 오류가 나옴 - 넣을 텍스트 안에 ' ' 가 들어가 있어서 나오는 오류 
        
        cursor.execute("""
            INSERT INTO company(name, description)
            VALUES (%s,%s)
        """,(name,description))
        db.commit()
         
        ##Table이 company, job 두개인데 company의 company_id를 job테이블이 공유하는 형식으로 제작해놔서 넣는 내용        
        company_id = cursor.lastrowid 
        
        
        for detail in company.select('div.company-jobs-detail > div.job-detail'):
            title = detail.select_one('a').text.strip()
            info = detail.select_one('span.job-stat-info').text.strip()
            date = detail.select_one('div.job-dates > span').text.strip()
            
            job_detail_sql = """
                INSERT INTO job(company_id, title, info, date)
                    VALUES (%s, %s, %s, %s)
            """
            
            cursor.execute(job_detail_sql, (company_id, title, info, date))
            db.commit()
                      
            #print('title',detail.select_one('a').text.strip())
            #print('info',detail.select_one('span.job-stat-info').text.strip())
            #print('date',detail.select_one('div.job-dates > span').text.strip())
        #print('')