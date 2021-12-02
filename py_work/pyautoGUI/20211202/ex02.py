import requests
from bs4 import BeautifulSoup

req = requests.get('http://www.dowellcomputer.com/main.jsp')

# print(req)  # response 200
# print(req.text)

html = BeautifulSoup(req.text, 'html.parser')
links = html.select('td>a')

print(links)
print(len(links))

for a in links:
    if a.has_attr('href'):
        # print(a.text)
        if a.text in 'notice':
            # print(a.text)
'''
    BeatifulSoup
    find함수 -> html태그 찾을 때 사용
    select함수 -> css 선택자
'''
