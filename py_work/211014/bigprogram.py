'''
    bigprogram.py 실행하면 크롬브라우저 실행되면서
    주소를 임의적으로 입력해서 자동으로 매크로 수행을 하는 프로그램
'''

from selenium import webdriver

aa = webdriver.Chrome('chromedriver.exe')
# 변수 aa가 크롬브라우저를 가리키굉ㅆ음

aa.get("http://www.naver.com")
# get쓰면 바까줌
# 이렇게하면 네이버 페이지 뜸

aa.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[1]/a').click()

# ctrl + alt +l 정렬!

import keyword

print(keyword.kwlist)