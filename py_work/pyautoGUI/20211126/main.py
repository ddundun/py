# -*- coding: utf-8 -*-
import sys

from PyQt5.QtGui import QPixmap

from weather import weather
from PyQt5 import *
from PyQt5 import uic
from PyQt5.QtWidgets import *
from bs4 import BeautifulSoup
from urllib import parse, request



form_class = uic.loadUiType("dmdkdk.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    #     # savebtn loadbtn createbtn
        self.searchbtn.clicked.connect(self.searchfn)
    #     self.loadbtn.clicked.connect(self.loadfn)
    #     self.createbtn.clicked.connect(self.createfn)
    #
    def searchfn(self):
        print("searchfn")

        d = (self.lineEdit.text())
        d += "날씨"
        d = parse.quote(d)
        URL = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + d

        source = request.urlopen(URL)
        soup = BeautifulSoup(source.read(), 'html.parser')

        w1 = soup.find("div", {"class": "weather_graphic"})
        weather = soup.find("ul", {"class": "weather_info_list"})
        # weather1=soup.find("span",{"class":"txt_weather"})
        # weather2=soup.find("p",{"class":"txt_desc"})
        # munzi = soup.find("span",{"dust_type1"})
        # weather1=weather1.get_text()
        # weather2=weather2.get_text()

        w1 = w1.get_text()
        weather = weather.get_text()

        print('현재날씨 = ', w1)
        # print('내일날씨 = ',weather)

        w2 = w1.split()
        # print(w2)

        w3 = w2[2].split('온도')
        # print(w3)

        w4 = w3[1].split('°')
        # print(w4)

        if (int(w4[0]) >= 10):
            print('오늘 가디건챙기세용')

            label1 = QLabel(self)

            label1.move(10, 10)

            # 이미지 관련 클래스 생성 및 이미지 불러오기

            pixmap = QPixmap('D:\Image\i2.png')

            # 이미지 관련 클래스와 라벨 연결
            label1.setPixmap(pixmap)

            self.show()

        elif (int(w4[0]) <= 5):
            print('롱패딩추천')
    #     try:
    #         kor = (self.koredit.text())
    #         eng = (self.engedit.text())
    #         math = (self.mathedit.text())
    #         tot = int(kor) + int(eng) + int(math)
    #         avg = tot / 3
    #         print('tot = ', tot)
    #         print('avg = ', avg)
    #         self.mex.savefn(kor, eng, math, tot, avg)
    #     except Exception as e:
    #         print(e)
    #
    # def loadfn(self):
    #     self.mex.loadfn()
    #
    # def createfn(self):
    #     self.mex.createfn()


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()
    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()