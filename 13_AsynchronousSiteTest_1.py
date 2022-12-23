#Test1) 아래 사이트를 크롤링하여 아래와 같이 각각 글에 id와 title 그리고 글마다 코멘트내용을 리스트 형식으로 담고 최종 json파일 형태로 저장해보시오.
#연습 사이트 : https://crawlingstudy-dd3c9.web.app/05 

import requests
import json 

#response = requests.get('https://crawlingstudy-dd3c9.web.app/05')
#print(response.text) #확인 결과 내용이 없음 

response = requests.get('https://jsonplaceholder.typicode.com/photos')

datas = []

for idx, data in enumerate(response.json()) :
    
    if idx ==3 :
        break
    
    temp ={
        'id' : data['id'],
        'title' : data['title'],
        'comment' : []
    }
    
    
    comments = requests.get('https://jsonplaceholder.typicode.com/comments', params ={
        'postId' : data['id']
    });
    
    for comment in comments.json() :
        temp['comment'].append(comment['body'])
    
    datas.append(temp)

with open("13_data.json","w") as json_file1 : 
    json.dump(datas,json_file1)
print(datas)