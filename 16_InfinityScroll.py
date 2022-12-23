#test1) 인피니티 스크롤 사이트의 제목, 카테고리를 크롤링 하세요.
#인피니티 스크롤 : 스크롤을 내리면 추가로 데이터를 불러오는 형식  
#https://www.jungle.co.kr/ 


import requests
import json

main_list = []



magazineOffset = 0
contestOffset = 0
exhibitOffset = 0
galleryOffset = 0

for i in range(10):
    response =requests.get(f'https://www.jungle.co.kr/recent.json?magazineOffset={magazineOffset}&contestOffset={contestOffset}&exhibitOffset={exhibitOffset}&galleryOffset={galleryOffset}')
    response_json = response.json()

    for item in response_json['moreList']:
        main_list.append(
            {
                'title' : item['title'],
                'category' : item['targetCode']
            }
        )
    magazineOffset = response_json['magazineOffset']
    contestOffset = response_json['contestOffset']
    exhibitOffset = response_json['exhibitOffset']
    galleryOffset = response_json['galleryOffset']
#print(main_list)

with open('main_list.json','w',encoding = 'utf8') as json_file:  #encoding = 'utf8' : 유니코드 형태일때 추가해주기
    json.dump(main_list, json_file, ensure_ascii=False) #ensure_ascii=False : 유니코드 형태일때 추가해주기


#json파일 볼때  ctrl+k(모두선택) → Ctrl + f (정렬)  해주면 보기 쉬움