#기사제목, 기사내용, 사람들반응, 댓글 모두 크롤링하여 json파일형태로 저장
import requests
import re
from bs4 import BeautifulSoup
import json


article = '011'
article_num ='0003987613'
page = '1'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

url = f'https://n.news.naver.com/mnews/article/{article}/{article_num}?sid=101'
response = requests.get(url,headers = headers)
soup = BeautifulSoup(response.text, 'html.parser')

## 다른기사도 크롤링하기 위해 중복되는 부분 가져온 것 
article = re.search("(?<=article\/)[0-9]+",url).group()
article_num = re.search("[0-9]+(?=\?sid)",url).group()
##

news ={
    'title': soup.select_one('#title_area span').text.strip(),
    'content' : soup.select_one('#dic_area').text.strip(),
    'reaction' : {
        'sad' :0,
        'like':0,
        'warm':0,
        'want':0,
        'angry':0,
        }, 
    'comments' : []
}

url = f'https://news.like.naver.com/v1/search/contents?suppress_response_codes=true&q=JOURNALIST%5B69146(period)%5D%7CNEWS%5Bne_{article}_{article_num}%5D%7CNEWS_MAIN%5Bne_{article}_{article_num}%5D&isDuplication=false&cssIds=MULTI_MOBILE%2CNEWS_MOBILE&_=1672997339735'

response = requests.get(url)
for reaction in response.json()['contents'][1]['reactions'] :
    news['reaction'][reaction['reactionType']] =  reaction['count']

## 다른기사도 크롤링하기위해 중복되는 부분 가져온 것 
article = re.search("(?<=Bne_)[0-9]+",url).group()
article_num = re.search("(?<=Bne_..._)[0-9]+",url).group()
##

headers = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
'cookie': 'NNB=74SF2VF2XKVGG; nx_ssl=2; ASID=d3d2e59c00000185533303da00000050; nid_inf=1209947340; NID_AUT=qZWBB/tA3OOqC6oQpe8C0ZwEWMyG7NgGSKpC1/V1dUEduAUSrz2arz8+RKPnpLAP; NID_JKL=DA36I4Jf9/RNDHXUu8J314YsOT8j2yyv29idTZjbmRs=; NID_SES=AAABoWzOZa+CW+TyNeF04Qq+B89B7MR+so9qPRv/kkXqyP8GWSJk5v9bguptK/rrM1S1oH5eWyQSrp9+HHwV/HGAX4kYMPiv8wIWPbpjdjMEPa18180LxdiXV6anul18BLNHDC/ZC9AQQlEH4RqxFip57G2JoDubKrBtMI3G6Vfnp4OD0mXC9xKUecXfty7iHiqTGyNRYm9gwMutFDplyFCE/A/Sx7FYQhdbXzBOGnafdensoeJA7WnJ852am6sRv8FiAR+7MxCQSHQ4jA1xH6vFpFvI9xmkhbUxC1yEAGPruBZoYnLMD57ouvzhEIOXnpxv4nvUyaDCS8aqdFkjzkzl6/SkzniMzDVbU+V6AWXDGlADepPj9Rl3fEmQroobe+9P3rkcPsPWvE/72++EWIF2+yspWTfTgP9I+aGY2OrsOm9kOlUC8lqdP07nTJaz3rVRO+DKdJUeYsh07MEBLq03fXDdXN/Dmmux+9yTMAt5IU0MJZHCWIWfX2d0eraa+cQt5i68xqdYOEsLqQmEE6KtT7ehZM43spQ1ElybnL3OKYUOQEMmRIM0la0hCxKg0xRnDw==; BMR=',
'referer': f'https://n.news.naver.com/mnews/article/comment/{article}/{article_num}?sid=101',
'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'script',
'sec-fetch-mode': 'no-cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

}

url = f'https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=news&templateId=default_economy&pool=cbox5&_cv=20230103135602&lang=ko&country=KR&objectId=news{article}%2C{article_num}&categoryId=&pageSize=20&indexSize=10&groupId=&listType=OBJECT&pageType=more&page=2&currentPage=1&refresh=false&sort=FAVORITE&current=2682092863&prev=2682084903&moreParam.direction=next&moreParam.prev=100004i00005605mvbfmycethd&moreParam.next=100000200000405mvbm94jvi84&includeAllStatus=true&_=1673006348978'
response = requests.get(url,headers=headers)
lastpage =json.loads(response.text.replace('_callback(','')[:-2])['result']['pageModel']['lastPage']
nextpage =json.loads(response.text.replace('_callback(','')[:-2])['result']['morePage']['next']
current =json.loads(response.text.replace('_callback(','')[:-2])['result']['pageModel']['current']

for page in range(1,lastpage + 1) :
    # url = f'https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=news&templateId=default_economy&pool=cbox5&_cv=20230103135602&lang=ko&country=KR&objectId=news{article}%2C{article_num}&categoryId=&pageSize=20&indexSize=10&groupId=&listType=OBJECT&pageType=more&page={page}&currentPage={page-1}&refresh=false&sort=FAVORITE&current=2682640283&prev=2682084903&moreParam.direction=next&moreParam.prev=100004i00005605mvbfmycethd&moreParam.next=100000000000005mvnj892qb7o&includeAllStatus=true&_=1673006348980'
    url = f'https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=news&templateId=default_economy&pool=cbox5&_cv=20230103135602&lang=ko&country=KR&objectId=news{article}%2C{article_num}&categoryId=&pageSize=20&indexSize=10&groupId=&listType=OBJECT&pageType=more&page={page}&currentPage={page-1}&refresh=false&sort=FAVORITE&current=2682092863&prev=2682084903&moreParam.direction=next&moreParam.prev=100004i00005605mvbfmycethd&moreParam.next={nextpage}&includeAllStatus=true&_=1673006348978'
    for comment in json.loads(response.text.replace('_callback(','')[:-2])['result']['commentList']:
        news['comments'].append(comment['contents'].strip())

with open('13_AsynchronousSiteTest_2.json','w',encoding = 'utf8') as json_file :
    json.dump(news, json_file, ensure_ascii=False)
