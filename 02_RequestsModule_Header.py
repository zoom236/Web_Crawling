import requests

URL = 'http://httpbin.org/get'

params = {'data1':'data1', 'data2':'data2'}
headers = {'content-Type':'application/json; charset=utf-8', 'test':'test'}
response = requests.get(URL, params=params,headers=headers)

print(response.text)

