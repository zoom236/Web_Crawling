#Test3) 아래 sns 키워드 검색 페이지를 분석하여 검색어를 입력하면 해당 검색어의 내용을 aws s3 storage에 검색어.json 파일로 저장하고 등록되어 있는 이미지도 파일로 같이 저장해주세요.
#https://www.instagram.com/explore/tags/%EB%A9%94%ED%83%80%EB%B2%84%EC%8A%A4/


import requests
from urllib import parse #url 인코딩 하는 모듈 
import boto3
import json




search_text = '메타버스'
texts= []

s3 = boto3.resource('s3')


headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'mid=Yv9MlgALAAFfPRZimDPbW3Ei2jHw; ig_did=6004A588-CB4A-4614-9060-CC888B4A661D; ig_nrcb=1; csrftoken=sRxBORBj9y0bYODnOMMCAQq26pAx3FDy; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=6205495889; sessionid=6205495889%3ASpPmsxV4MVV567%3A11%3AAYdzxLOWAmEzgnIej8IeAeACQGcjBTUEObY4hHcwoQ; shbid="16614\0546205495889\0541703404753:01f79302889374a50cd5c24faaedc0ba558c2a2bef489eccd6a006d94bed2c2ccc99997f"; shbts="1671868753\0546205495889\0541703404753:01f74f96a5983447212767be71489a258343ca335139bbe61720f7a264bd4b8748fae01b"; fbsr_124024574287414=mJnw0osUqIhnsolYDPm7eXeRd25i7kfXioNcc-Ft-Mc.eyJ1c2VyX2lkIjoiMTAwMDAzMDkzNTc4NzkwIiwiY29kZSI6IkFRRDM5SHVJVGo4aW9ya1AtVm5tcjVPd3lDWDNiUmdrQVVxN3JKb0FqZ29zT0xGam5mWnZRcFRhZ3c0ZGlVT2otN21ibjNWekJUampXTU1wOEVBRFc1bDF6Nkx3c3ZTdkwzNFpLZTk3c1NyQlJ6WTdMZHIwN2xUTzNncWFqMVRBYU5VSTNUVEllczBpOGVsclNYb3hXd0ZYamJNaDIyZkdRWEhzUHpZU0hwMHQxc014b0YxNG53dGd1blkzQUhRdXJ3V2hFU1V1VTRSOXJoWEdHMm1vb19uQmZFUF9PYWZMZWhZaFVXUDZZbk5jczU0UVZtQng3QlVMMkJYeXZ1eXhTeWVGQU9sOHhjZkttV2pHV0FkQ3NQY1J5NDZUdEUySHFKRzM5R1V6TXYwYW9FbWRwbmxLWWFUTk5YczMtay1LTE1jeVo3aEJKUHB5RUtLQVRIT0doUjFmIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUc3dWlLRTBoYjBmNDZ4SVU5QVFFakhhd3JmcnBnUXJJT1dwQ0dSQmZqZXBpbG1EQ3BXMUJScktISlJJaFRYS2JxSjIydE1wUTRHbFZBU0dJdnRNMWFjakc5VXZzeDRvQ0VkeG1DYkNIckM5anpaQU5UbFNoeTdGSmZhYjdmRUJZSzNzTjdHaXVxWkI5cXYzaHlkcnBmRVBYYW1Wa2NCRWY3c1YyS1R5bzFwMjA2WkN0WVpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzE4NjkwNjl9; rur="NAO\0546205495889\0541703405302:01f70d3a299d27f3b96e2550ccf2d0a995c54c24a878ba7e0f0f453e74782ec96e37e5a0"',
    'origin': 'https://www.instagram.com',
    'referer':'https://www.instagram.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-asbd-id': '198387',
    'x-csrftoken': 'sRxBORBj9y0bYODnOMMCAQq26pAx3FDy',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR1t-cjdmFVxUWNs5oTUBFHAlIpCsZiv-DPKgOmEgrq_taOJ'
}

response = requests.get('https://i.instagram.com/api/v1/tags/web_info/?tag_name='+ parse.quote(search_text) +'',headers=headers)

#스크롤을 내리지 않은 첫페이지에서 이미지 크롤링

for rows in response.json()['data']['recent']['sections'] : 
     for columns in rows['layout_content']['medias']:
        text= ''
        try :
            text =columns['media']['caption']['text']
        except:
            pass #text를 안적은 경우 
        texts.append(text)
        
        #키가 있는지 없는지 체크하는 방법
        #true이면 이미지가 여러개, false이면 이미지 하나 
        if 'carousel_media' in columns['media']:
            for idx, image in enumerate(columns['media']['carousel_media']):
                    res_image = requests.get(image['image_versions2']['candidates'][0]['url'])
                    s3.Bucket('studyzoom').put_object(Key = f'insta_search/{search_text}/{id}_{idx}.jpg', Body = res_image.content)
            pass
        else:
            res_image = requests.get(columns['media']['image_versions2']['candidates'][0]['url'])
            s3.Bucket('studyzoom').put_object(Key = f'insta_search/{search_text}/{id}.jpg', Body = res_image.content)
            pass
        
        #print(text)
        
#스크롤을 내린 상태에서의 이미지 크롤링

#section payload - max id : QVFBZGtIajhsOVNIaXpKNXlqUHFBWVVrOW9WTWhSd3diaElQSmlrUk9YSzNQXzZwNmZOQ0JXbzB5ZkV2TW5Pb3hHdkZYbEdIRU1OVFZERXcyTVhlVHhMYQ==
#tag_name preview -max id : QVFBZGtIajhsOVNIaXpKNXlqUHFBWVVrOW9WTWhSd3diaElQSmlrUk9YSzNQXzZwNmZOQ0JXbzB5ZkV2TW5Pb3hHdkZYbEdIRU1OVFZERXcyTVhlVHhMYQ==
#스크롤을 내릴때 마다 max id 변경

##Post방식, body에 내용 넣어서 보내는 형식
page = 1
max_id ='QVFBZGtIajhsOVNIaXpKNXlqUHFBWVVrOW9WTWhSd3diaElQSmlrUk9YSzNQXzZwNmZOQ0JXbzB5ZkV2TW5Pb3hHdkZYbEdIRU1OVFZERXcyTVhlVHhMYQ=='

for page in range(3):

    url = 'https://i.instagram.com/api/v1/tags/'+ parse.quote(search_text) +'/sections/'
    headers = {
        'accept': '*/*',
        #'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-length': '224',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'mid=Yv9MlgALAAFfPRZimDPbW3Ei2jHw; ig_did=6004A588-CB4A-4614-9060-CC888B4A661D; ig_nrcb=1; csrftoken=sRxBORBj9y0bYODnOMMCAQq26pAx3FDy; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=6205495889; sessionid=6205495889%3ASpPmsxV4MVV567%3A11%3AAYdzxLOWAmEzgnIej8IeAeACQGcjBTUEObY4hHcwoQ; shbid="16614\0546205495889\0541703404753:01f79302889374a50cd5c24faaedc0ba558c2a2bef489eccd6a006d94bed2c2ccc99997f"; shbts="1671868753\0546205495889\0541703404753:01f74f96a5983447212767be71489a258343ca335139bbe61720f7a264bd4b8748fae01b"; fbsr_124024574287414=mJnw0osUqIhnsolYDPm7eXeRd25i7kfXioNcc-Ft-Mc.eyJ1c2VyX2lkIjoiMTAwMDAzMDkzNTc4NzkwIiwiY29kZSI6IkFRRDM5SHVJVGo4aW9ya1AtVm5tcjVPd3lDWDNiUmdrQVVxN3JKb0FqZ29zT0xGam5mWnZRcFRhZ3c0ZGlVT2otN21ibjNWekJUampXTU1wOEVBRFc1bDF6Nkx3c3ZTdkwzNFpLZTk3c1NyQlJ6WTdMZHIwN2xUTzNncWFqMVRBYU5VSTNUVEllczBpOGVsclNYb3hXd0ZYamJNaDIyZkdRWEhzUHpZU0hwMHQxc014b0YxNG53dGd1blkzQUhRdXJ3V2hFU1V1VTRSOXJoWEdHMm1vb19uQmZFUF9PYWZMZWhZaFVXUDZZbk5jczU0UVZtQng3QlVMMkJYeXZ1eXhTeWVGQU9sOHhjZkttV2pHV0FkQ3NQY1J5NDZUdEUySHFKRzM5R1V6TXYwYW9FbWRwbmxLWWFUTk5YczMtay1LTE1jeVo3aEJKUHB5RUtLQVRIT0doUjFmIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUc3dWlLRTBoYjBmNDZ4SVU5QVFFakhhd3JmcnBnUXJJT1dwQ0dSQmZqZXBpbG1EQ3BXMUJScktISlJJaFRYS2JxSjIydE1wUTRHbFZBU0dJdnRNMWFjakc5VXZzeDRvQ0VkeG1DYkNIckM5anpaQU5UbFNoeTdGSmZhYjdmRUJZSzNzTjdHaXVxWkI5cXYzaHlkcnBmRVBYYW1Wa2NCRWY3c1YyS1R5bzFwMjA2WkN0WVpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzE4NjkwNjl9; rur="NAO\0546205495889\0541703405309:01f7f733428b1837c74c5c64e86474e1c250879483de5956d5b610799a1608604eefc768"',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'x-asbd-id': '198387',
        'x-csrftoken': 'sRxBORBj9y0bYODnOMMCAQq26pAx3FDy',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR1t-cjdmFVxUWNs5oTUBFHAlIpCsZiv-DPKgOmEgrq_taOJ',
        'x-instagram-ajax': '1006770720'
    }
    data ={
        'include_persistent': 0,
        'max_id': max_id,
        'next_media_ids[]':3000082482456179182,
        'page': page,
        'surface': 'grid',
        'tab':'recent'
    }

    response = requests.post(url, data=data,headers=headers)
    for rows in response.json()['sections']:
        
        for columns in rows['layout_content']['medias']:
            id = columns['media']['id']
            text= ''
            try :
                text =columns['media']['caption']['text']
            except:
                pass #text를 안적은 경우 
            texts.append(text)
            
            #키가 있는지 없는지 체크하는 방법
            #true이면 이미지가 여러개, false이면 이미지 하나 
            if 'carousel_media' in columns['media']:
                for idx, image in enumerate(columns['media']['carousel_media']):
                    res_image = requests.get(image['image_versions2']['candidates'][0]['url'])
                    s3.Bucket('studyzoom').put_object(Key = f'insta_search/{search_text}/{id}_{idx}.jpg', Body = res_image.content)
                pass
            else:
                res_image = requests.get(columns['media']['image_versions2']['candidates'][0]['url'])
                s3.Bucket('studyzoom').put_object(Key = f'insta_search/{search_text}/{id}.jpg', Body = res_image.content)
                pass
            
            #print(text)

    max_id = response.json()['next_max_id']
    page =response.json()['next_page']


s3.Bucket('studyzoom').put_object(Key = f'insta_search/{search_text}.json', Body = json.dumps(texts, ensure_ascii=False))
print('완료')