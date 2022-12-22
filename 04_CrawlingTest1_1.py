##test1) html 문서내에 id가 cook인 태그내의 내용을 출력해주세요.

import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
result = soup.find(id="cook")

print(result.text)


