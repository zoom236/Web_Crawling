import requests
import datetime
from bs4 import BeautifulSoup

#어제일자 모든 기사, 제목과 본문 분류 
date = datetime.datetime.strptime('20221230','%Y%m%d')

page = 1
for i in range(20):
    
    print("=======================================")
    print("===============날짜 : ", date.strftime('%Y%m%d'))
    print("=======================================")
    
    
    while True :
        date_str = date.strftime('%Y%m%d')
        url = f'https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=003&date={date_str}&page={page}'

        headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        
       
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        print(f'================== page {page}')
        if str(page) !=soup.select_one('div.paging > strong').text :
            print('크롤링완료')
            break
        for news in soup.select('div.list_body ul li') :
            try :
                response = requests.get(news.select('dt')[1].select_one('a').attrs['href'],headers=headers)
            # print(news.select('dt')[1].select_one('a').text.strip())
            except:
                response = requests.get(news.select('dt')[0].select_one('a').attrs['href'],headers=headers)


            media = BeautifulSoup(response.text,'html.parser')
            
            try : 
                #일반기사 
                print(media.select_one('h2#title_area').text.strip())
                print('')
                print(media.select_one('div#dic_area').text.strip().replace('\n',''))
                print('')
            except:
                
                try :
                    #연예기사
                    print(media.select_one('div#content h2.end_tit').text.strip())
                    print('')
                    print(media.select_one('div#articeBody').text.strip().replace('\n',''))
                    print('')
                except:
                    #스포츠기사
                    print(media.select_one('div#content h4.title').text.strip())
                    print('')
                    print(media.select_one('div#newsEndContents').text.strip().replace('\n',''))
                    print('')
        page +=1
                    
    date = date - datetime.timedelta(days=1)