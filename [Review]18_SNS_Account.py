import requests
import json
from urllib import parse
import boto3


s3 = boto3.resource('s3')



headers = {
    'accept': '*/*',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    'cookie': 'personalization_id="v1_HgdeA5LS6ho7gyREPeTqng=="; guest_id_marketing=v1%3A167213149468853377; guest_id_ads=v1%3A167213149468853377; guest_id=v1%3A167213149468853377; ct0=0742d18ff1a41a2eecc8494a92deca10; _ga=GA1.2.1277264130.1673865647; _gid=GA1.2.983950578.1673865647; gt=1614981000244912135',
    'origin': 'https://twitter.com',
    'referer': 'https://twitter.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-csrf-token': '0742d18ff1a41a2eecc8494a92deca10',
    'x-guest-token': '1614981000244912135',
    'x-twitter-active-user': 'yes',
    'x-twitter-client-language': 'ko'
}


screen_name = "Disney"
tweets = []



#userId 찾기 
url = 'https://api.twitter.com/graphql/hVhfo_TquFTmgL7gYwf91Q/UserByScreenName'
params1 = {
    "screen_name":screen_name,
    "withSafetyModeUserFields":True,
    "withSuperFollowsUserFields":True
    }
params2 = {
    "responsive_web_twitter_blue_verified_badge_is_enabled":True,
    "verified_phone_label_enabled":False,
    "responsive_web_graphql_timeline_navigation_enabled":True
    }

params1_text = json.dumps(params1)
params1_text = parse.quote(params1_text)

params2_text = json.dumps(params2)
params2_text = parse.quote(params2_text)
response = requests.get(url + '?variables=' + params1_text + '&features='+params2_text, headers= headers)
rest_id = response.json()['data']['user']['result']['rest_id']


#cursor 찾기 
url = 'https://api.twitter.com/graphql/oFomu6X21hguOVSeG0PhDA/UserTweets'
params1 = {
    "userId":rest_id,
    "count":40,
    "includePromotedContent":True,
    "withQuickPromoteEligibilityTweetFields":True,
    "withSuperFollowsUserFields":True,
    "withDownvotePerspective":False,
    "withReactionsMetadata":False,
    "withReactionsPerspective":False,
    "withSuperFollowsTweetFields":True,
    "withVoice":True,
    "withV2Timeline":True
    }
params2 = {
    "responsive_web_twitter_blue_verified_badge_is_enabled":True,
    "verified_phone_label_enabled":False,
    "responsive_web_graphql_timeline_navigation_enabled":True,
    "view_counts_public_visibility_enabled":True,
    "view_counts_everywhere_api_enabled":True,
    "longform_notetweets_consumption_enabled":False,
    "tweetypie_unmention_optimization_enabled":True,
    "responsive_web_uc_gql_enabled":True,
    "vibe_api_enabled":True,
    "responsive_web_edit_tweet_api_enabled":True,
    "graphql_is_translatable_rweb_tweet_is_translatable_enabled":True,
    "standardized_nudges_misinfo":True,
    "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":False,
    "interactive_text_enabled":True,
    "responsive_web_text_conversations_enabled":False,
    "responsive_web_enhance_cards_enabled":False
           }
params1_text = json.dumps(params1)
params1_text = parse.quote(params1_text)

parmas2_text = json.dumps(params2)
parmas2_text = parse.quote(parmas2_text)
response= requests.get(url+'?variables='+params1_text+ '&features='+parmas2_text, headers=headers)
cursor = response.json()['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][-1]['content']['value']

# 1페이지 tweet 내용 가져오기
for tweet in response.json()['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries']:
    try:
        tweets.append({
            'full_text': tweet['content']['itemContent']['tweet_results']['result']['legacy']['full_text'],
            'user_id_str' : tweet['content']['itemContent']['tweet_results']['result']['legacy']['user_id_str']
        })
    except :
        pass


for i in range(10) :
#트윗 내용 있는 곳 
    url = 'https://api.twitter.com/graphql/oFomu6X21hguOVSeG0PhDA/UserTweets'
    params1 = { 
            "userId": rest_id,
            "count":40,
            "cursor":cursor ,
            "includePromotedContent":True,
            "withQuickPromoteEligibilityTweetFields":True,
            "withSuperFollowsUserFields":True,
            "withDownvotePerspective":False,
            "withReactionsMetadata":False,
            "withReactionsPerspective":False,
            "withSuperFollowsTweetFields":True,
            "withVoice":True,
            "withV2Timeline":True,
            }
    params2 = {
        "responsive_web_twitter_blue_verified_badge_is_enabled":True,
        "verified_phone_label_enabled":False,
        "responsive_web_graphql_timeline_navigation_enabled":True,
        "view_counts_public_visibility_enabled":True,
        "view_counts_everywhere_api_enabled":True,
        "longform_notetweets_consumption_enabled":False,
        "tweetypie_unmention_optimization_enabled":True,
        "responsive_web_uc_gql_enabled":True,
        "vibe_api_enabled":True,
        "responsive_web_edit_tweet_api_enabled":True,
        "graphql_is_translatable_rweb_tweet_is_translatable_enabled":True,
        "standardized_nudges_misinfo":True,
        "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":False,
        "interactive_text_enabled":True,
        "responsive_web_text_conversations_enabled":False,
        "responsive_web_enhance_cards_enabled":False
    }

    params1_text = json.dumps(params1)
    parmas1_text = parse.quote(params1_text)

    params2_text = json.dumps(params2)
    parmas2_text = parse.quote(params2_text)

    response = requests.get(url+'?variables='+parmas1_text+'&features='+parmas2_text, headers = headers)
    cursor = response.json()['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entries'][-1]['content']['value']

    #2페이지 이상 tweet 내용 가져오기
    for tweet in response.json()['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entries']:
        
        try:
            tweets.append({
                'full_text' : tweet['content']['itemContent']['tweet_results']['result']['legacy']['full_text'],
                'user_id_str' :tweet['content']['itemContent']['tweet_results']['result']['legacy']['user_id_str']
            })
          
        except :
            pass


s3.Bucket('zoomstudy').put_object(Key = f'tweets_user/{screen_name}.json',Body = json.dumps(tweets, ensure_ascii =False) )
