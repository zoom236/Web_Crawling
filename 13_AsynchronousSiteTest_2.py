# test2) 아래 url의 뉴스기사 본문에 기사제목, 기사내용, 사람들반응, 댓글을 모두 크롤링하여 json 파일 형태로 저장해주세요.
#연습 사이트 : https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=101&oid=011&aid=0003987613


import requests
import json
import re
from bs4 import BeautifulSoup
 

URL = 'https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=101&oid=011&aid=0003987613'
#URL2를 봤을 때 ne_011_0003987613 반복 되는 것을 알 수 있고,oid, aid와 같은 것을 볼 수 있다. 따라서 Oid와 aid를 바꾸면 다른 기사로 바뀜 

oid = re.search("(?<=oid=)[0-9]+",URL).group()
aid = re.search("(?<=aid=)[0-9]+",URL).group()

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
response = requests.get(URL,headers=headers)
soup = BeautifulSoup(response.text,"html.parser")

title = soup.select_one('div.media_end_head_title h2#title_area').text.strip()
content =soup.select_one('div#contents div#dic_area').text.strip()


news = {
    'title' : title,
    'content' : content,
    'reaction' : {
        'sad' : 0,
        'like' : 0,
        'warm' : 0,
        'want': 0,
        'angry' : 0
    },
    'comments': []
}
#URL2 ='https://news.like.naver.com/v1/search/contents?suppress_response_codes=true&callback=jQuery331027309651910029653_1671772580393&q=JOURNALIST[69146(period)]|NEWS[ne_011_0003987613]|NEWS_MAIN[ne_011_0003987613]&isDuplication=false&cssIds=MULTI_MOBILE,NEWS_MOBILE&_=1671772580394'
# print(reponse2.text)를 했을 때 json형태 끝에 ; 있는 것을 보고 함수가 있다는 것을 알 수 있었음.
# 결과 일부 : "mobile","applyYn":null}]});
# 함수를 지워야 하기 때문에 위에서 지워봐야함 callback=jquery가 함수 같으니 지워보기 

URL2 = f'https://news.like.naver.com/v1/search/contents?suppress_response_codes=true&q=JOURNALIST[69146(period)]|NEWS[ne_{oid}_{aid}]|NEWS_MAIN[ne_{oid}_{aid}]&isDuplication=false&cssIds=MULTI_MOBILE,NEWS_MOBILE&_=1671772580394'
response2 = requests.get(URL2)
for reaction in response2.json()['contents'][1]['reactions'] :
    news['reaction'][reaction['reactionType']] = reaction['count']  
    print(reaction)
headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=QZVMCT3VJT7WE; NID_AUT=1ieukToC/zYBtKmoyq4Yzv2UraM1B2Eew4eBomPxUeQeI0X62WLOspry6M+wesLM; NID_JKL=PJEA6quxYqQRuuecM2gypn5fFi0Y2XX/z0gme9psUic=; ASID=d3d2e59c00000183e5a5650a00000056; _ga=GA1.1.2039777440.1661235595; _ga_8P4PY65YZ2=GS1.1.1669110661.4.0.1669110661.0.0.0; nx_ssl=2; page_uid=hIfPHlprvmZssDF9Gv0ssssstyh-154532; NID_SES=AAABoDtYo64RCioyZQrYu5uRDnz9/qdPLBQjfrgU1H959JHkED250tcT0iCuT2mU3aCMA2R0+Plj7x3zUIdFyKn9wmrYNwlNuBJxOH6mYLBlyUZPmpdwgcEOg2qXx+B2koJVewLprFTzhhre2oP7mxfy9Z3FJyJub6b9h+pHzKLpI8Y08k/CQMqkDE2cZCZdQjCFteulLSJVcEhtQt5j/DMWbV+quch2z3k6Ni69bU1t+gGM8AYv/ZRz8PoizaFHEsKdlRcE9yUR5C9gWYgbsqlrYIi9ryss89yTLSw9OASIeL/2gMWab74UTWsbvbGxVx6ROEYF+rF4FW6pqjJzMx2ahJFSvHbjGVxXaEt99TKG9caYdKaxnviqT3lk2MVnlazr3wcqlMRdOjl5HV3al0ZoDrbytLUc6wRgjfHxJ2ZwhvZxUwDP3aYUm6epanNhxrWuOZRZGvXN/3v2Z6H+bFreDjYr0AOuRC84mTy7had2qEKxR2UUo3bj5TKbF3Y63ECCMKFOKBLSUbxzCUmBDFUH35KIZg0X8KDCJbTYrDuKj7WT; BMR=',
    'referer': 'https://n.news.naver.com/mnews/article/comment/011/0003987613?sid=101',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}


## 코멘트 내용 변함 x for문에 웹사이트 주소 문제인 것 같음. 공통점 찾아서 고쳐야함 
response = requests.get(f'https://cbox5.apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=news&templateId=default_economy&pool=cbox5&_cv=20221222141657&lang=ko&country=KR&objectId=news{oid},{aid}&categoryId=&pageSize=20&indexSize=10&groupId=&listType=OBJECT&pageType=more&page=1&initialize=true&userType=&useAltSort=true&replyPageSize=20&sort=FAVORITE&includeAllStatus=true&_=1671778283159',headers = headers)
lastpage = json.loads(response.text.replace('_callback(','')[:-2])['result']['pageModel']['lastPage']

for page in range(1, lastpage + 1):
    response =requests.get(f'https://cbox5.apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=news&templateId=default_economy&pool=cbox5&_cv=20221222141657&lang=ko&country=KR&objectId=news{oid},{aid}&categoryId=&pageSize=20&indexSize=10&groupId=&listType=OBJECT&pageType=more&page={page}&initialize=true&userType=&useAltSort=true&replyPageSize=20&sort=FAVORITE&includeAllStatus=true&_=1671778283159',headers = headers)
    for comment in json.loads(response.text.replace('_callback(','')[:-2])['result']['commentList']:
        news['comments'].append(comment['contents'].strip())
   
with open('13_AsynchronousSiteTest_2.json','w',encoding ='utf8') as json_file:
    json.dump(news,json_file,ensure_ascii=False)

print(news)