import requests
from bs4 import BeautifulSoup

URL= 'https://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)
soup = BeautifulSoup(response.text,'html.parser')

print(soup.find(id = 'cook').text)
key = []
values = []
for element in  soup.find_all('th') :
    key.append(element.text)
    

for element in  soup.find('table').find('tbody').find_all('tr') :
    temp = []
    for element in element.find_all('td'):
        temp.append(element.text)
    values.append(dict(zip(key, temp)))

print(values)

for atag in soup.find_all('a'):
    response=requests.get('https://crawlingstudy-dd3c9.web.app/01/'+atag.attrs['href'])
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.find('p').text.strip())
