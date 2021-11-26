# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib import parse, request


d=input("지역을 입력하세요. ")
d+="날씨"
d=parse.quote(d)

URL='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='+d

source = request.urlopen(URL)
soup = BeautifulSoup(source.read(), 'html.parser')

w1=soup.find("div",{"class":"weather_graphic"})
weather=soup.find("ul",{"class":"weather_info_list"})
# weather1=soup.find("span",{"class":"txt_weather"})
# weather2=soup.find("p",{"class":"txt_desc"})
# munzi = soup.find("span",{"dust_type1"})
# weather1=weather1.get_text()
# weather2=weather2.get_text()

w1= w1.get_text()
weather=weather.get_text()

# print('날씨',weather1.strip(),weather2.strip(),'미세먼지',munzi)
print('내일날씨 = ',weather)
print('현재날씨 = ',w1)