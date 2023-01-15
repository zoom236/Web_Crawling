import requests
import json
import pymysql
from bs4 import BeautifulSoup


db = pymysql.connect(host = 'localhost', port= 3306, user = 'study', passwd= 'study', db = 'study', charset = 'utf8')
cursor = db.cursor()

for page in range(1,11) :
    
    response = requests.get(f'https://www.rocketpunch.com/api/jobs/template?page={page}&q=')
    soup = BeautifulSoup(response.json()['data']['template'],'html.parser')
    for recruit in soup.select('div.company.item') :
        name = recruit.select_one('div.company-name strong').text
        description = recruit.select_one('div.description').text.replace('👋','')
               
        
        cursor.execute("""
            INSERT INTO company(name, description)
            VALUES (%s,%s)
        """,(name,description))
        db.commit()
        
        company_id = cursor.lastrowid
        
        
        for detail in recruit.select('div.company-jobs-detail div.job-detail'):
            title = detail.select_one('a').text
            info= detail.select_one('span.job-stat-info').text
            date= detail.select_one('div.job-dates > span').text.strip()
            
            job_detail_sql = """
                INSERT INTO job(company_id, title, info, date)
                VALUES (%s,%s,%s,%s)
            """
            
            cursor.execute(job_detail_sql,(company_id,title,info,date))
            db.commit()
        