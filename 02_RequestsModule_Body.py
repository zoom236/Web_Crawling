import requests

URL = 'http://httpbin.org/post'

params = {'data1':'data1', 'data2':'data2'}
headers = {'content-Type':'application/json; charset=utf-8', 'test':'test'}
data = {'data1':'data1','data2':'data2'}
response = requests.post(URL, params=params,headers=headers, data=data)
## data를 보낼 때는 post방식으로 변경해줘야함 , get방식은 body를 사용할 수 없음 
print(response.text)

