#뉴스 크롤링
#https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&oid=003
#매체의 어제일자 모든 기사를 아래와 같이 제목과 본문을 분류하여 크롤링해주세요.


import requests
import datetime
from bs4 import BeautifulSoup

date = datetime.datetime.strptime('20211120', '%Y%m%d')

for i in range(20) :
    
    print("================================")
    print("================날짜 :", date.strftime('%Y%m%d'))
    print("================================")
    
    page = 1

    while True : 
    
        date_str = date.strftime('%Y%m%d')   
        URL = f'https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=003&date={date_str}&page={page}'
        # 접속이 안될 경우 network -> 맨처음켜진 거에서 header- request 내용을 그대로 복사한 뒤 header ={안에 내용붙여넣기 }
        headers = {
        #    ':authority' : 'news.naver.com',
        #    ':method' : 'GET',
        #    ':path' : '/main/list.naver?mode=LPOD&mid=sec&oid=003&date=20221221',
        #    ':scheme' : 'https',
        #    'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        #    'accept-encoding' : 'gzip, deflate, br',
        #    'accept-language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        #    'cookie' : 'JSESSIONID=81E5E5463D5F186F02270B80CA4D606B; NNB=QZVMCT3VJT7WE; NID_AUT=1ieukToC/zYBtKmoyq4Yzv2UraM1B2Eew4eBomPxUeQeI0X62WLOspry6M+wesLM; NID_JKL=PJEA6quxYqQRuuecM2gypn5fFi0Y2XX/z0gme9psUic=; ASID=d3d2e59c00000183e5a5650a00000056; _ga=GA1.1.2039777440.1661235595; _ga_8P4PY65YZ2=GS1.1.1669110661.4.0.1669110661.0.0.0; nx_ssl=2; page_uid=hInzsdprvN8ssBtH3XNssssstB4-145786; NID_SES=AAABoGanpSfLna+MzLw1KpNVYoKBnyNJ0ptRmTlM90VXqskfhBgzuIau5SFCA/JlH7+kEUGdJfLi0fb6qey2wOhmsNx1OETinq2QPXZKjX+l42zsh1Oz6e+lQIi5KRC8VJWN8QfrBfXZCtcU3fk/KnreK45RxsMql2h1+2gNoPJdRqE4ul7gvxxgekisodcZyZSelzWOhqTfeLzCEywVqB4gObjHrqls2C9QUQXCASyTHkl/5VfhN2tTID9+UGPHVoE2nysNJwjUWhdh1F5haZP2V0hjcY4A6j5xKvgvNHvRPRipF/csK1SAVgwkBQ1nAr+woOi3Cmzv1zoEGF8OCD/ZsTJljAXoBgrExEtq3SY60KHd3G0r6U3jsXi1FH3F4e2JOYfgeNukSIaK0roiM5DElNKQEkmm7o5w9lgKcmzJuqxl8Mog7emjVNXEBfujMMJnbE3vRBstybpkU+OnOldZPBV97Mj9PKC5o+ObWh1YFjuoyW4VYFov3vPaChubKesM4KRg1YRJSNDwS8P7s/OWpZsELDpWy9yeGvYOdrq6J1bR',
        #    'referer' : 'https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=003',
        #    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        #    'sec-ch-ua-mobile': '?0',
        #    'sec-ch-ua-platform' : '"Windows"',
        #    'sec-fetch-dest' : 'document',
        #    'sec-fetch-mode': 'navigate',
        #    'sec-fetch-site': 'same-origin',
        #    'sec-fetch-user': '?1',
        #    'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
            }
        response = requests.get(URL,headers = headers)
        #print(response.text)
        ## url을 적은 뒤 한번 프린트 해보기 안될경우 headers 추가해줘야함 ...! 
        ## 대부분 user-agent가 없어서 실행안되는거 
        soup = BeautifulSoup(response.text, 'html.parser')
        
        print("================================")
        print("================현재페이지 :", page)
        print("================================")
    ## 마지막 페이지는 출력 안되게 하기 ----
        #print(page)
        #print(soup.select_one('div.paging > strong').text)
        
        if str(page) != soup.select_one('div.paging > strong').text:
            print('크롤링완료')
            break
    ## 마지막 페이지는 출력 안되게 하기 ----
        for news_item in soup.select('div.list_body ul li') :
            #print(news_item.select('dt')[1].select_one('a').attrs['href'])
            #print(news_item.select('dt')[1].select_one('a').text.strip())
            
            ## 런타임 오류가 났을 때 예외 된 처리들은 except문을 진행해 해결
    ##('dt')[0]은 기사사진 [1]은 제목이었는데 기사사진이 없을 경우 [0]이 제목이 되면서 런타임 오류가 발생했었음        
            news_url = '' 
            
            try :
                news_url = news_item.select('dt')[1].select_one('a').attrs['href']
            except :
                news_url = news_item.select('dt')[0].select_one('a').attrs['href']
    ##('dt')[0]은 기사사진 [1]은 제목이었는데 기사사진이 없을 경우 [0]이 제목이 되면서 런타임 오류가 발생했었음     
            response = requests.get(news_url, headers = headers)    
            news_soup = BeautifulSoup(response.text, 'html.parser')
            
            title = ''
            body = ''
            
            try :
                #일반기사
                title = news_soup.select_one('div#ct h2#title_area').text.strip()
                body = news_soup.select_one('div#dic_area').text.strip()
            except :
                
                try:
                    #스포츠 기사 
                    title = news_soup.select_one('div.news_headline h4.title').text.strip()
                    body = news_soup.select_one('div#newsEndContents').text.strip().replace('\n','')
                except :
                    #연예기사             
                    title = news_soup.select_one('div.end_ct_area h2.end_tit').text.strip()
                    body = news_soup.select_one('div.end_body_wrp div#articeBody').text.strip()
            
            
            print(title)
            print('')
            print(body)
            print('')
            print('')
    
        
        page +=1
    date = date - datetime.timedelta(days=1)
        