#test2) 정상적인 이메일만 추출해주세요.

import re

mail = """
jkilee@gmail.com
kttredef@naver.com
akdeflaa.com
abkereff@aacde
adekik@best.kr
adefgree@korea.co.kr"""

result = re.finditer('.*[@].*[\.].*',  mail)

for email in result :
    print(email.group())