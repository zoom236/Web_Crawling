#test 2) 아래 sns키워드 검색페이지를 분석하여 검색어를 입력하면 해당 검색어의 내용을 크롤링하여 AWS S3 Storage에 검색어 .json 파일로 저장하는 프로그램을 만드세요
# https://twitter.com/search?q=%EB%A9%94%ED%83%80%EB%B2%84%EC%8A%A4&src=typed_query&f=live

import requests
import json
import boto3

tweet = []
s3 = boto3.resource('s3')
search_text = '메타버스'

headers = {
'accept': '*/*',
#'accept-encoding': 'gzip, deflate, br',- 압축된 내용 때문에 깨진 글씨가 나옴 
'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
'cookie': 'personalization_id="v1_3iIf5pCnMdcErtV9LC6UGA=="; guest_id_marketing=v1%3A166970499587819002; guest_id_ads=v1%3A166970499587819002; guest_id=v1%3A166970499587819002; _ga=GA1.2.1627996721.1671823221; _gid=GA1.2.1894542955.1671823221; ct0=d2ce29e0751bd46ce78b399c192d78fd; gt=1606525512955834368',
'origin': 'https://twitter.com',
'referer': 'https://twitter.com/',
'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
'x-csrf-token': 'd2ce29e0751bd46ce78b399c192d78fd',
'x-guest-token': '1606525512955834368',
'x-twitter-active-user': 'yes',
'x-twitter-client-language': 'ko'
}

params ={
    'include_profile_interstitial_type': 1,
    'include_blocking':1,
    'include_blocked_by': 1,
    'include_followed_by': 1,
    'include_want_retweets': 1,
    'include_mute_edge': 1,
    'include_can_dm': 1,
    'include_can_media_tag': 1,
    'include_ext_has_nft_avatar': 1,
    'include_ext_is_blue_verified': 1,
    'include_ext_verified_type': 1,
    'skip_status': 1,
    'cards_platform': 'Web-12',
    'include_cards': 1,
    'include_ext_alt_text': True,
    'include_ext_limited_action_results':False,
    'include_quote_count': True,
    'include_reply_count': 1,
    'tweet_mode': 'extended',
    'include_ext_collab_control': True,
    'include_entities': True,
    'include_user_entities': True,
    'include_ext_media_color': True,
    'include_ext_media_availability': True,
    'include_ext_sensitive_media_warning': True,
    'include_ext_trusted_friends_metadata': True,
    'send_error_codes':True,
    'simple_quoted_tweet': True,
    'q': search_text,
    'tweet_search_mode':'live',
    'count': 20,
    'query_source': 'typed_query',
    'pc': 1,
    'spelling_corrections': 1,
    'include_ext_edit_control': True,
    'ext': 'mediaStats,highlightedLabel,hasNftAvatar,voiceInfo,enrichments,superFollowMetadata,unmentionInfo,editControl,collab_control,vibe'
}


response= requests.get('https://api.twitter.com/2/search/adaptive.json',headers= headers, params= params)
response_json= response.json()

#print(response.status_code)
for tweets in response_json['globalObjects']['tweets']:
    tweet.append({
            'full_text': response_json['globalObjects']['tweets'][tweets]['full_text'],
            'user_id' : response_json['globalObjects']['tweets'][tweets]['user_id']      
    })



#파라메타의 변화를 보니 처음 파라메타엔 cursor가 없었고 두번째부터 cursor가 생기기 시작함.    
#첫번째 호출 후 cursor가져오기 
cursor = response_json['timeline']['instructions'][0]['addEntries']['entries'][-1]['content']['operation']['cursor']['value']
#print(cursor)



##for문이 10회 돌긴 하지만 2페이지 가 9번 반복 하는 현상 발생
for i in range(10) :
    params = {
        'include_profile_interstitial_type': 1,
        'include_blocking': 1,
        'include_blocked_by': 1,
        'include_followed_by': 1,
        'include_want_retweets': 1,
        'include_mute_edge':1,
        'include_can_dm': 1,
        'include_can_media_tag': 1,
        'include_ext_has_nft_avatar':1,
        'include_ext_is_blue_verified': 1,
        'include_ext_verified_type': 1,
        'skip_status':  1,
        'cards_platform':'Web-12',
        'include_cards': 1,
        'include_ext_alt_text': True,
        'include_ext_limited_action_results': False,
        'include_quote_count': True,
        'include_reply_count': 1,
        'tweet_mode': 'extended',
        'include_ext_collab_control': True,
        'include_entities': True,
        'include_user_entities': True,
        'include_ext_media_color': True,
        'include_ext_media_availability': True,
        'include_ext_sensitive_media_warning': True,
        'include_ext_trusted_friends_metadata': True,
        'send_error_codes':True,
        'simple_quoted_tweet': True,
        'q': search_text,
        'tweet_search_mode': 'live',
        'count': 20,
        'query_source':'typed_query',
        'cursor':'scroll:thGAVUV0VFVBaAwNHVopm4yywWgMDT_ergxsssEnEV8IV6FYCJehgHREVGQVVMVDUBFQAVAAA=',
        'pc': 1,
        'spelling_corrections':  1,
        'include_ext_edit_control': True,
        'ext': 'mediaStats,highlightedLabel,hasNftAvatar,voiceInfo,enrichments,superFollowMetadata,unmentionInfo,editControl,collab_control,vibe'
    }

    response= requests.get('https://api.twitter.com/2/search/adaptive.json',headers= headers, params= params)
    response_json= response.json()


    for tweets in response_json['globalObjects']['tweets']:
        tweet.append({
            'full_text': response_json['globalObjects']['tweets'][tweets]['full_text'],
            'user_id': response_json['globalObjects']['tweets'][tweets]['user_id']      
        })

    #파라메타의 변화를 보니 처음 파라메타엔 cursor가 없었고 두번째부터 cursor가 생기기 시작함.    
    #두번째 cursor가져오기 

    cursor = response_json['timeline']['instructions'][-1]['replaceEntry']['entry']['content']['operation']['cursor']['value']
    # print(response_json['timeline']['instructions'][-1]['replaceEntry']['entry']['content']['operation']['cursor']['cursorType'])
    # print(cursor)
print(tweet)
s3.Bucket('studyzoom').put_object(Key =f'tweet_search/{search_text}.json', Body =json.dumps(tweet, ensure_ascii=False))