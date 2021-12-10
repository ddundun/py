import requests
from bs4 import BeautifulSoup


class Typing:
    def returnMessage(self):
        data = requests.get(
            "https://search.naver.com/search.naver?where=nexearch&sm=top"
            "_hty&fbm=1&ie=utf8&query=%EB%8C%80%EA%B5%AC%EB%82%A0%EC%94%A8")
        soup = BeautifulSoup(data.text, 'html.parser')
        ondos = soup.select_one(
            '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking '
            '> div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info '
            '> div > div.weather_graphic > div.temperature_text > strong').text
        weather = soup.select_one(
            '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking '
            '> div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > '
            'div > div.weather_graphic > div.weather_main > i > span').text
        b = str(ondos).split("현재 온도")
        c = b[1].split("°")
        ondos_num = c[0]
        ondo = eval(ondos_num)
        print("현재 날씨 :", weather)
        # 맑음,비,흐림,구름많음
        print("현재 온도 :", b[1])
        dust = soup.select_one(
            "#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking >"
            " div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div"
            " > div.report_card_wrap > ul > li:nth-child(1) > a > span").text
        print("미세먼지 :", dust)
        rain = soup.select_one(
            '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > '
            'div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div '
            '> div.temperature_info > dl > dd:nth-child(2)').text
        print("강수확률 :", rain)
        textBox = "현재 날씨 : " + weather + "\n" + "현재 온도 : " + b[
            1] + "\n" + "미세먼지 : " + dust + "\n" + "강수확률 : " + rain + "\n"
        if (ondo >= 28):
            print("반팔,반바지,민소매,짧은 치마,린넨 옷은 어떨까요?")
            a = "반팔,반바지,민소매,짧은 치마,린넨 옷은 어떨까요?"
        elif (ondo < 28 and ondo >= 23):
            print("반팔,얇은 셔츠,반바지,면바지는 어떨까요?")
            a = "반팔,얇은 셔츠,반바지,면바지는 어떨까요?"
        elif (ondo < 23 and ondo >= 20):
            print("긴팔 티,가디건,블라우스,후드티,면바지,슬랙스는 어떨까요?")
            a = "긴팔 티,가디건,블라우스,후드티,면바지,슬랙스는 어떨까요?"
        elif (ondo < 20 and ondo >= 17):
            print("니트,얇은 가디건,후드,맨투맨,긴 바지,면바지,슬랙스,원피스는 어떨까요?")
            a = "니트,얇은 가디건,후드,맨투맨,긴 바지,면바지,슬랙스,원피스는 어떨까요?"
        elif (ondo < 17 and ondo >= 12):
            print("자켓,셔츠,가디건,간절기 야상,청바지,스타킹은 어떨까요?")
            a = "자켓,셔츠,가디건,간절기 야상,청바지,스타킹은 어떨까요?"
        elif (ondo < 12 and ondo >= 9):
            print("트렌치코트,간절기 야상,점퍼,기모바지는 어떨까요?")
            a = "트렌치코트,간절기 야상,점퍼,기모바지는 어떨까요?"
        elif (ondo < 9 and ondo >= 5):
            print("히트텍,가죽 옷,기모,울 코트는 어떨까요?")
            a = "히트텍,가죽 옷,기모,울 코트는 어떨까요?"
        else:
            print("패딩,두꺼운 코트,누빔 옷,기모,목도리는 어떨까요?")
            a = "패딩,두꺼운 코트,누빔 옷,기모,목도리는 어떨까요?"
        textBox += a
        return textBox
