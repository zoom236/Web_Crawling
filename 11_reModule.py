## re 모듈

import re


##re.match("찾고 싶은 문자열/정규표현식",text) : 문자열 처음부터 매치여부 조사. 객체리턴
text = "I like orange! I love orange!"
result = re.match("orange",text)
print(result)

# None 출력

text1 = "orange I like orange! I love orange!"
result1 = re.match("orange",text1)
print(result1)
#<re.Match object; span=(0, 6), match='orange'> 객체 리턴 

print(result1.group())
print(result1.start())
print(result1.end())
print(result1.span())



#re.search("찾고 싶은 문자열 / 정규표현식", text) : 문자열 전체를 조사. 처음 검색된 최초 문자열 객체 리턴
text3 = "I like orange! I love orange!"
result3 = re.search("orange",text3)
print(result3)
print(result3.group())
print(result3.start())
print(result3.end())
print(result3.span())


#re.findall("찾고 싶은 문자열 / 정규표현식", text) : 매치되는 모든 문자열 리스트로 리턴
text4 = "I like orange! I love orange!"
result4 = re.findall("orange",text4)
print(result4)


#re.finditer("찾고싶은 문자열/ 정규표현식",text) : 매치되는 모든 문자열의 반복 가능한 객체로 리턴

text5 = "I like orange! I love orange!"
result5 = re.finditer("orange",text5)
for each in result5 :
    print(each)
    print(each.group())
    print(each.start())
    print(each.end())
    print(each.span()) 
    
#re.sub(정규식, 치환할문자, 대상문자) : 매치되는 문자열을 변경

text6 = """[앵커]

바로 좀 팩트체크를 해 보겠습니다. 제모를 하면 마약검사에서 빠져나갈 수 있다. 연예인 마약사건과 맞물려서 이런 글들이 온라인에서 확산됐습니다. 수사기법을 비웃는 듯한 내용입니다. 팩트체크팀이 국립과학수사연구원의 도움을 받아서 확인을 했습니다. 결론은 마약 성분은 체모 외에도 온몸을 흔적을 남긴다는 겁니다.
오대영 기자 나와 있습니다. 구체적으로 어떤 글들이 퍼져 있습니까?

[기자]

전신 제모를 하면 문제가 없다. 염색, 탈색을 하면 된다. 눈썹은 검사해도 소용없다 등의 내용입니다.
포털사이트에서 마약 검사라고 검색을 하면 모발 검사 안 걸리는 법이라는 연관 검색어까지 뜹니다."""

text7 = text6.replace("[앵커]","").replace("[기자]","")
print(text7)
#위와 아래는 같은 결과를 나타냄 
text6 = re.sub("\[.+\]","",text6)
print(text6)