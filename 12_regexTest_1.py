#test 휴대폰 번호만 추출해주세요

import re

number ="""
010-2334-3234
02-302-3033
010-1321-4043
02-01-32
33-3303-3033
016-444-3042
"""

print(re.findall("[0-9]{3}-[0-9]{3,4}-[0-9]{4}", number))

for number in re.finditer("[0-9]{3}-[0-9]{3,4}-[0-9]{4}", number) :
    print(number.group())