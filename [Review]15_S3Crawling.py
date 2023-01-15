import awscli
import datetime
import boto3
import requests
import json
from bs4 import BeautifulSoup

s3 = boto3.resource('s3')
##파일 업로드 
# data = open('13_AsynchronousSiteTest_1.json','rb')
# s3.Bucket('zoomstudy').put_object(Key = 'python/13_AsynchronousSiteTest_2.json', Body = data )

##파일 다운로드
# s3.Bucket('zoomstudy').download_file('13_AsynchronousSiteTest_1.json','13_newsCrawling.json')

##test ) 일주일 뉴스 타이틀과 요약내용 크롤링 해서 날짜별로 파일을 만들어 s3스토리지에 저장하기


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}


date = datetime.datetime.strptime('20230114','%Y%m%d')

for i in range(7):
    date_str = date.strftime('%Y%m%d')
    page = 1

    news = []

    while True:
        

        print(date_str, page)
        
        
        url = f'https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=003&date={date_str}&page={page}'


                
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        if str(page) != soup.select_one('div.paging strong').text.strip():
            break


        for news_data in soup.select('ul.type06 li') :
            news.append({
                'title':news_data.select('a')[-1].text.strip(),
                'body':news_data.select_one('span.lede').text.strip()
            })
        
        page += 1
        
        

    s3.Bucket('zoomstudy').put_object(Key = f'news/{date_str}.json',Body = json.dumps(news, ensure_ascii= False))
    
    date = date - datetime.timedelta(days=1)