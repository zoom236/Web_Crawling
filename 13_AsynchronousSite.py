#비동기사이트 크롤링
#연습 사이트 : https://crawlingstudy-dd3c9.web.app/04/

 
import requests

# response = requests.get('https://crawlingstudy-dd3c9.web.app/04/') - 출력해보니 크롤링할 데이터가 없음.  
response = requests.get('https://jsonplaceholder.typicode.com/posts') # json형태의 데이터 
datas = response.json() #딕셔너리 형태로 바꿔주기 → .json
print(type(datas)) #출력 결과 : list 

for data in datas:
    print(data['title'])
    print(data['body'])
    print('')
    
#---------------------------------------------- json 모듈 사용 
    
#json : 자바스크립트 객체 문법을 따르는 문자기반의 데이터 포맷 , 파이썬의 딕셔너리 형태와 비슷 
#json 형태 데이터를 파이썬 딕셔너리로 바꾸는 방법
# import json 
# json.loads

#json.dump() - list나 딕셔너리를 json파일로 저장
#json.load() - json 파일 읽기 

#import requests
import json

response2 = requests.get('https://jsonplaceholder.typicode.com/posts')
datas1 = json.loads(response2.text)

print(json.dumps(datas1))

with open('data.json','w') as json_file:
    json.dump(datas1, json_file)