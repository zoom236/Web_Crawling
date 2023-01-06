import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/photos')

datas=[]

for idx, data in enumerate(response.json()) :
    if idx == 100 :
        break
    
    print(idx)
    
    temp = {
        'id' : data['id'],
        'title' : data['title'],
        'comment' : []
    }
    
    comments = requests.get('https://jsonplaceholder.typicode.com/comments', params = {'postId' : data['id']})
    for comment in comments.json():
        temp['comment'].append(comment['body'])
    
    datas.append(temp)

with open("13_AsynchronousSiteTest_1.json", "w") as json_file :
    json.dump(datas,json_file)

print(datas)