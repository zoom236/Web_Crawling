import requests
from bs4 import BeautifulSoup

#인기검색종목과 주요 해외지수를 각각 상한가인 종목만 크롤링하여 종목명과 주가지수를 아래와 같이 리스트로 정리 

url = 'https://crawlingstudy-dd3c9.web.app/03'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

popular = []
for pop in soup.select('#popularItemList > li') :
    
    if pop.select_one('img').attrs['alt'] == '상한'  :
        popular.append([pop.select_one('a').text,pop.select_one('span').text])
        
print(popular)

major = []
for maj in soup.select('.lst_major > li') :
    
    if maj.select_one('img').attrs['alt'] == '상한' :
        major.append([maj.select_one('a').text,maj.select_one('span').text])

print(major)
    
