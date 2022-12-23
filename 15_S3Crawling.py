##파이썬 s3연동 모듈 : boto3, awscli

import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all() :
    print(bucket.name)

bucket_name = 'studyzoom'
bucket = s3.Bucket(bucket_name)

local_file = 'd:\\Web_crawling_Python\\crawling_VSCode\news.json'
obj_file = 'news.json'
bucket.upload_file(local_file, obj_file)
##경로 왜 못찾는건지 모르겠네 포기 ㅠ 마지막에 다시듣기