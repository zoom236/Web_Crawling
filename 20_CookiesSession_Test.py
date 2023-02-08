import requests
from bs4 import BeautifulSoup
import re

areas = [
    "강남구",
    "강동구",
    "강북구",
    "강서구",
    "관악구",
    "광진구",
    "구로구",
    "금천구",
    "노원구",
    "도봉구",
    "동대문구",
    "동작구",
    "마포구",
    "서대문구",
    "서초구",
    "성동구",
    "성북구",
    "송파구",
    "양천구",
    "영등포구",
    "용산구",
    "은평구",
    "종로구",
    "중구",
    "중랑구"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

session = requests.Session()
session.get('https://www.opinet.co.kr/user/main/mainView.do')

oil_station = []


for area in areas :

    data = {
        'BTN_DIV': 'os_btn',
    'BTN_DIV_STR': '',
    'POLL_ALL':'all',
    'SIDO_NM': '서울특별시',
    'SIGUNGU_NM': area,
    'SIDO_CD': 1,
    'SIGUN_CD':119,
    'MAP_CENTER_X':'', 
    'MAP_CENTER_Y': '',
    'MAP_ZOOM': '',
    'MAP_FIRST_X': '',
    'MAP_FIRST_Y': '',
    'LPG_YN':'' ,
    'SESSION_USER_ID':'' ,
    'SIDO_NM0':'서울특별시',
    'SIGUNGU_NM0': area,
    'DONG_NM': '',
    'GIS_X_COOR':'' ,
    'GIS_Y_COOR': '',
    'GIS_X_COOR_S':'' ,
    'GIS_X_COOR_E': '',
    'GIS_Y_COOR_S': '',
    'GIS_Y_COOR_E': '',
    'SEARCH_MOD': 'addr',
    'OS_NM': '',
    'OS_ADDR': '',
    'NORM_YN': 'on',
    'SELF_DIV_CD': 'on',
    'VLT_YN': 'on',
    'KPETRO_YN': 'on',
    'KPETRO_DP_YN': 'on',
    'POLL_DIV_CD': 'SKE',
    'POLL_DIV_CD': 'GSC',
    'POLL_DIV_CD': 'HDO',
    'POLL_DIV_CD': 'SOL',
    'POLL_DIV_CD': 'RTO',
    'POLL_DIV_CD': 'ETC',
    }



    response = session.post('https://www.opinet.co.kr/searRgSelect.do',data=data,headers=headers)

    soup = BeautifulSoup(response.text,'html.parser')



    for data in soup.select('table.tbl_type10 tbody#body1 >tr'):
        # print(data.select_one('a').attrs['href'])
        items = list(re.finditer("'[^']*',",data.select_one('a').attrs['href']))
        # 2-일반 휘발유 가격 (items[2].group())
        # 19- 셀프주유소 여부 
        # 22- 주유소 이름
        # 23 - 브랜드
        # 25 - 주소
        oil_station.append({
            '지역' : area,
            '유가' :items[2].group().replace("',","").replace("'",""),
            '주유소명':items[22].group().replace("',","").replace("'",""),
            '브랜드명' :items[23].group().replace("',","").replace("'",""),
            '주소' :items[25].group().replace("',","").replace("'",""),
            '셀프주유소여부':items[19].group().replace("',","").replace("'","")
        })



print(oil_station)
    
    