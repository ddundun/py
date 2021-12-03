# -*- coding: utf-8 -*-
import sys
from PyQt5.QtGui import *
from weather import weather
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
    #     label = QLabel()
    #     label.setPixmap(QPixmap("logo.png"))
    #     self.setCentralWidget(label)

    # def initWidget(self):
    #     label_1 = QLabel("라벨1", self)
    #     label_2 = QLabel("라벨2", self)
    #     label_3 = QLabel("라벨3", self)
    #
    #     boxlayout = QVBoxLayout(self)
    #     boxlayout.addWidget(label_1)
    #     boxlayout.addWidget(label_2)
    #     boxlayout.addWidget(label_3)




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
        print(w2)

        w3 = w2[2].split('온도')
        print(w3)

        w4 = w3[1].split('°')
        print(w4)

        if (int(w4[0]) >= 10):
            print('오늘 가디건챙기세용')

            # label = QLabel()
            # label.setPixmap(QPixmap("../20211202/images/2.png"))
            # self.setCentralWidget(label)

        elif (int(w4[0]) <= 10):
            print('롱패딩추천')
            # label1 =QLabel("",self)
            # label = QLabel()
            # label.setPixmap(QPixmap("../20211202/images/2.png"))
            # self.setCentralWidget(label)
            #
            # self.label1.setText("롱패딩추천")






if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()
    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()