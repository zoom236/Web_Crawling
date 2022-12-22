import requests

URL = 'http://httpbin.org/get'

params = {'data1':'data1', 'data2':'data2'}
response = requests.get(URL, params=params)

print(response.text)

######################################################
##위와 같은 값이 나옴, 위에 코드가 더 깔끔 

# URL = 'http://httpbin.org/get?data1=data2&data2=data2'

# response = requests.get(URL)

# print(response.text)

