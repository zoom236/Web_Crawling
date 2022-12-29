import requests
from bs4 import BeautifulSoup
#브랜드 :
#제품명 :
#가격 :
for page in range(1,11) :
    print('=====================',page)
    URL = f'https://www.musinsa.com/categories/item/001?d_cat_cd=001&brand=&list_kind=small&sort=pop_category&sub_sort=&page={page}&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    

    for item in soup.select('ul#searchList > li') :
        brand = item.select_one('p.item_title').text.strip()
        name = item.select_one('p.list_info > a').attrs['title']
        if len(item.select_one('p.price').text.strip().split()) == 2:
            price = item.select_one('p.price').text.strip().split()[1]
        
        else: 
            price = item.select_one('p.price').text.strip().split()[0]  
        print(f"""브랜드 : {brand}
제품명 : {name}
가격 : {price}
""")

