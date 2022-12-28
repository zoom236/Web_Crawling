import requests
from bs4 import BeautifulSoup

url = 'https://crawlingstudy-dd3c9.web.app/03/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

popular = []

for pop in soup.select('#popularItemList > li'):
    popular.append([pop.select_one('a').text,pop.select_one('img').attrs['alt']])

print(popular)

major = []
for maj in soup.select('.lst_major > li') :
    major.append([maj.select_one('a').text,maj.select_one('img').attrs['alt']])

print(major)
