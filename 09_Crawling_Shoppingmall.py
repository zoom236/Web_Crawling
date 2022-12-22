# test ) 쇼핑몰의 상의(TOP) 카테고리 첫페이지의 제품들의 브랜드명, 제품명, 가격을 아래와 같이 크롤링해주세요.
# https://store.musinsa.com/app/items/lists/001
# 성공시 총 10페이지 크롤링해주세요 

import requests
import re
from bs4 import BeautifulSoup

for i in range(1,11):
    print('Page ===========================', i)
    
    URL = f'https://www.musinsa.com/categories/item/001?d_cat_cd=001&brand=&list_kind=small&sort=pop_category&sub_sort=&page={i}&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    for item in soup.select('ul#searchList > li') :
        print('브랜드 : ', item.select_one('.article_info p.item_title').text.strip())
        print('상품명 : ', item.select_one('.article_info p.list_info a').attrs['title'])
        price =''
    
    # 강사님이랑 답은 일치하나 가격이 제대로 표현되지 않음 아래쪽 정규표현식 사용한 답 사용하기 
    #if len(item.select_one('.article_info p.price').text.strip().split(" ")) == 1:
    #    price = item.select_one('.article_info p.price').text.strip().split(" ")[0]
    #else:
    #    price = item.select_one('.article_info p.price').text.strip().split(" ")[1]
    
        if len(re.findall('[0-9,]*원', item.select_one('.article_info p.price').text)) == 1:
            price = re.findall('[0-9,]*원', item.select_one('.article_info p.price').text)[0]
        else:
           price = re.findall('[0-9,]*원', item.select_one('.article_info p.price').text)[1]
        
        
        print('가격 : ',price)
    