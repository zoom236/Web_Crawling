import requests
session = requests.Session()


session.get('https://naver.com')
print(session.cookies.get_dict())
session.get('https://naver.com')
print(session.cookies.get_dict())
#쿠키 추가
#쿠키는 도메인 별로 관리를 함 
session.cookies.set("COOKIE_NAME","value", domain = 'naver.com')
print(session.cookies.get_dict())