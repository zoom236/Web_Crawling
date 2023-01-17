import requests
from urllib import parse
import boto3
import json

search_text = '메타버스'
texts = []

s3 = boto3.resource('s3')


headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'ig_nrcb=1; mid=Y8YtXgALAAHRzk7LDpXL469pgyzp; ig_did=3821174C-61FC-4C96-95C5-8BFE29AAEAC2; csrftoken=Ez62wKi5oW7GO86hMnXqVRXn0Rpz8IcO; ds_user_id=6205495889; shbid="16614\0546205495889\0541705468321:01f75d8202b25c96dfb00291e4effd5a17a3eabff5f2d2b93e7c2c09bbf820a37889075e"; shbts="1673932321\0546205495889\0541705468321:01f71188eb29f7dab1c905528a0065e86326cfb11ec8c921ab95b8f8be21a2fc81bef2db"; datr=IS7GYxfOmVDv1gOQXAL113BV; sessionid=6205495889%3Ausn5eK0cJl1p1o%3A21%3AAYf5gdxlayYy631FxlEVFSCoAxBczx1EdVd98EKSew; rur="VLL\0546205495889\0541705468816:01f76ecb1a27808d3cdbb63b79cbcc55a045cd93968d62c078e3335774a134b840298418"',
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
    'x-csrftoken': 'Ez62wKi5oW7GO86hMnXqVRXn0Rpz8IcO',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR1t-cjdmFVxUWNs5oTUBFHAlIpCsZiv-DPKgOmEgrq_tUu4'
}


url = 'https://i.instagram.com/api/v1/tags/web_info/?tag_name='+parse.quote(search_text)
response = requests.get(url, headers =headers)
for rows in response.json()['data']['recent']['sections']:
    for columns in rows['layout_content']['medias'] :
        text = ''
        try :
            text = columns['media']['caption']['text']
        except :
            pass
        
        texts.append(text)
        
        if 'carousel_media' in columns['media']:
                #True 이미지 여러장
            for idx, image in enumerate(columns['media']['carousel_media']) :
                res_image = requests.get(image['image_versions2']['candidates'][0]['url'])
                s3.Bucket('zoomstudy').put_object(Key = f'insta_search/{search_text}/{id}_{idx}.jpg',Body =res_image.content)
            pass
                
        else :
                #False 이미지 한장
            res_image = requests.get(columns['media']['image_versions2'] ['candidates'][0]['url'])
            s3.Bucket('zoomstudy').put_object(Key = f'insta_search/{search_text}/{id}.jpg',Body =res_image.content)
            pass
        

headers = {
    'accept': '*/*',
    #'accept-encoding': 'gzip, deflate, br',
    'accept-language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-length': '265',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_nrcb=1; mid=Y8YtXgALAAHRzk7LDpXL469pgyzp; ig_did=3821174C-61FC-4C96-95C5-8BFE29AAEAC2; csrftoken=Ez62wKi5oW7GO86hMnXqVRXn0Rpz8IcO; ds_user_id=6205495889; shbid="16614\0546205495889\0541705468321:01f75d8202b25c96dfb00291e4effd5a17a3eabff5f2d2b93e7c2c09bbf820a37889075e"; shbts="1673932321\0546205495889\0541705468321:01f71188eb29f7dab1c905528a0065e86326cfb11ec8c921ab95b8f8be21a2fc81bef2db"; datr=IS7GYxfOmVDv1gOQXAL113BV; sessionid=6205495889%3Ausn5eK0cJl1p1o%3A21%3AAYf5gdxlayYy631FxlEVFSCoAxBczx1EdVd98EKSew; rur="NAO\0546205495889\0541705471528:01f77e3f6a87c28a88c08ba1f1b5da54db9591699519a5a5ec8cc84bacc0f73b6704ef8b"',
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
    'x-csrftoken': 'Ez62wKi5oW7GO86hMnXqVRXn0Rpz8IcO',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR1t-cjdmFVxUWNs5oTUBFHAlIpCsZiv-DPKgOmEgrq_tUu4',
    'x-instagram-ajax': '1006823085'
}

page = 1
max_id = 'QVFDaDI2YVUwZFNvZ1JsRUEweXdhUGhFWUZKaEtrNWtlMURrZXhQaDNZOFZSb192eEdaaHJlcE00dHNrRjUxbW51R0l5eFhWc3RMV3I1VU1uM0IteWdOUw=='
next_media_ids1 = 3017403393694800455
next_media_ids2 = 3017402556671280584


for page in range(3):
    try : 
        url = 'https://i.instagram.com/api/v1/tags/'+parse.quote(search_text)+'/sections/'
        data = {
                'include_persistent': 0,
                'max_id':max_id,
                'next_media_ids[]':next_media_ids1,
                'next_media_ids[]':next_media_ids2,
                'page':page,
                'surface':'grid',
                'tab':'recent'
            }
        response = requests.post(url,data = data, headers=headers)        
    except : 
        try :
            url = 'https://i.instagram.com/api/v1/tags/'+parse.quote(search_text)+'/sections/'
            data = {
                    'include_persistent': 0,
                    'max_id':max_id,
                    'next_media_ids[]':next_media_ids1,
                    'page':page,
                    'surface':'grid',
                    'tab':'recent'
                }
            response = requests.post(url,data = data, headers=headers)
        except :
            url = 'https://i.instagram.com/api/v1/tags/'+parse.quote(search_text)+'/sections/'
            data = {
                'include_persistent': 0,
                'max_id':max_id,
                'page':page,
                'surface':'grid',
                'tab':'recent'
            }
            response = requests.post(url,data = data, headers=headers)

    for rows in response.json()['sections']:
        for columns in rows['layout_content']['medias'] :
            id = columns['media']['id']
            text = ''
            try :
                text = columns['media']['caption']['text']
            except :
                pass
            texts.append(text)
            
            if 'carousel_media' in columns['media']:
                #True 이미지 여러장
                for idx, image in enumerate(columns['media']['carousel_media']) :
                    res_image = requests.get(image['image_versions2']['candidates'][0]['url'])
                    s3.Bucket('zoomstudy').put_object(Key = f'insta_search/{search_text}/{id}_{idx}.jpg',Body =res_image.content)
                pass
                
            else :
                #False 이미지 한장
                res_image = requests.get(columns['media']['image_versions2'] ['candidates'][0]['url'])
                s3.Bucket('zoomstudy').put_object(Key = f'insta_search/{search_text}/{id}.jpg',Body =res_image.content)
                pass      
            
    max_id = response.json()['next_max_id']
    page = response.json()['next_page']
    try :
        next_media_ids1 = response.json()['next_media_ids'][0]
        next_media_ids2 = response.json()['next_media_ids'][1]
        pass
    
    except :
        try :
            next_media_ids1 = response.json()['next_media_ids'][0]
            pass
        except :
            pass


s3.Bucket('zoomstudy').put_object(Key = f'insta_search/{search_text}.json',Body = json.dumps(texts,ensure_ascii =False))