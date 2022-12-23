#test3) 텍스트 중에 <내용> 괄호로 묶여진 텍스트를 괄호 포함 모두 제거해주세요.

import re

text = '안녕하세요 저는 <em>홍길동</em> 입니다. 나이는 24살 세계 최고의 <a href="aa.aa.com">데이터 분석가</a>가 되고싶습니다.'

text = re.sub("<[^>]*>","",text)
print(text)
