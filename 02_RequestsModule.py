import requests

URL = 'http://httpbin.org/get'

response = requests.get(URL)

print(response.status_code) ## 200 : 정상 작동  
print(response.text) ## json형식 key: value

response = requests.post('http://httpbin.org/post')

##크롤링은 대부분 get방식 이용하고 post를 가끔 이용 /get, post는 웹브라우저로 불러 올 수 없음 - python 이용
##get방식은 파라메타 방식으로 이용 URL = 'http://httpbin.org/post?key = value?key=value'

print(response.status_code)
print(response.text)

response = requests.put('http://httpbin.org/put') ##수정할 때 사용

print(response.status_code)
print(response.text)


response = requests.delete('http://httpbin.org/delete')

print(response.status_code)
print(response.text)
