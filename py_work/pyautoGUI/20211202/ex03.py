# import urllib.request 파이선기본라이브러리
import requests # 라이브러리 설치 필요
from bs4 import BeautifulSoup

class Review:
    def __init__(self,comment,data,star,good,bad):
        self.comment = comment
        self.data = data
        self.star = star
        self.good = good
        self.bad = bad
    def __str__(self): #tostring 함수
        return ' 내용 ' + self.comment+' 날짜 '+self.data+' 별점 '+self.star+' 좋아요 '+self.good+' 싫어요 '+self.bad


url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=36944'
# html = urllib.request.urlopen(url).read()
# print(html)
# html.parser = html번역기 .. xml.parser= xml 번역기. json.parser = json 번역기
# html = BeautifulSoup(html,'html.parser')
# print(html)

req = requests.get(url)
html = BeautifulSoup(req.text.strip(),'html.parser')
#strip : 빈공백없애기
review_list = []

review_list.append(Review('이영화잘만듬','20110101','10','400','300'))
review_list.append(Review('이영화잘만듬1','20130101','2','42','330'))
review_list.append(Review('이영화잘만듬2','20140101','3','430','320'))

for review in review_list:
    print(review)